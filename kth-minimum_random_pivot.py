# Kth minimum number of an array (list) with random pivot 
from random import randint
from time import time
def q_pivot(l):

    p = randint(0,len(l)-1)
    i=0
    while i<len(l):
        if l[i]<l[p] and i > p:
            l[i],l[p],l[p+1]=l[p+1],l[i],l[p]
            p+=1
        elif l[i]>l[p] and i<p:
            l[i],l[p],l[p-1]=l[p-1],l[i],l[p]
            p-=1
        else:
            i+=1
    return l,p

def kth_min(l,k):
    if k > len(l):
        return 'error: k cannot be larger than length(l)'
    
    l,p=q_pivot(l)
    #print l,p
    if p+1 == k:
        return l[p]
    elif p+1 < k:
        return kth_min(l[p+1:],k-p-1)
    elif p+1 > k:
        return kth_min(l[:p],k)
t0=time()
l = [randint(0,1000) for i in xrange(2**20)]
k = randint(1,len(l))
t1=time()
kth = kth_min(l,k)
t2 = time()
print 'Validate the answer:',kth_min(l,k) == sorted(l)[k-1]
print 'Time to generate a random list:',t1-t0
print 'Time to find the kth minimum:',t2-t1

