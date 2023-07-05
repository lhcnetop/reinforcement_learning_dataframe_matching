import polars as pl
from random_data_generators.type_generators.string_generator import get_list_of_random_strings


def generate_df(data_size:int)->pl.DataFrame:
    pre_dataframe={
        "id":range(data_size),
        "field1":get_list_of_random_strings(6,data_size),
        "field2":get_list_of_random_strings(8,data_size), 
        "field3":get_list_of_random_strings(10,data_size)
    }

    df=pl.DataFrame(pre_dataframe)
    return df