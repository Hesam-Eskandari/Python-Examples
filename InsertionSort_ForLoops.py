
# coding: utf-8

# In[1]:


#Insertion Sort by Using For loops
from random import random
from time import time
l=[100*random()-50 for i in xrange(2**11)]
def insertion(l):
    for i in range(len(l)):
        k=i
        for j in range(i):
            if l[k-1]>l[k]:
                a=l[k-1]
                l[k-1]=l[k]
                l[k]=a
                k-=1
    return l

#l= [3,2,1,7,6,4,-1,0,15,-12,18]
#print l
t1 = time()
l2=insertion(l)
t2=time()-t1
print "Elapsed Time:",t2

