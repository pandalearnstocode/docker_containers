import numpy as np
from numpy import random, random_intel


def intel_RG(n):
    np.random_intel.rand(n)
    pass


def intel_rand_int_1d(min_value, max_value, sample_size):
    np.random_intel.randint(min_value, max_value, size=sample_size)
    pass


def intel_rand_int_2d(min_value, max_value, sample_size):
    np.random_intel.randint(min_value, max_value, size=(sample_size, sample_size))
    pass
# import numpy as np
# np.random.uniform([0,1],[2,3],size=(30000,2))
# np.random.uniform([0,1],[2,3],size=(30000,2))


# import numpy as np
# from numpy import random, random_intel
# np.array([0,1]) + ((np.array([2,3]) - np.array([0,1])) * np.random_intel.uniform(size=(30000,2)))
# np.array([0,1]) + ((np.array([2,3]) - np.array([0,1])) * np.random_intel.uniform(size=(30000,2)))
