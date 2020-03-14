L = [2,4,9,7,5,1,6,3,8]

def triInsertion2(L):
	n = len(L)
	if n < 2:
		return L
	for k in range(1,n):
		x = L[k]
		i = k
		while i>0 and x<L[i-1]:
			L[i] = L[i-1]
			i -= 1
		L[i] = x
	return L

T = triInsertion2(L)
print(T)


def triInsertion(L):
	n = len(L)
	for k in range(1,n):
		x = L[k]
		i = k
		while i>0 and x<L[i-1]:
			L[i] = L[i-1]
			i -= 1
		L[i] = x



import random 
L = [random.randint(0, 10) for i in range(10)]

triInsertion(L)
print(L)


import timeit
start = timeit.default_timer()
stop = timeit.default_timer()


def printComplexite(nmax):
	X = []
	Y = []
	for i in range(10,nmax,50):
		L = [random.randint(0,100) for k in range(i)]
		X.append(i)
		start = timeit.default_timer()
		triInsertion(L)
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


