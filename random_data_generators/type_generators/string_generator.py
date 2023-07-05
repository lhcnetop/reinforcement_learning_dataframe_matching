import string
import random


def get_list_of_random_strings(length:int,size:int,chars=string.digits):
    list_of_random_strings=[]
    for i in range(size):
        random_string=''.join(random.choices(chars,k=length))
        list_of_random_strings.append(random_string)
    return list_of_random_strings

def get_random_string(length:int,chars=string.digits):
    return ''.join(random.choices(chars,k=length))