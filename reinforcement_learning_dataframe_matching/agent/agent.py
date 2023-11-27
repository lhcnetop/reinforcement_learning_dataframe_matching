import gymnasium as gym
import random
import math
import torch

from agent.learner import Learner

## Implementar conforme: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html

class Agent:
    def __init__(self, 
                environment:gym.Env, 
                learner:Learner, 
                device:torch.device, 
                eps_decay:dict
                ):
        self.environment=environment
        self.learner=learner
        self.device=device
        self.eps_decay=eps_decay
        self.steps_done=0

    def select_action(self, state, decay_eps:bool=True):
        sample = random.random()
        epsilon=self.get_epsilon()
        
        if decay_eps:
            self.steps_done+=1
        if sample > epsilon:
            return self.select_policy_action(state)
        else:
            return self.select_random_action()

    def get_epsilon(self):
        eps_threshold = self.eps_decay['end'] + (self.eps_decay['start'] - self.eps_decay['end']) * \
            math.exp(-1. * self.steps_done / self.eps_decay['decay'])
        return eps_threshold
    
    def select_policy_action(self, state):
        with torch.no_grad():
            return self.learner.policy_net(state).max(1)[1].view(1,  1)
            '''
            aux=self.learner.policy_net(state)
            aux2=aux.max(0)
            aux4=aux2[1]
            aux3=aux4.view(1,  1)
            return aux3
            '''
    
    def select_random_action(self):
        return torch.tensor([[self.environment.action_space.sample()]],  device=self.device,  dtype=torch.long)

    def select_custom_action(self,state):
        return torch.tensor([[self.environment.action_space.sample()]],  device=self.device,  dtype=torch.long)