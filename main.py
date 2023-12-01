## Implementação seguindo: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
import polars as pl


from environment.utils import get_matched_row_grade_metrics
from experiments.experiment import Experiment
from random_data_generators.df_generator import generate_df


experiment=Experiment.from_json('/home/lhcn/Documents/Pessoal/Mestrado2023/Deep RL/Projeto plano B/Experiments_20231128/Experimento_BaixaCardin_128_128_batch3000_apenasDisturber5/Experimento.json')
experiment.run()