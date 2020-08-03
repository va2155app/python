#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gg(a):
    n=1
    arr=list()
    while n<a:
        i=1
        x=0
        while i<=n:
            if n%i==0 :
                x+=1
                i+=1
            else:
                i+=1
        if x<=2:
            arr.append(n)    
        n+=2
    return arr
print("{}是質數".format(gg(10000)))
            


# In[ ]:




