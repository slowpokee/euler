f = open('tri.txt','r')
l = f.read().split('\n')
del l[-1]
li = []
for i in l:
	li.append(map(int, i.split(' ')))
a = []

for i in range(len(li)-1,-1,-1):
	if(i != len(li)-1):
		for k in range(0,len(li[i])):
			li[i][k] = li[i][k] + max(li[i+1][k],li[i+1][k+1])
	#for j in range(0,len(li[i])-1,2):
		#li[i][j] = max(li[i][j],li[i][j+1])
print li[0]
