import random 
n = 40
m = n**2 -1
L = [random.randint(0, m) for i in range(n)]




def triComptage(L):
	n = len(L)
	m = max(L)+1
	count = [0]*m
	sort = []
	for i in range(n):
		count[L[i]] += 1
	for i in range(m):
		for j in range(count[i]):
			sort.append(i)
	return(sort)


c = 0
for _ in range(100):
	c += max([random.randint(0, m) for i in range(n)])
print(c/100)



T = triComptage(L)
print(L)
print(T)


import timeit
start = timeit.default_timer()
stop = timeit.default_timer()


def printComplexite(nmax):
	X = []
	Y = []
	for i in range(10,nmax,50):
		L = [random.randint(0,i**2-1) for k in range(i)]
		X.append(i)
		start = timeit.default_timer()
		triComptage(L)
		stop = timeit.default_timer()
		Y.append(stop-start)
	return([X,Y])






N = 1000
P = printComplexite(N)

import numpy as np
Z = np.polyfit(P[0], P[1], 2)
t = np.arange(0., N, 1)



import matplotlib.pyplot as plt
plt.plot([P[0]],[P[1]], 'ko')
plt.plot(t, Z[0]*t**2 + Z[1]*t + Z[2], 'r--')
#plt.plot(L[Enveloppe[0]][0],L[Enveloppe[0]][1], 'bo')
#plt.plot(P[0],P[1], 'ro')
#plt.plot([L[i][0] for i in Enveloppe],[L[i][1] for i in Enveloppe ], 'r-')
plt.show()

