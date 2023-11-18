## Implementação seguindo: https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html
import polars as pl


from environment.utils import get_matched_row_grade_metrics
from experiments.experiment import Experiment
from random_data_generators.df_generator import generate_df


experiment=Experiment.from_json('/home/lhcn/Documents/Pessoal/Mestrado2023/Deep RL/Projeto plano B/Experimento2_1/Experimento.json')
experiment.run()
'''

dataframe_height=100

df_original=generate_df(dataframe_height)

print(df_original.dtypes)

df_disturbed=disturb1(df_original).df

print(df_original.height)

df_matched=df_disturbed.join(df_original,how='cross')
df_matched=df_disturbed.join(df_original,how='cross').with_columns(
    pl.struct(['field1', 'disturbed_field1','field2', 'disturbed_field2','field3', 'disturbed_field3'])
    .apply(get_matched_row_grade_metrics)
    .alias('similarity')
).filter(
    pl.col('similarity')>0.1
).sort(
    by=['disturbed_id','similarity'],
    descending=[False,True]
).groupby(
    by=['disturbed_id'],maintain_order=True
).first()



#print(df_matched)
print(df_matched.describe)

def get_match_close(threshold:float):
    def match_close(df_original:pl.DataFrame, df_disturbed:pl.DataFrame):
        df_matched=df_disturbed.join(df_original,how='cross').with_columns(
            pl.struct(['field1', 'disturbed_field1','field2', 'disturbed_field2','field3', 'disturbed_field3'])
            .apply(get_matched_row_grade_metrics)
            .alias('similarity')
        ).filter(
            pl.col('similarity')>threshold
        ).sort(
            by=['disturbed_id','similarity'],
            descending=[False,True]
        ).groupby(
            by=['disturbed_id'],maintain_order=True
        ).first()
        return df_matched
    return match_close


print(get_match_close(0.99)(df_original=df_original,df_disturbed=df_disturbed).describe)

print(get_match_close(0.5)(df_original=df_original,df_disturbed=df_disturbed).describe)
'''