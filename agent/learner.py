

from agent.dqn import PolicyNetwork
from agent.replay_memory import ReplayMemory

import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class Learner():
    def __init__(self, 
                 replay_memory:ReplayMemory, 
                 observation_space_size:int, 
                 action_space_size:int, 
                 device:torch.device, 
                 learning_rate:float=1e-4, 
                 gamma:float=0.99, 
                 tau:float=0.005, 
                 batch_size:int=128,
                 hidden_layer1:int=64,
                 hidden_layer2:int=64,
                 ):
        self.policy_net = PolicyNetwork(observation_space_size,  action_space_size,hidden_layer1,hidden_layer2).to(device)
        self.target_net = PolicyNetwork(observation_space_size,  action_space_size,hidden_layer1,hidden_layer2).to(device)
        self.target_net.load_state_dict(self.policy_net.state_dict())

        self.optimizer = optim.AdamW(self.policy_net.parameters(),  lr=learning_rate,  amsgrad=True)
        self.memory = replay_memory
        self.gamma=gamma
        self.tau=tau
        self.batch_size=batch_size
        self.device=device


    def optimize_model(self):
        batch = self.memory.get_batch(self.batch_size)
        if batch is None:
            return

        # Compute a mask of non-final states and concatenate the batch elements
        # (a final state would've been the one after which simulation ended)
        non_final_mask = torch.tensor(tuple(map(lambda s: s is not None, 
                                            batch.next_state)),  device=self.device,  dtype=torch.bool)
        aux=[s for s in batch.next_state if s is not None]
        non_final_next_states = torch.cat(aux)
        state_batch = torch.cat(batch.state)
        action_batch = torch.cat(batch.action)
        reward_batch = torch.cat(batch.reward)

        # Compute Q(s_t,  a) - the model computes Q(s_t),  then we select the
        # columns of actions taken. These are the actions which would've been taken
        # for each batch state according to policy_net
        state_action_values = self.policy_net(state_batch).gather(1,  action_batch)

        # Compute V(s_{t+1}) for all next states.
        # Expected values of actions for non_final_next_states are computed based
        # on the "older" target_net; selecting their best reward with max(1)[0].
        # This is merged based on the mask,  such that we'll have either the expected
        # state value or 0 in case the state was final.
        next_state_values = torch.zeros(self.batch_size,  device=self.device)
        with torch.no_grad():
            next_state_values[non_final_mask] = self.target_net(non_final_next_states).max(1)[0]
        # Compute the expected Q values
        expected_state_action_values = (next_state_values * self.gamma) + reward_batch

        # Compute Huber loss
        criterion = nn.SmoothL1Loss()
        loss = criterion(state_action_values,  expected_state_action_values.unsqueeze(1)) ## Essa é a linha que determina que o modelo é uma DDQN ao invés de uma DQN

        # Optimize the model
        self.optimizer.zero_grad()
        loss.backward()
        # In-place gradient clipping
        torch.nn.utils.clip_grad_value_(self.policy_net.parameters(),  100)
        self.optimizer.step()

    def update_target_network(self):
        # Soft update of the target network's weights
        # θ′ ← τ θ + (1 −τ )θ′
        target_net_state_dict = self.target_net.state_dict()
        policy_net_state_dict = self.policy_net.state_dict()
        for key in policy_net_state_dict:
            target_net_state_dict[key] = policy_net_state_dict[key]*self.tau + target_net_state_dict[key]*(1-self.tau)
        self.target_net.load_state_dict(target_net_state_dict)