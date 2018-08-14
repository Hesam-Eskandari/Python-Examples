#Recursive Insertion Sort
# You may get "RuntimeError" error if the input list has a size bigger than 487 elements.

from random import randint
from time import time

def insertion(l,i=1):
    """
    Input: the input list "l"
    Output: sorted "l"
    """
    if i==len(l)+1:
        return l
    else:
        inner_insertion(l,i)
        return insertion(l,i+1)
    
def inner_insertion(l,i,j=0):
    """
    Input: list "l" and element "i"
    Output: put "i" in a proper (sorted) position in "l"
    """
    if j==i-1:
        return l
    else:
        k=i-j-1
        if l[k-1]>l[k]:
            a=l[k-1]
            l[k-1]=l[k]
            l[k]=a
        return inner_insertion(l,i,j+1)
    
l=[randint(-50,50) for i in xrange(487)]
#print l,"\n"
t1=time()
l2=insertion(l)
t2=time()-t1
print "Elapsed Time:",t2
