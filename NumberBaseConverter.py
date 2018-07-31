#Maximum possible base is 62
def m2n(a,m=[2,10]):
	a=str(a)
	sign = lambda a2=a:'-' if a2[0]=="-" else ''
	sign = sign(a)
	a = a[1:]*(sign=='-') + a*(sign=="")
	
	# this function convertes the number "a" from base m[0] to m[1]
	s="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!"
	D = {l:s[l] for l in xrange(len(s))}
	for l in xrange(len(s)):
		D[s[l]] = l	
	for element in a:
		if D['!'] < max(m[0],m[1]):
			print 'error: the base is too high'
			return 'error: base exceeded its maximum value'
		if D[element] >= m[0]:
			print 'error: the base is too low'
			return "error: base-to-number compatibility"

			
	#print D['Z']
	def m2ten(a2=str(a),n=m[0],i=0):
		if i == len(str(a))-1:
			return D[a2[i]]
		else:
			#print a2[i]
			#print 10**D[a2[i]]
			return (n**(len(a2)-1-i))*D[a2[i]]+ m2ten(a2,n,i+1)
	def powd(b,n,k=0):
		if b//(n**k)==0:
			return k-1
		else:
			return powd(b,n,k+1)
	def ten2m(a2=m2ten(),n=m[1],j=powd(m2ten(a,m[0]),m[1])):
		if j==0:
			return D[a2]
		else:
	    	#return D[ten2m(a2%(n**j),n,j-1)]+ D[(a2//(n**j))*(10**j)]
			return  D[(a2//(n**j))] + ten2m(a2%(n**j),n,j-1)		
	return sign+ten2m()
		
print m2n("HesamEskandari",[63,60])




