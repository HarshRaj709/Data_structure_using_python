#import numpy as np
from numpy import *

#1d array
a = array([1,2,3,45,75])         # here we cant add 'a'
print(a)

#2d Array
b = array([[1,4,58,56,2,6],[85,696,54,232,78,12]])  #must be both blocks are of same length
print(b)

#1d array with two list type element
c = array([[1,2,3],[3,4]], dtype=object)        #[list([1, 2, 3]) list([3, 4])]
print(c)