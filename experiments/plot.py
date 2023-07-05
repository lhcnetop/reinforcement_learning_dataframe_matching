
from typing import List
import matplotlib
import matplotlib.pyplot as plt
import torch

is_ipython = 'inline' in matplotlib.get_backend()
plt.ion()

def plot_rewards(total_reward_list:List[float],show_result=False):
    plt.figure(1)
    rewards = torch.tensor(total_reward_list, dtype=torch.float)
    if show_result:
        plt.title('Result')
    else:
        plt.clf()
        plt.title('Training...')
    plt.xlabel('Episode')
    plt.ylabel('Episode Total Discounted Reward')
    plt.plot(rewards.numpy())
    
    if len(rewards) >= 10:
        means = rewards.unfold(0, 10, 1).mean(1).view(-1)
        means = torch.cat((torch.zeros(9), means))
        plt.plot(means.numpy())
    plt.annotate('Teste anotação',(100,10))
    plt.pause(0.001)  # pause a bit so that plots are updated