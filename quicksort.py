def partition(a,L):
	if not L:
		return [[],[]]
	L1, L2 = [], []
	while L:
		if a >= L[0]:
			L1.append(L.pop(0))
		else:
			L2.append(L.pop(0))
	return [L1,L2]


def quicksort(L):
	n = len(L)
	if n < 2:
		return L
	a = L.pop(0)
	part = partition(a,L)
	L1 = quicksort(part[0])
	L2 = quicksort(part[1])
	return L1 + [a] + L2

import random 
n = 10
L = [random.randint(0, 10) for i in range(n)]

print(L)
T = quicksort(L)
print(L)
print(T)