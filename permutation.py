def perm(l):
    if len(l) == 1:
        return [l]
    else:
        return [[pivot] + rest for i, pivot in enumerate(l) for rest in perm(l[:i] + l[i+1:])]
# In[3]: %timeit perm(range(3))
# 10000 loops, best of 3: 25.7 micro s per loop
# In[4]: %timeit perm(range(5))
# 1000 loops, best of 3: 810 micro s per loop
# In[5]: %timeit perm(range(10))
# 1 loops, best of 3: 39.6 s per loop


def perm_insert(l):
    if len(l) == 1:
        return [l]
    else:
        return [rest[:j] + [l[0]] + rest[j:] for rest in perm_insert(l[1:]) for j in xrange(len(l))]
# In[16]: %timeit perm_insert(range(3))
# 10000 loops, best of 3: 21.6 micro s per loop
# In[17]: %timeit perm_insert(range(5))
# 1000 loops, best of 3: 312 micro s per loop
# In[18]: %timeit perm_insert(range(10))
# 1 loops, best of 3: 9.97 s per loop

print perm_insert(list("pie"))
print perm_insert(range(3))