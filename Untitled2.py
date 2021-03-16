#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=(int(input('n=')))
for i in range(n):
    for j in range(i):
        print('#',end="")
    print('')
for i in range(n,0,-1):
    for i in range(i):
     print('#',end="")
    print('')

