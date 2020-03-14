import random 
n = 50000
N = 20
L = [random.randint(0, 100) for i in range(n)]

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


def triFusionN(L,N):
	n = len(L)
	if n < N:
		triInsertion(L)
		return L
	m = n//2
	return Fusion(triFusionN(L[:m],N),triFusionN(L[m:],N))

def triInsertion(L):
	n = len(L)
	for k in range(1,n):
		x = L[k]
		i = k
		while i>0 and x<L[i-1]:
			L[i] = L[i-1]
			i -= 1
		L[i] = x



def triMelange(L,N):
	return triFusionN(L,N)






import timeit
start = timeit.default_timer()
T = triMelange(L,N)
#print(L)
#print(T)
stop = timeit.default_timer()

print('Time: ', stop - start)  

x = stop - start








# Cas du tri fusion simple
def triFusion(L):
	n = len(L)
	if n < 2:
		return L
	m = n//2
	return Fusion(triFusion(L[:m]),triFusion(L[m:]))



L = [random.randint(0, 100) for i in range(n)]
import timeit
start = timeit.default_timer()
T = triFusion(L)
stop = timeit.default_timer()

print('Time: ', stop - start)  

print((stop - start-x)/x*100)