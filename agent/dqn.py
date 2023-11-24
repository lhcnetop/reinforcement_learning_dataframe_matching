from __future__ import annotations

import random

import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn as nn
import numpy as np

import gymnasium as gym


plt.rcParams["figure.figsize"] = (10,  5)

class PolicyNetwork(nn.Module):
    """Parametrized Policy Network."""

    def __init__(self,  obs_space_dims: int,  action_space_dims: int):
        """Initializes a neural network that estimates the mean and standard deviation
         of a normal distribution from which an action is sampled from.

        Args:
            obs_space_dims: Dimension of the observation space
            action_space_dims: Dimension of the action space
        """
        super().__init__()

        hidden_space1 = 16
        hidden_space2 = 16

        self.shared_net = nn.Sequential(
            nn.Linear(obs_space_dims,  hidden_space1), 
            nn.Tanh(), 
            nn.Linear(hidden_space1,  hidden_space2), 
            nn.Tanh(), 
        )

        self.policy_action_net = nn.Sequential(
            nn.Linear(hidden_space2,  action_space_dims)
        )


    def forward(self,  x: torch.Tensor) -> tuple[torch.Tensor]:
        
        shared_features = self.shared_net(x.float())

        action_values = self.policy_action_net(shared_features)
        
        return action_values
    

