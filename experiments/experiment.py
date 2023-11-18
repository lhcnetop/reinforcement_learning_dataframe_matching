import json
import pathlib
import time
from typing import List
import matplotlib
from matplotlib import pyplot as plt
import torch
from agent.agent import Agent
from agent.learner import Learner
from agent.replay_memory import ReplayMemory
from environment.concil_environment import ConcilEnv
from itertools import count
import polars as pl
import uuid
import os

DEFAULT_BATCH_SIZE = 128
DEFAULT_GAMMA = 0.999
DEFAULT_EPS_START = 0.9
DEFAULT_EPS_END = 0.05
DEFAULT_EPS_DECAY = 100
DEFAULT_TAU = 0.005
DEFAULT_LR = 1e-4
DEFAULT_REPLAY_MEMORY_SIZE=10000

is_ipython = 'inline' in matplotlib.get_backend()
plt.ion()

plt.figure(1)
plt.clf()
plt.title('Training...')
plt.xlabel('Episode')
plt.ylabel('Total Discounted Reward')

class Experiment():
    def __init__(self, 
                 results_dir:str, 
                 device:torch.device=torch.device("cuda" if torch.cuda.is_available() else "cpu"), 
                 REPLAY_MEMORY_SIZE:int=DEFAULT_REPLAY_MEMORY_SIZE, 
                 BATCH_SIZE:int=DEFAULT_BATCH_SIZE, 
                    GAMMA:float=DEFAULT_GAMMA, 
                    EPS_START:float=DEFAULT_EPS_START, 
                    EPS_END:float=DEFAULT_EPS_END, 
                    EPS_DECAY:int=DEFAULT_EPS_DECAY, 
                    TAU:float=DEFAULT_TAU, 
                    LR:float=DEFAULT_LR, 
                env_options:dict={}, 
                run_options:dict={
                    'num_warmup_episodes':100, 
                    'train_test_cycle':[100, 50], 
                    'num_cycles':9
                }
                 ):
        self.device=device
        self.GAMMA=GAMMA
        self.environment=ConcilEnv(options=env_options)
        self.memory = ReplayMemory(REPLAY_MEMORY_SIZE)
        
        self.results_dir=results_dir+uuid.uuid4().hex+'/'
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)

        # Get number of actions from gym action space
        n_actions = self.environment.action_space.n
        # Get the number of state observations
        state,  info = self.environment.reset()
        n_observations = len(state)
        
        self.learner=Learner(self.memory, n_observations,  n_actions, device, LR, GAMMA, TAU, BATCH_SIZE)

        self.agent=Agent(self.environment, self.learner, device, eps_decay={
            'start':EPS_START, 
            'end':EPS_END, 
            'decay':EPS_DECAY
        })

        self.episode_count=0
        self.episode_rewards=[]
        self.rewards_tensor = torch.tensor([],  dtype=torch.float)
        self.df_errorbars=None
        self.episode_title=''
        self.episode_index=0
        self.action_history=[]
        self.num_warmup_episodes=run_options['num_warmup_episodes']
        self.train_test_cycle=(run_options['train_test_cycle'][0], run_options['train_test_cycle'][1])
        self.num_cycles=run_options['num_cycles']

    def run(self):
        start_time=time.time()
        self.episode_title='warmup'
        random_walk_rewards=self.warmup_replay_buffer(self.num_warmup_episodes)
        self.append_rewards(random_walk_rewards)
        self.append_errorbar(random_walk_rewards)
        self.render()

        for i_cycle in range(self.num_cycles):
            self.episode_title=f'train_{i_cycle}'
            training_rewards=self.run_train_cycle(self.train_test_cycle[0])
            self.append_rewards(training_rewards)

            self.episode_title=f'test_{i_cycle}'
            test_batch_rewards=self.run_test_cycle(self.train_test_cycle[1])
            self.append_errorbar(test_batch_rewards)
            self.render()
        self.append_rewards([0])

        print(f'Salvando arquivos em {self.results_dir}')
        print(self.df_errorbars)
        plt.savefig(self.results_dir+'experiment.png')
        print(pl.DataFrame(self.action_history))
        pl.DataFrame(self.action_history).write_parquet(self.results_dir+'experiment.parquet')
        pl.DataFrame(self.action_history).write_csv(self.results_dir+'experiment.csv')
        end_time=time.time()
        print(f'Rodou em: {(end_time-start_time):0.2f}s')


    def save_action_history(self, action, step_index, reward,penalty, total_discounted_reward):
        self.action_history.append({
                'episode_type':self.episode_title, 
                'episode_index':self.episode_index, 
                'disturber_index':self.environment.distuber_index,
                'step_index':step_index, 
                'action':action, 
                'reward':reward, 
                'penalty':penalty,
                'total_discounted_reward':total_discounted_reward
            })


    def append_rewards(self, rewards_list:List):
        tensor=torch.tensor(rewards_list,  dtype=torch.float)
        self.rewards_tensor=torch.concat((self.rewards_tensor, tensor))

    def append_errorbar(self, rewards_list:List):
        x=len(self.rewards_tensor.numpy())-1
        y=pl.Series(rewards_list).mean()
        error=pl.Series(rewards_list).std()
        if self.df_errorbars is None:
            self.df_errorbars=pl.DataFrame([
                {
                    'x':x, 
                    'y':y, 
                    'error':error
                }
            ])
        else:
            self.df_errorbars=pl.concat((self.df_errorbars, pl.DataFrame([
                    {
                        'x':x, 
                        'y':y, 
                        'error':error
                    }
                ]))
            )

    def render(self):
        plt.clf()
        plt.title('Training...')
        plt.plot(self.rewards_tensor.numpy())
        x_column=self.df_errorbars.get_column('x').to_numpy()
        y_column=self.df_errorbars.get_column('y').to_numpy()
        error_column=self.df_errorbars.get_column('error').to_numpy()
        plt.errorbar(x_column, y_column, error_column, fmt='o',  linewidth=2,  capsize=6)        
        

    def warmup_replay_buffer(self, num_episodes_warmup):
        random_walk_rewards=self.run_batch_episodes(num_episodes_warmup, action_selection='random', with_training=False)
        return random_walk_rewards

    def run_train_cycle(self, num_episodes):
        return self.run_batch_episodes(num_episodes, action_selection='eps_decay', with_training=True)
    
    def run_test_cycle(self, num_episodes):
        return self.run_batch_episodes(num_episodes, action_selection='learned', with_training=False)

    def run_batch_episodes(self, 
                    num_episodes:int, 
                    action_selection:str='eps_decay', 
                    with_training:bool=True)->List[float]:
        episode_rewards=[]
        for i_episode in range(num_episodes):
            start_time=time.time()
            episode_total_discounted_reward=self.run_episode(action_selection=action_selection, with_training=with_training)
            end_time=time.time()
            print(f'Rodou episodio {self.episode_title} {i_episode} com disturber{self.environment.distuber_index} em {end_time-start_time:.2f}s / recompensa: {episode_total_discounted_reward:.1f}')
            episode_rewards.append(episode_total_discounted_reward)
        return episode_rewards
            


    def run_episode(self, 
                    action_selection:str='eps_decay', 
                    with_training:bool=True
                    )->float:
        self.episode_index+=1
        state,  info = self.environment.reset()
        state = torch.tensor(state,  dtype=torch.float32,  device=self.device).unsqueeze(0)
        total_discounted_reward=0

        for t in count():
            if action_selection=='random':
                action= self.agent.select_random_action()
            elif action_selection=='learned':
                action=self.agent.select_policy_action(state)
            else:
                action=self.agent.select_action(state) 
    #        action = select_action(state)
            
            observation,  reward,  terminated,  truncated,  _ = self.environment.step(action.item())
            
            total_discounted_reward+=pow(self.GAMMA, t)*reward
            self.save_action_history(action=action.item(), step_index=t, reward=reward,penalty=self.environment.penalty, total_discounted_reward=total_discounted_reward)
            
            reward = torch.tensor([reward],  device=self.device)
            done = terminated or truncated

            if terminated:
                next_state = None
            else:
                next_state = torch.tensor(observation,  dtype=torch.float32,  device=self.device).unsqueeze(0)

            # Store the transition in memory
            self.memory.push(state,  action,  next_state,  reward)

            # Move to the next state
            state = next_state

            if with_training:
                # Perform one step of the optimization (on the policy network)
                self.learner.optimize_model()
                self.learner.update_target_network()

            if done:
                #self.episode_rewards.append(cumulative_reward)
                #plot_durations()
                break

        return total_discounted_reward
    
    @staticmethod
    def from_json(json_file_path:str):
        path=pathlib.Path(json_file_path)
        results_dir=str(path.parent)+'/'
        with open(json_file_path) as json_file:
            json_spec=json.load(json_file)
            print(json_spec)
            experiment=Experiment(
                results_dir=results_dir, 
                REPLAY_MEMORY_SIZE=json_spec['REPLAY_MEMORY_SIZE'], 
                BATCH_SIZE=json_spec['BATCH_SIZE'], 
                GAMMA=json_spec['GAMMA'], 
                EPS_START=json_spec['EPS_START'], 
                EPS_END=json_spec['EPS_END'], 
                EPS_DECAY=json_spec['EPS_DECAY'], 
                TAU=json_spec['TAU'], 
                LR=json_spec['LR'], 
                env_options=json_spec['env_options'], 
                run_options=json_spec['run_options']
            )
            return experiment
        #raise CouldNotLoadJsonFile(message=f'Não foi possível carregar o arquivo {json_file_path} json para gerar um experimento')


class CouldNotLoadJsonFile(Exception):
    def __init__(self,  message="Não foi possível carregar o arquivo json para gerar um experimento"):
        self.message = message
        super().__init__(self.message)
