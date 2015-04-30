def a(n):
	return n if n == 1 else a(n-1) * n

def c(n,r):
	return a(n)/(a(r)*a(n-r))

m = 0
for i in range(1,101):
	for j in range(1,i):
		if(c(i,j) > 1000000):
			m = m + 1
print m
