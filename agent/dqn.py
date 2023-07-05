from __future__ import annotations

import random

import matplotlib.pyplot as plt
import seaborn as sns
import torch
import torch.nn as nn
import numpy as np

import gymnasium as gym


plt.rcParams["figure.figsize"] = (10, 5)

class PolicyNetwork(nn.Module):
    """Parametrized Policy Network."""

    def __init__(self, obs_space_dims: int, action_space_dims: int):
        """Initializes a neural network that estimates the mean and standard deviation
         of a normal distribution from which an action is sampled from.

        Args:
            obs_space_dims: Dimension of the observation space
            action_space_dims: Dimension of the action space
        """
        super().__init__()

        hidden_space1 = 16  # Nothing special with 16, feel free to change
        hidden_space2 = 16  # Nothing special with 32, feel free to change

        # Shared Network
        self.shared_net = nn.Sequential(
            nn.Linear(obs_space_dims, hidden_space1),
            nn.Tanh(),
            nn.Linear(hidden_space1, hidden_space2),
            nn.Tanh(),
        )

        # Policy Mean specific Linear Layer
        self.policy_action_net = nn.Sequential(
            nn.Linear(hidden_space2, action_space_dims)
        )

        ## Como o problema é diferente, não precisaremos deste outro output
        # Policy Std Dev specific Linear Layer
        #self.policy_stddev_net = nn.Sequential(
        #    nn.Linear(hidden_space2, action_space_dims)
        #)

    def forward(self, x: torch.Tensor) -> tuple[torch.Tensor]:
        """Conditioned on the observation, returns the mean and standard deviation
         of a normal distribution from which an action is sampled from.

        Args:
            x: Observation from the environment

        Returns:
            action_means: predicted mean of the normal distribution
            action_stddevs: predicted standard deviation of the normal distribution
        """
        shared_features = self.shared_net(x.float())

        action_values = self.policy_action_net(shared_features)
        ## Como o problema é diferente, não precisaremos deste outro output
        #action_stddevs = torch.log(
        #    1 + torch.exp(self.policy_stddev_net(shared_features))
        #)

        return action_values
    
