import polars as pl
from  random_data_generators.type_generators.int_generator import *

'''
def generate_df(data_size:int)->pl.DataFrame:
    pre_dataframe={
        "id":range(data_size), 
        "field1":get_list_of_random_strings(6, data_size), 
        "field2":get_list_of_random_strings(8, data_size),  
        "field3":get_list_of_random_strings(10, data_size)
    }

    df=pl.DataFrame(pre_dataframe)
    return df
    '''

def generate_df(data_size:int)->pl.DataFrame:
    pre_dataframe={
        "id":range(data_size), 
        "field1":get_list_of_random_integers(4, data_size),
        "field2":get_list_of_random_correlated_integers(6,get_random_integer(3), data_size),
        "field3":get_list_of_random_correlated_integers(8,get_random_integer(4), data_size),
    }
    df=pl.DataFrame(pre_dataframe)
    df=df.select(
        pl.col('id'),
        pl.col('field1').cast(pl.Utf8),
        pl.col('field2').cast(pl.Utf8),
        pl.col('field3').cast(pl.Utf8),
                 )
    return df
