#Counting sort algorithm
#Restriction: The input must be a list of positive integers

from random import randint
from time import time
def counting_sort(A):
    """
    Input: a random list of positive integers
    Output: sorted by counting sort
    """
    c=[0 for i in xrange(max(A))]
    for i in xrange(len(A)):
        c[A[i]-1]+=1
    d=list(c)
    for i in xrange(len(c)-1):
        d[i+1]=c[i+1]+d[i]
    B=list(A)
    i=len(A)-1
    while i>=0:
        B[d[A[i]-1]-1]=A[i]
        d[A[i]-1]-=1
        i-=1
    return B
        
t0=time()
size=2**20
l=[randint(1,10000) for i in xrange(size)]
t1=time()
print 'Time to make a random list of size',size,':',t1-t0,'sec'
l1=counting_sort(l)
t2=time()
print 'counting sort:',t2-t1,'sec'
l2=sorted(l)
t3=time()
print 'built in sorted algorithm:',t3-t2,'sec'
print 'if the results are the same:',l1==l2
    
