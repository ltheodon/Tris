L = [2,4,9,7,5,1,6,3,8]

def Fusion_rec(L1,L2):
	if not L1:
		return L2
	if not L2:
		return L1
	if(L1[0]<L2[0]):
		return [L1[0]] + Fusion_rec(L1[1:],L2)
	else:
		return [L2[0]] + Fusion_rec(L1,L2[1:])

def Fusion(L1,L2):
	if not L1:
		return L2
	if not L2:
		return L1
	n1, n2 = len(L1), len(L2)
	i1, i2 = 0, 0
	L = []
	while i1<n1 and i2<n2:
		if(L1[i1]<L2[i2]):
			L.append(L1[i1])
			i1 += 1
		else:
			L.append(L2[i2])
			i2 += 1
	return L + L1[i1:] + L2[i2:]


def triFusion(L):
	n = len(L)
	if n < 2:
		return L
	m = n//2
	return Fusion(triFusion(L[:m]),triFusion(L[m:]))


T = triFusion(L)
print(T)


import random 
L = [random.randint(0, 10) for i in range(10)]

def validation(L):
	if not L:
		return True
	for i in range(len(L)-1):
		if L[i+1] < L[i]:
			return False
	return True

T = triFusion(L)
print(validation(L))
print(validation(T))
print(T)

def validation_rec(L):
	n = len(L)
	if n < 2:
		return True
	if L[0] <= L[1]:
		return validation_rec(L[1:])
	else:
		return False


L = [random.randint(0, 10) for i in range(10)]
T = triFusion(L)
print(validation_rec(L))
print(validation_rec(T))
print(T)