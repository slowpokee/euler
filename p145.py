import time

a = []
total = 0
result = 0
test = 0
flag = 1
start_time = time.time()
for i in range(1,10000000):
	a = map(int, str(i))
	if a[-1] != 0:
		temp = len(a) / 2
		for j in range(0,temp):
			if (a[j] + a[0-j-1]) % 2 == 1 and flag == 1:
				flag = 1
			else:
				flag = 0
		if flag == 1:
			b = a[::-1]
			c = map(int, b)
			d = int(''.join(str(i) for i in c))
			e = map(int, str(i + d))
			if all(i % 2 == 1 for i in e):
				#if(a[0] == 3 and len(a) == 6):
				#	test = test + 1
				#print i, d, e
				result = result + 1
				#result.append(e)
		flag = 1
end_time = time.time() - start_time
print test
print result, "in", end_time
