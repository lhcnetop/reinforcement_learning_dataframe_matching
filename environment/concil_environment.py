from gymnasium import Env
import polars as pl
import numpy.random as rand
from environment.actions import *
import time

from environment.state import State, get_match_grade_metrics
from disturb.disturbers import *
from random_data_generators.df_generator import generate_df

### Usar https://github.com/deepmind/acme/blob/master/acme/wrappers/gym_wrapper.py para encapsular esse ambiente no dm_env
class ConcilEnv(Env):
    def __init__(self, 
                 seed:int=1, 
                 options:dict={}
                 ):
        super().__init__()
        self.seed=seed, 
        self.options=options

        self.wrong_match_penalty=options.get('wrong_match_penalty', 0)
        self.dataframe_height=options.get('dataframe_height', pow(10, 4))

        self.custom_state=State()
        self.custom_state.set_size_df_original(self.dataframe_height)
        self.custom_state.set_size_df_disturbed(self.dataframe_height)
        self.observation_space=self.custom_state.get_observation_space()        
        self.penalty=0
        self.action_space=get_action_space()
        self.actions_array=get_actions_array()  
        self.wrong_match_penalty=options['wrong_match_penalty']      
        

        self.reset()


    def get_random_disturber(self):
        aux_array=[disturb1,disturb2,disturb3,disturb4,disturb5,disturb6,disturb7,disturb8,disturb9,disturb10,disturb11,disturb12,disturb13,disturb14,disturb15]
        random_int=rand.choice(len(aux_array))
        self.distuber_index=random_int
        return aux_array[random_int]

    def reset(self):
        super().reset(seed=self.seed[0], options=self.options)
        ### rand.seed=seed
        self.df_original=generate_df(self.dataframe_height)
        self.df_disturbed=self.get_random_disturber()(self.df_original).df
        #print(f'Rodando com disturber: {self.distuber_index}')

        self.df_matches=None
        self.custom_state=State()
        self.custom_state.set_disturber(self.distuber_index)
        self.custom_state.set_size_df_original(self.df_original.height)
        self.custom_state.set_size_df_disturbed(self.df_original.height)
        self.custom_state.set_size_df_pending_match(0)
        self.custom_state.set_avg_match_grade(0)
        self.custom_state.set_percent_matched(0)
        self.custom_state.set_step_index(0)
        self.iteration_counter=0
        obs=self.custom_state.get_observation()
        info={}
        '''
        print('------------ DF Original ------------')
        print(self.df_original)
        print('------------ DF Perturbado ------------')
        print(self.df_disturbed)
        '''
        return (obs, info)
        
    
    def step(self, action):
        self.iteration_counter+=1
        self.custom_state.set_action_taken(action)
        self.custom_state.set_step_index(self.iteration_counter)
        acao=get_action(action)

        startTime=time.time()
        if self.df_matches is not None:
            df_disturbed=self.df_disturbed.clone().join(self.df_matches,  on='disturbed_id', how='anti')
            df_original=self.df_original.clone().join(self.df_matches,  on='id', how='anti')
        else:
            df_disturbed=self.df_disturbed.clone()
            df_original=self.df_original.clone()

        matched_df=acao['function'](df_original, df_disturbed)
        '''
        print('------------ DF Combinado ------------')
        print(matched_df.filter(pl.col('id')!=pl.col('disturbed_id')))
        '''
        endTime=time.time()
        reward,penalty=self.get_reward(matched_df)
        penalty+=(endTime-startTime)
        #reward+=(endTime-startTime)
        self.penalty=penalty
        #print(f'Reward: {reward}, Penalty:{penalty}')
        if self.df_matches is None:
           self.df_matches=matched_df
        else:
            self.df_matches=pl.concat([self.df_matches, matched_df])

        self.custom_state.set_avg_match_grade(
            get_match_grade_metrics(self.df_original, self.df_disturbed, self.df_matches)['avg']
        )
        size_df_pending_match=self.df_disturbed.join(self.df_matches,  on='disturbed_id', how='anti').height
        self.custom_state.set_size_df_pending_match(size_df_pending_match)
        self.custom_state.set_percent_matched(self.df_disturbed.join(self.df_matches,  on='disturbed_id').height/self.df_disturbed.height)
        obs=self.custom_state.get_observation()
        
        terminated=self.get_termination_condition(size_df_pending_match)
        truncated=self.get_truncation_condition()
        info={}
        return (obs, reward, terminated, truncated, info)
        
    
    def render(self):
        return
        #print(f'Linhas restantes - Original: {self.df_original.join(self.df_matches,  on="id", how="anti").height}')
        #print(f'Estado atual - Pending Match: {self.custom_state.size_df_pending_match} / % matched: {self.custom_state.percent_matched} / avg grade: {self.custom_state.avg_match_grade}')
    
    def close(self):
        return
        
    
    def get_termination_condition(self, size_df_pending_match:int):
        if size_df_pending_match==0:
            return True
        return False
    
    def get_truncation_condition(self):
        if self.iteration_counter>=20:
            return True
        return False
    
    #TODO adicionar métrica de penalização por lentidao
    def get_reward(self, matched_df:pl.DataFrame):
        #print(self.wrong_match_penalty)
        if (not matched_df is None) & (matched_df.height>0):
            reward_column=(matched_df
                    .with_columns(
                        pl.struct(['id', 'disturbed_id'])
                        .apply(lambda x: 1 if (x['id']==x['disturbed_id']) else self.wrong_match_penalty)
                        .alias('reward')
                                )
                    .get_column('reward'))
            reward = reward_column.sum()
            total_penalty=reward_column.to_frame().filter(pl.col('reward')<0).get_column('reward').sum()
            return [reward,total_penalty]
        else:
            return 0,0