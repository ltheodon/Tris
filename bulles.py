import random 
n = 10
L = [random.randint(0, 10) for i in range(n)]
T = L.copy()

def triBulles(L):
	n = len(L)
	for i in range(n,1,-1):
		for j in range(i-1):
			if L[j+1] < L[j]:
				L[j+1], L[j] = L[j], L[j+1]


print(L)
triBulles(L)
print(L)

def triBullesOpti(L):
	n = len(L)
	for i in range(n,1,-1):
		stop = True
		for j in range(i-1):
			if L[j+1] < L[j]:
				stop = False
				L[j+1], L[j] = L[j], L[j+1]
		if stop:
			return None


triBullesOpti(T)
print(T)