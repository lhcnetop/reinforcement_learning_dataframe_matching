import polars as pl
import random as rand

from random_data_generators.type_generators.string_generator import get_random_string

class DisturbedDataframe():

    def __init__(self, df:pl.DataFrame, sample_size:int=None):
        self.df=df.clone()
        if sample_size is not None:
            self.df=df.sample(n=sample_size, shuffle=True)
        #print(self.df.schema)
        self.df=self.df.rename({
            'id':'disturbed_id', 
            'field1':'disturbed_field1', 
            'field2':'disturbed_field2', 
            'field3':'disturbed_field3', 
        })


    def suffix_string(self,  field:str,  suffix_string,  probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x)+suffix_string if rand.random()<=probability else str(x) )
        )

    def prefix_string(self,  field:str,  prefix_string,  probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: prefix_string+str(x) if rand.random()<=probability else str(x) )
        )

    def suffix_random_string(self,  field:str,  random_string_length:int,  probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x)+get_random_string(random_string_length) if rand.random()<=probability else str(x) )
        )

    def prefix_random_string(self,  field:str,  random_string_length:int,  probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: get_random_string(random_string_length)+str(x) if rand.random()<=probability else str(x) ) 
        )


    def trim_left(self, field:str, length:int, probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x)[length:] if rand.random()<=probability else str(x) )
        )

    def trim_right(self, field:str, length:int, probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x)[:-length] if rand.random()<=probability else str(x) )
        )


    def trim_char_left(self, field:str, chars:str, probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x).lstrip(chars) if rand.random()<=probability else str(x) )
        )

    def trim_char_right(self, field:str, chars:str, probability:float=1.0):
        self.df=self.df.with_columns(
            pl.col(field).apply(lambda x: str(x).rstrip(chars) if rand.random()<=probability else str(x) )
        )