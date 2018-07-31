#Fibonatcii  
l=[0]
def fibo(n,i=0,j=1,k=0):
	"""
	Input: request for n first elements of Fibonatcci 
	Output: n first elements of Fibonatcci
	"""
	if k==n-1:
		return l
	else:
		l.append(j)
		return fibo(n,j,i+j,k+1)
		
print fibo(7)
