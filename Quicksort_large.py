#Quicksort for large size lists
#Note: Self-assignment should be done first in muliple-assignments (lines 19 and 20)
from random import randint
from time import time

def quick_sort(l):
    """
    Input: random list of integers
    Output: sorted input
    """
    if len(l)==1 or len(l)==0:
        return l
    else:
        #p=len(l)/2
        p=randint(0,len(l)-1)
        i=0
        while i < len(l):
            if l[i]<l[p] and i>p:
                l[i],l[p],l[p+1]=l[p+1],l[i],l[p]
                #l[p+1],l[i],l[p]=l[p],l[p+1],l[i]
                p=p+1
            elif l[i]>l[p] and i<p:
                l[i],l[p],l[p-1]=l[p-1],l[i],l[p]
                p=p-1
            else:
                i+=1
        #return l,p
        l[:p]=quick_sort(l[:p])
        l[p:]=quick_sort(l[p:])
        return l
    
t0=time()
size=2**18
l= [randint(-50,50) for i in xrange(size)]
#print l
t1=time()
r=quick_sort(list(l))
t2=time()
#print r
r2=sorted(l)
t3=time()

print 'time to generate random list of size',size,':',t1-t0,'sec'
print 'quick sort:',t2-t1,'sec'
print 'built in "sorted()":',t3-t2,'sec'
print 'if the results are the same:',r==r2