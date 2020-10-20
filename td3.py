# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné\n
    comme jour, heure, minute, seconde."""
    jts = temps[0] * 86400
    hts = temps[1] * 3600
    mts = temps[2] * 60
    return jts + hts + mts + temps[3]


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui\n
    correspond au nombre de seconde passé en argument"""
    stj = seconde // 86400
    sth = seconde // 3600 % 24
    stm = seconde // 60 % 60
    return stj, sth, stm, seconde % 60


temps = secondeEnTemps(100000)
x = str(temps[0]) + " jours " + str(temps[1])
print(x, "heures", temps[2], "minutes", temps[3], "secondes")
