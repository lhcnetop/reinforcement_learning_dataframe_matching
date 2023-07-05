from gymnasium.spaces import Box,Discrete,Tuple
import numpy as np
import polars as pl
from strsimpy.normalized_levenshtein import NormalizedLevenshtein
from strsimpy.cosine import Cosine

from environment.actions import get_action_space

normalized_levenshtein = NormalizedLevenshtein()
cosine=Cosine(3)

class State:
    def __init__(self,options:dict={}):
        
        n_actions=get_action_space().n  
        self.actions_taken=[]
        for i in range(n_actions):
            self.actions_taken.append(0)

        self.included_metrics=options.get('included_metrics',
            {
                'avg':True,
                'min':False,
                'max':False,
                'quantile_10':False,
                'quantile_90':False
            }
        )

        self.disturber=[0,1,0] ## Pode ser utilizado para que o agente aprenda a otimizar por disturber
        self.step_index=0
        self.size_df_disturbed=0 ##<=10^6
        self.size_df_original=0 ##<=10^6
        self.size_df_pending_match=0 ##<=10^6
        self.avg_match_grade=0 ## >=0, <=1
        self.percent_matched=0 ## >=0, <=1

    def set_step_index(self,step_index:int):
        self.step_index=step_index
    
    def set_action_taken(self,action_index:int):
        self.actions_taken[action_index]=1

    def set_size_df_disturbed(self,size:int):
        self.size_df_disturbed=size

    def set_size_df_original(self,size:int):
        self.size_df_original=size

    def set_size_df_pending_match(self,size:int):
        self.size_df_pending_match=size

    def set_avg_match_grade(self,grade:float):
        if not (0 <= grade <= 1):
            raise GradeNotInRangeError(grade)
        self.avg_match_grade=grade

    def set_percent_matched(self,percent:int):
        if not (0 <= percent <=1):
            print(f'Percentual: {percent}')
            raise PercentNotInRangeError(percent)
        self.percent_matched=percent


    def get_observation(self):
        state=(
#            self.size_df_disturbed, ##Removendo os parametros que estão em outra escala
#            self.size_df_original, ##Removendo os parametros que estão em outra escala
#            self.size_df_pending_match, ##Removendo os parametros que estão em outra escala
            self.avg_match_grade,
            self.percent_matched,
#            self.step_index, ##Removendo os parametros que estão em outra escala
            self.actions_taken[0],
            self.actions_taken[1],
            self.actions_taken[2],
            self.actions_taken[3],
            self.actions_taken[4],
            self.actions_taken[5],
            self.actions_taken[6],
            )
#        print(state)
        return state

    def get_observation_space(self):
        observation_space=Tuple(
            (
#            Discrete(self.size_df_disturbed),
#            Discrete(self.size_df_original),
#            Discrete(self.size_df_disturbed),
            Box(low=0,high=1),
            Box(low=0,high=1),
#            Discrete(100),
            Discrete(1), #actions_taken[0]
            Discrete(1), #actions_taken[1]
            Discrete(1), #actions_taken[2]
            Discrete(1), #actions_taken[3]
            Discrete(1), #actions_taken[4]
            Discrete(1), #actions_taken[5]
            Discrete(1), #actions_taken[6]
            )
            )
        return observation_space
        
def get_match_grade_metrics(df_original:pl.DataFrame,df_disturbed:pl.DataFrame,df_matched:pl.DataFrame):
    grade_series=(df_matched
        .join(df_original, on='id')
        .join(df_disturbed, on='disturbed_id')
        .with_columns(
            (pl.struct(["field1","field2","field3", "disturbed_field1","disturbed_field2","disturbed_field3"])
                .apply(get_matched_row_grade_metrics)
                .alias('match_grade')
                )
        ).get_column('match_grade')
        )
    avg=grade_series.mean()
    min=grade_series.min()
    max=grade_series.max()
    quantile_10=grade_series.quantile(0.1)
    quantile_90=grade_series.quantile(0.9)
    
    return {
        'avg':avg,
        'min':min,
        'max':max,
        'quantile_10':quantile_10,
        'quantile_90':quantile_90
    }

def get_matched_row_grade_metrics(struct: dict)->float:
    grade_field1=cosine.similarity(struct['field1'],struct['disturbed_field1'])
    grade_field2=cosine.similarity(struct['field2'],struct['disturbed_field2'])
    grade_field3=cosine.similarity(struct['field3'],struct['disturbed_field3'])
    grade=(grade_field1+grade_field2+grade_field3)/3
    return grade
        
class GradeNotInRangeError(Exception):
    def __init__(self, grade, message="Grade is not in [0,1] range"):
        self.Grade = grade
        self.message = message
        super().__init__(self.message)

class PercentNotInRangeError(Exception):
    def __init__(self, grade, message="Percent is not in [0,1] range"):
        self.Grade = grade
        self.message = message
        super().__init__(self.message)


