# Exercice
def tri(lis):
    l_triee = []
    for i in range(len(lis)):
        minimum = min(lis)
        l_triee.append(minimum)
        lis.remove(minimum)
    return l_triee


tri([4, 13, 42, 27, 31, 17, 21])

# Out[]: [4, 13, 17, 21, 27, 31, 42]


# Exercice
def compter_negatives(nombres):
    """Renvoie le nombre d'éléments <0 de la liste passée en paramètre"""
    compte = 0
    for elem in nombres:
        if(elem < 0):
            compte += 1
    return compte


compter_negatives([3, -1, 1.5, 5, -6.3, -7.9, 2])
# Out : 3
