# 2
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste.append(n)
    return liste


print(syracuse(3))


# 3
def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(2, n_max):
        syracuse(i)
    return "Conjecture vérifiée"


print(testeConjecture(10000))


# 4
def tempsVol(n):
    """ Retourne le temps de vol de n """
    lis = syracuse(n)
    return len(lis)


print("Le temps de vol de", 3, "est", tempsVol(3))


# 5
def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    lis = []
    for i in range(1, n_max):
        lis.append(tempsVol(i))
    return lis


print(tempsVolListe(100))


# 6
l1 = tempsVolListe(10000)
maxi = max(l1)
i = l1.index(maxi)
print(i + 1)


# 7
def altitudeMaxListe(n_max):
    lis = []
    for i in range(1, n_max):
        lis.append(max(syracuse(i)))
    return lis


# def altitude(n):
    # maxalt = [max(syracuse(i)) for i in range(1, n)]
    # Maxi1 = max(maxalt)
    # b = maxalt.index(Maxi1)
    # print(b + 1)


l2 = altitudeMaxListe(10000)
maxi_2 = max(l2)
i_2 = l2.index(maxi_2)
print(i_2 + 1)
print(max(syracuse(i_2 + 1)))
