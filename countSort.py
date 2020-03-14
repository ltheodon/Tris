import numpy as np
def countSort(L):
	n = len(L)
	m = np.max(L)+1
	histo = [0]*m
	for i in range(n):
		histo[L[i]] += 1
	T = []
	for i in range(m):
		for j in range(histo[i]):
			T.append(i)
	return T

import random as rand
L = [rand.randint(0,20) for i in range(10)]
T = countSort(L)
print(L)
print(T)


def longueur(L):
    if L == []:
        return 0
    return 1 + longueur(L[1:])

print(longueur(L))



def countSortZ(L):
	m = np.min(L)
	fL = [n-m for n in L]
	return [n+m for n in countSort(fL)]

L = [rand.randint(-10,10) for i in range(10)]
T = countSortZ(L)
print(L)
print(T)