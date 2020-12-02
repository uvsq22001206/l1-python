# 2
carre_mag = [
    [4, 14, 15, 1],
    [9, 7, 6, 12],
    [5, 11, 10, 8],
    [16, 2, 3, 13]
    ]
print(carre_mag)

# 3
carre_pas_mag = [list(lis) for lis in carre_mag]
carre_pas_mag[1][1] = 3
print(carre_pas_mag)


# 4
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for lis in carre:
        print(lis)


afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)


# 5
def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    if sum(carre[0]) == sum(carre[1]) and sum(carre[1]) == sum(carre[2]) and sum(carre[2]) == sum(carre[3]):
        return sum(carre[0])
    else:
        return -1


print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))


# 6
def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    L0 = sum(carre[0][i] for i in range(4))
    L1 = sum(carre[1][i] for i in range(4))
    L2 = sum(carre[2][i] for i in range(4))
    L3 = sum(carre[3][i] for i in range(4))
    if L0 == L1 and L1 == L2 and L2 == L3:
        return L0
    else:
        return -1


print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))


# 7
def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    for i in range(3, -1, -1):
        L0 = sum(carre[i][j] for j in range(4))
    L1 = sum(carre[i][i] for i in range(4))
    if L0 == L1:
        return L0
    else:
        return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))


# 8
def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    if testLignesEgales(carre) == -1 and testColonnesEgales(carre) == -1 and testDiagonalesEgales(carre) == -1:
        return False
    else:
        return True


print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))
