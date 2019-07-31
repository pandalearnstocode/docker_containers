import numpy as np
def base_RG(n):
    np.random.rand(n)
    pass
def base_rand_int_1d(min_value,max_value,sample_size):
    np.random.randint(min_value,max_value,size=sample_size)
    pass
def base_rand_int_2d(min_value,max_value,sample_size):
    np.random.randint(min_value,max_value,size=(sample_size,sample_size))
    pass