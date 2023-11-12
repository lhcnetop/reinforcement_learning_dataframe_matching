import random
import numpy.random as nprand

def get_list_of_random_correlated_integers(length:int, average_increment:float, size:int):
    print(f'Inicializando array aleatorio correlacionado de {size} inteiros com tamanho de string: {length}, incremento médio: {average_increment}')
    list_of_random_integers=[]
    seed=get_random_integer(length)
    list_of_random_integers.append(seed)
    random_increments=nprand.poisson(lam=average_increment,size=size-1)
    cumulative_increments=random_increments.cumsum()
    list_of_random_integers=[*list_of_random_integers,*(seed+cumulative_increments).tolist()]    
    return list_of_random_integers

def get_list_of_random_integers(length:int, size:int):
    min_int=pow(10,length-1)
    max_int=pow(10,length)-1
    return nprand.random_integers(low=min_int,high=max_int,size=size)

def get_random_integer(length:int):
    min_int=pow(10,length-1)
    max_int=pow(10,length)-1
    return random.randint(min_int,max_int)
    
