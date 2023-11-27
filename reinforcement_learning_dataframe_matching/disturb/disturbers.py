import polars as pl

from disturb.disturbed_df import DisturbedDataframe



def disturb1(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.2) 
    disturb_probability_field2=options.get('disturb_probability_field2', 0.1)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.2)
    

    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 1, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 3, probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 1, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '0', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '000000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 4, probability=disturb_probability_field2)

    ## Field2 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    return disturbed_df


def disturb2(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.2) 
    disturb_probability_field2=options.get('disturb_probability_field2', 0.1)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.2)
    

    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 1, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 3, probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 1, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '0', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '000000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 4, probability=disturb_probability_field2)

    ## Field2 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    return disturbed_df


def disturb3(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.2) 
    disturb_probability_field2=options.get('disturb_probability_field2', 0.1)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.99)
    

    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 1, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 3, probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 1, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '0', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '000000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 4, probability=disturb_probability_field2)

    ## Field2 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 7, probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    return disturbed_df


def disturb4(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.8)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.15)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.1)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 3, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '000', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 4, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '00000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '000000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 7, probability=disturb_probability_field3)
    disturbed_df.trim_char_right('disturbed_field3', '000', probability=disturb_probability_field2)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    return disturbed_df

def disturb5(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.08)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.60)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.30)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 3, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '000', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_field1)
    disturbed_df.trim_and_substitute_random_right('disturbed_field1', 2, probability=disturb_probability_field3)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 4, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '00000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '0000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 2, probability=disturb_probability_field2)
    disturbed_df.trim_and_substitute_random_left('disturbed_field2', 3, probability=disturb_probability_field2)

    ## Field3 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field3', 5, probability=disturb_probability_field3)
    disturbed_df.trim_char_right('disturbed_field3', '000', probability=disturb_probability_field2)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 3, probability=disturb_probability_field3)
    return disturbed_df

def disturb6(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.25)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.95)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.07)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 3, probability=disturb_probability_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 4, probability=disturb_probability_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 5, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_field3)
    return disturbed_df

def disturb7(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.08)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.07)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.99)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.05)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.04)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.03)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '00', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_right('disturbed_field2', '00', probability=disturb_probability_field2)
    disturbed_df.suffix_string('disturbed_field2', '000000', probability=disturb_probability_intense_field2)
    disturbed_df.suffix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.trim_char_right('disturbed_field3', '000', probability=disturb_probability_field2)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    return disturbed_df

def disturb8(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.08)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.80)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.15)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.07)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.05)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.10)


    ## Field1 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field1', 3, probability=disturb_probability_field1)
    disturbed_df.trim_char_left('disturbed_field1', '000', probability=disturb_probability_field1)
    disturbed_df.prefix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.prefix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)

    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 4, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '00000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '000000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)
    disturbed_df.trim_and_substitute_random_left('disturbed_field2', 6, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field3', 5, probability=disturb_probability_field3)
    disturbed_df.trim_char_right('disturbed_field3', '000', probability=disturb_probability_field2)
    disturbed_df.suffix_random_string('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb9(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.85)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.20)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.15)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.10)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.02)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.05)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb10(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.85)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.07)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb11(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.85)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.00)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.07)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.00)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb12(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.85)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.00)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.07)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.00)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb13(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.85)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.00)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb14(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.80)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.00)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.00)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df

def disturb15(df:pl.DataFrame,  sample_size:int=None,  options:dict={})->DisturbedDataframe:
    disturbed_df=DisturbedDataframe(df, sample_size)
    disturb_probability_field1=options.get('disturb_probability_field1', 0.85)
    disturb_probability_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_field3=options.get('disturb_probability_field3', 0.00)
    disturb_probability_intense_field1=options.get('disturb_probability_field1', 0.00)
    disturb_probability_intense_field2=options.get('disturb_probability_field2', 0.00)
    disturb_probability_intense_field3=options.get('disturb_probability_field3', 0.00)


    ## Field1 perturbado mexendo à direita
    disturbed_df.trim_right('disturbed_field1', 2, probability=disturb_probability_field1)
    disturbed_df.trim_char_right('disturbed_field1', '0', probability=disturb_probability_field1)
    disturbed_df.suffix_string('disturbed_field1', '0000', probability=disturb_probability_intense_field1)
    disturbed_df.suffix_random_string('disturbed_field1', 4, probability=disturb_probability_intense_field1)


    ## Field2 perturbado mexendo à esquerda
    disturbed_df.trim_left('disturbed_field2', 3, probability=disturb_probability_field2)
    disturbed_df.trim_char_left('disturbed_field2', '000', probability=disturb_probability_field2)
    disturbed_df.prefix_string('disturbed_field2', '00000', probability=disturb_probability_intense_field2)
    disturbed_df.prefix_random_string('disturbed_field2', 5, probability=disturb_probability_intense_field2)

    ## Field3 perturbado mexendo à esquerda e à direita
    disturbed_df.trim_right('disturbed_field3', 1, probability=disturb_probability_field3)
    disturbed_df.trim_char_left('disturbed_field3', '0', probability=disturb_probability_field3)
    disturbed_df.prefix_string('disturbed_field3', '00', probability=disturb_probability_field3)
    disturbed_df.suffix_random_string('disturbed_field3', 3, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_right('disturbed_field3', 4, probability=disturb_probability_field3)
    disturbed_df.trim_and_substitute_random_left('disturbed_field3', 7, probability=disturb_probability_intense_field3)
    disturbed_df.prefix_random_string('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    disturbed_df.trim_left('disturbed_field3', 6, probability=disturb_probability_intense_field3)
    return disturbed_df
