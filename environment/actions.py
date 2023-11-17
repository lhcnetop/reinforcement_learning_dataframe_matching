import numpy
import polars as pl
from gymnasium.spaces import Discrete

from typing import List

from environment.state import get_matched_row_grade_metrics

# TODO alterar para o match pegar apenas os remanescentes
# TODO permitir que o match seja com base em similaridade
def get_match_equals(original_fields:List[str], disturbed_fields:List[str]):
    def match_equals(df_original:pl.DataFrame, df_disturbed:pl.DataFrame):
        #print(f'Exectuando match_equals nas colunas: {original_fields}')
        matched_df=df_disturbed.join(df_original, left_on=disturbed_fields, right_on=original_fields)
        return matched_df.select(['id', 'disturbed_id'])
    return match_equals

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


actions_map={
    'match_equals_field_1':get_match_equals(['field1'], ['disturbed_field1']), 
    'match_equals_field_2':get_match_equals(['field2'], ['disturbed_field2']), 
    'match_equals_field_3':get_match_equals(['field3'], ['disturbed_field3']), 
    'match_equals_fields_1_2':get_match_equals(['field1', 'field2'], ['disturbed_field1', 'disturbed_field2']), 
    'match_equals_fields_3_2':get_match_equals(['field3', 'field2'], ['disturbed_field3', 'disturbed_field2']), 
    'match_equals_fields_3_1':get_match_equals(['field3', 'field1'], ['disturbed_field3', 'disturbed_field1']), 
    'match_equals_fields_1_2_3':get_match_equals(['field3', 'field1', 'field2'], ['disturbed_field3', 'disturbed_field1', 'disturbed_field2']),
    'match_close_08':get_match_close(0.8)
}

def get_actions_array():
    actions_array=[]    
    for action in actions_map:
        actions_array.append(action)
    return actions_array

def get_action_space():
    qtd_acoes_possiveis=len(get_actions_array())
    return Discrete(qtd_acoes_possiveis)

def get_action(action:numpy.int64)->dict:
        function_name=get_actions_array()[action]
        return {
             'function':actions_map[function_name], 
             'name':function_name
        }


