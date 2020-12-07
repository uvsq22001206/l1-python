# Chiffrement de César
# Décalage cyclique de l'alphabet avec une clé
# exemple : décalage de 4 : ABCDEFGHIJKLMNOPQRSTUVWXYZ -->
# EFGHIJKLMNOPQRSTUVWXYZABCD
# MESSAGE chiffré(décalage de 5) : RJXXFLJ
# 26 décalages possibles --> 26 clés possibles
# chiffrer = quand on a la clé secrète. Texte clair -> Texte chiffré
# Déchiffrer = quand on a la clé secrète. Texte chiffré -> Texte clair
# Décrypter = quand on n'a PAS la clé secrète. Texte chiffré -> Texte clair
# Objectif : chiffrer et déchiffrer avec le code de césar un message

# chiffre et déchiffre avec une clé k(entier pris entre 0 et 25)


def chiffreCesar(clef, clair):
    # ici on suppose que clair ne
    # contient que des A - Z
    """ Clef est un entier compris entre 0 et 25,
    clair est une chaine de caractère. Fonction qui va
    chiffrer une chaine de caractère choisi """
    chiffre = ""
    for c in clair:
        # c est pour "caractère"
        # utilisation du code ASCII
        tmp = ord(c) + clef
        if (tmp > 90):
            tmp = ord(c) - 26 + clef
        chiffre = chiffre + chr(tmp)
    return chiffre


def dechiffreCesar(clef, chiffre):
    """ chiffre est une chaine de caractère"""
    clair = ""
    chiffre1 = str(chiffre)
    for c in chiffre1:
        tmp = ord(c) - clef
        if (tmp < 65):
            tmp = ord(c) + 26 - clef
        clair += chr(tmp)
    return clair


ch = "MESSAGE"
s = print(chiffreCesar(5, ch))
print(dechiffreCesar(5, "RJXXFLJ"))
