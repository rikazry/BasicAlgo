import numpy as np


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
# In[15]: %timeit fibonacci(5)
# 100000 loops, best of 3: 15.4 micro s per loop
# In[16]: %timeit fibonacci(10)
# 1000 loops, best of 3: 197 micro s per loop
# In[17]: %timeit fibonacci(20)
# 10 loops, best of 3: 21.6 ms per loop


def fibonacci_tail(n, last=1, previous=0):
    if n == 0:
        return previous
    elif n == 1:
        return last
    elif n == 2:
        return last + previous
    return fibonacci_tail(n-1, last + previous, last)
# In[18]: %timeit fibonacci_tail(5)
# 100000 loops, best of 3: 5.97 micro s per loop
# In[19]: %timeit fibonacci_tail(10)
# 10000 loops, best of 3: 12.7 micro s per loop
# In[20]: %timeit fibonacci_tail(20)
# 10000 loops, best of 3: 33.7 micro s per loop
# In[33]: %timeit fibonacci_tail(500)
# 1000 loops, best of 3: 347 micro s per loop


def fibonacci_matrix(n):
    initial_vec = np.matrix([1, 0])
    trans_mat = np.matrix([[1, 1], [1, 0]])
    if n == 0:
        return initial_vec[1]
    return (trans_mat ** (n-1) * initial_vec.T).item(0, 0)
# In[24]: %timeit fibonacci_matrix(5)
# 10000 loops, best of 3: 117 micro s per loop
# In[25]: %timeit fibonacci_matrix(10)
# 10000 loops, best of 3: 130 micro s per loop
# In[26]: %timeit fibonacci_matrix(20)
# 10000 loops, best of 3: 138 micro s per loop
# In[34]: %timeit fibonacci_matrix(500)
# 1000 loops, best of 3: 202 micro s per loop
