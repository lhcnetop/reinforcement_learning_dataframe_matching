import polars as pl

from disturb.disturbed_df import DisturbedDataframe


def disturb1(df:pl.DataFrame, sample_size:int=None, options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df,sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1',0.2) 
    disturb_probability_field2=options.get('disturb_probability_field2',0.2)
    disturb_probability_field3=options.get('disturb_probability_field3',0.1)
    

    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1',1,probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1','0',probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1','0000',probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1',3,probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2',1,probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2','0',probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2','000000',probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2',4,probability=disturb_probability_field2)

    ## Field2 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3',1,probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3','0',probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3','00',probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3',4,probability=disturb_probability_field3)
    return disturbed_df