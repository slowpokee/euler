import math
def div(n):
	total = 0
	for i in range(1,n):
		if(n%i==0):
			total = total + i
	return total

total = []
for i in range(1,10001):
	a = div(i)
	if(div(a) == i and a != i):
		total.append(a)
		total.append(i)
total = list(set(total))
print total
print sum(total)
