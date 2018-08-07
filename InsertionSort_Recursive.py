
# coding: utf-8

# In[4]:


#Recursive Insertion Sort
# You may get this error if the input list has a size bigger than 487 elements:
# RuntimeError: maximum recursion depth exceeded in cmp
from random import random
from time import time
l=[100*random()-50 for i in xrange(487)]
def insertion(l,i=1):
    if i==len(l)+1:
        return l
    else:
        inner_insertion(l,i)
        return insertion(l,i+1)
    
def inner_insertion(l,i,j=0):
    if j==i-1:
        return l
    else:
        k=i-j-1
        if l[k-1]>l[k]:
            a=l[k-1]
            l[k-1]=l[k]
            l[k]=a
        return inner_insertion(l,i,j+1)
#l= [3,2,1,7,6,4,-1,0,15,-12]
#print l,"\n"
t1=time()
l2=insertion(l)
t2=time()-t1
print "Elapsed Time:",t2

