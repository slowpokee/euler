total = []
for i in range(2,101):
	for j in range(2,101):
		total.append(i**j)
total = list(set(total))
print len(total)
