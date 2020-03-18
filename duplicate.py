import random 
n = 10
L = [i for i in range(1,n+1)]
L.append(random.randint(1, n))
random.shuffle(L)

# La lsite L contient au moins un doublon (entiers entre 1 et n, n+1 éléments)


def findDuplicate(L):
	tortue = L[0]
	lievre = L[0]
	while True:
		tortue = L[tortue]
		lievre = L[L[lievre]]
		if tortue == lievre:
			break

	pointeur1 = L[0]
	pointeur2 = tortue
	while pointeur1 != pointeur2:
		pointeur1 = L[pointeur1]
		pointeur2 = L[pointeur2]
	return pointeur1

print(L)
print(findDuplicate(L))

