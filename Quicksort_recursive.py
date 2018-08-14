#Recursive Quicksort
#Note: Self-assignment should be done first in muliple-assignments (see the comented line (lines 20 and 21))
#Restriction: "RuntimeError" could happen if the input size is more than 2**9
from time import time
from random import randint

def qs(l,p,i=0):
    """
    Input: a list and a pivot
    Output: rearranged input: [k<=p|p|k>=p] 
    """
    if len(l)==i:
        return l,p
    else:
        if l[i]>l[p] and i<p:
            l[i],l[p],l[p-1]=l[p-1],l[i],l[p]
            p-=1
            i-=1
        elif l[i]<l[p] and i>p:
            l[i],l[p],l[p+1]=l[p+1],l[i],l[p]
            #l[p+1],l[i],l[p]=l[p],l[p+1],l[i]
            p+=1
            i-=1
        return qs(l,p,i+1)

def quicksort(l):
    """
    Input: random list of integers
    Output: sorted input
    """
    if len(l)==1 or len(l)==0:
        return l
    else:
        #p=randint(0,len(l)-1)
        p=len(l)/2
        l,p=qs(l,p)
        l[:p]=quicksort(l[:p])
        l[p:]=quicksort(l[p:])
        return l  
t0=time()
size=2**9
l=[randint(-500,500) for i in xrange(size)]
t1=time()
r1=quicksort(list(l))
t2=time()
print t2-t1
r2=sorted(l)
t3=time()

print 'time to generate random list of size',size,':',t1-t0,'sec'
print 'quick sort:',t2-t1,'sec'
print 'built in "sorted()":',t3-t2,'sec'
print 'if the results are the same:',r1==r2
