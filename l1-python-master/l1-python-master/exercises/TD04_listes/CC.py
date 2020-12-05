# CC du 5 décembre 2020


# 1
def carre(liste):
    for i in range(len(liste)):
        liste[i] = liste[i] ** 2
    print(liste)


carre([1, 3, 5])

# 2
lis = []
for i in range(101):
    if i % 2 == 0:
        lis.append(i)
lis.extend([i for i in range(99, 0, -1)])
print(lis)


# 3
def somme(liste1, liste2):
    somme = sum(liste1) + sum(liste2)
    print(somme)


somme([1, 2, 3], [1, 2])


# 4
def carre_croissant(n):
    lis = []
    liste = []
    for j in range(1, n+1):
        for i in range(j, n+j):
            lis.append(i)
    liste.extend(lis)
    print(liste)


carre_croissant(5)

# 10
liste = [2] * 3 + [-1] * 2
liste.append(0)
liste.remove(-1)
liste.sort()
print(liste)
