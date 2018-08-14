#Insertion Sort by Using For loops
#Time complexity of an imput of size "n"= O(n**2)
from random import randint
from time import time

def insertion(l):
    """
    Input: a randomly generated list 
    Output: sorted imput 
    """
    for i in range(len(l)):
        k=i
        for j in range(i):
            if l[k-1]>l[k]:
                a=l[k-1]
                l[k-1]=l[k]
                l[k]=a
                k-=1
    return l

size=2**12
l= [randint(-100,100) for i in xrange(size)]
#print l
t1 = time()
l2=insertion(l)
t2=time()-t1
print "Elapsed Time:",t2
