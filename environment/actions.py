import numpy
import polars as pl
from gymnasium.spaces import Discrete

from typing import List


def get_match_equals(original_fields:List[str],disturbed_fields:List[str]):
    def match_equals(df_original:pl.DataFrame,df_disturbed:pl.DataFrame):
        #print(f'Exectuando match_equals nas colunas: {original_fields}')
        matched_df=df_disturbed.join(df_original,left_on=disturbed_fields,right_on=original_fields)
        return matched_df.select(['id','disturbed_id'])
    return match_equals


actions_map={
    'match_equals_field_1':get_match_equals(['field1'],['disturbed_field1']),
    'match_equals_field_2':get_match_equals(['field2'],['disturbed_field2']),
    'match_equals_field_3':get_match_equals(['field3'],['disturbed_field3']),
    'match_equals_fields_1_2':get_match_equals(['field1','field2'],['disturbed_field1','disturbed_field2']),
    'match_equals_fields_3_2':get_match_equals(['field3','field2'],['disturbed_field3','disturbed_field2']),
    'match_equals_fields_3_1':get_match_equals(['field3','field1'],['disturbed_field3','disturbed_field1']),
    'match_equals_fields_1_2_3':get_match_equals(['field3','field1','field2'],['disturbed_field3','disturbed_field1','disturbed_field2'])
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