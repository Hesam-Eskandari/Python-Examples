
# coding: utf-8

# In[5]:


#Merge Sort by Using For loops

from time import time
from random import random

def merge(m1,m2):
    m=[]
    while len(m1)!=0 and len(m2)!=0:
        if m1[0]==min(m1[0],m2[0]):
            m.append(m1[0])
            del(m1[0])
        else:
            m.append(m2[0])
            del(m2[0])
    if len(m1)!=0:
        m.extend(m1)
    else:
        m.extend(m2)
    return m

def marg(l):
    if len(l)==1:
        return l
    else:
        m=[]
        while len(l)>1:
            m.append(merge(l[0],l[1]))
            del(l[0])
            del(l[0])
        if len(l)==1:
            m[-1]=merge(m[-1],l[0])
        return m

def mergesort(l):
    l2=[[l[i]] for i in xrange(len(l))]
    while len(l2)>1:
        l2=marg(l2)
    return l2[0]

#print mergesort([3,1,2,0])
            
l=[100*random()-50 for i in xrange(2**15)]
t1=time()
r=mergesort(l)
t2=time()-t1
print "Elapsed Time:",t2           
            
            

