
# coding: utf-8

# In[2]:


#Recursive Merge Sort
# You may get this error if the input list has a size bigger than 963 elements:
# RuntimeError: maximum recursion depth exceeded in cmp

from time import time
from random import random

def merge(m1,m2,m=[]):
    if len(m1)==0 or len(m2)==0:
        m.extend(m1)
        m.extend(m2)
        del m1
        del m2
        return m
        
    else:
        if m1[0] == min(m1[0],m2[0]): 
            m.append(m1[0])
            del(m1[0])
        else: 
            m.append(m2[0])
            del(m2[0])
        return merge(m1,m2,m)

def marg(l2,l3=[],i=0):
    if len(l2)==0:
        return l3
    elif len(l2)==1:
        if len(l3)==0:
            l3=l2
        else:
            #print l3
            l4=merge(l2[0],l3[-1],[])
            #print l4
            l3[-1]=l4
        return l3
    else:
        l4=merge(l2[0],l2[1],[])
        l3.append(list(l4))
        l4=[]
        del(l2[0])
        del(l2[0])
        return marg(l2,l3,i+1)
        
def mergesort(l,i=0):
    if i==0:
        l2=list(l)
        def zahr(l2,l3=[]):
            if len(l2)==0:
                return l3
            else:
                l3.append([l2[0]])
                del(l2[0])
                return zahr(l2,l3)
        l=zahr(l2)
    if len(l)==1:
        return l[0]
    else:
        l=marg(l,[])
        return mergesort(l,i+1)

#r=mergesort([3,2,0,18,-1,12,0,-18])
#print r
l=[100*random()-50 for i in xrange(963)]
t1=time()
r=mergesort(l)
t2=time()-t1
print "Elapsed Time:",t2

