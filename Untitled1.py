#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=input("потери=")
x=int(x)
y=input("прибыль=")
y=int(y)
if x>y:
    res=x-y
    print("Ваши убытки составляют=",res)
elif x<y:
    res=x+y
    print("Ваша прибыль составляет=",res)

