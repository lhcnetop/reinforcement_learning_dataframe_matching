## Implementação seguindo: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
import polars as pl

from experiments.experiment import Experiment

results_default_dir='/home/lhcn/Documents/Pessoal/Mestrado2023/Sardinha/Experiments/'


experiment=Experiment.from_json('/home/lhcn/Documents/Pessoal/Mestrado2023/Sardinha/Experiments/Experimento4/Experimento.json')
experiment.run()
