# temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jts = temps[0] * 86400
    hts = temps[1] * 3600
    mts = temps[2] * 60
    return jts + hts + mts + temps[3]


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    stj = seconde // 86400
    sth = seconde // 3600 % 24
    stm = seconde // 60 % 60
    return stj, sth, stm, seconde % 60


def exo1():
    temps = (3, 23, 1, 34)
    print(type(temps))
    print(tempsEnSeconde(temps))
    temps = secondeEnTemps(100000)
    print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")


def strJour(temps):
    if temps[0] == 0:
        return ""
    elif temps[0] == 1:
        return "un jour"
    else:
        return str(temps[0]) + " jours"


def strHeure(temps):
    if temps[1] == 0:
        return ""
    elif temps[1] == 1:
        return " une heure"
    else:
        return " " + str(temps[1]) + " heures"


def strMinute(temps):
    if temps[2] == 0:
        return ""
    elif temps[2] == 1:
        return " une minute"
    else:
        return " " + str(temps[2]) + " minutes"


def strSeconde(temps):
    if temps[3] == 0:
        return ""
    elif temps[3] == 1:
        return " une seconde"
    else:
        return " " + str(temps[3]) + " secondes"


def afficheTemps(temps):
    print(strJour(temps) + strHeure(temps) + strMinute(temps) + strSeconde(temps))


def exo2():
    afficheTemps((1, 0, 14, 23))


def demandeTemps():
    day = int(input("Days :"))
    hour = int(input("Hours :"))
    minute = int(input("Minutes :"))
    second = int(input("Secondes :"))

    while(day < 0):
        day = int(input("Invalid number of days, give a new number :"))

    while(hour < 0 or hour >= 24):
        hour = int(input("Invalid number of hours, give a new number :"))

    while(minute < 0 or minute >= 60):
        minute = int(input("Invalid number of minutes, give a new number :"))

    while(second < 0 or second >= 60):
        second = int(input("Invalid number of seconds, give a new number :"))
    return (day, hour, minute, second)


def exo3():
    afficheTemps(demandeTemps())


def sommeTemps(temps1, temps2):
    res = [0, 0, 0, 0]
    for i in range(0, 4):
        res[i] = temps1[i] + temps2[i]

    if(res[3] >= 60):
        res[2] += res[3] // 60
        res[3] %= 60
    if(res[2] >= 60):
        res[1] += res[2] // 60
        res[2] %= 60
    if(res[1] >= 24):
        res[0] += res[1] // 24
        res[1] %= 24
    return res


def exo4():
    afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))


def proportionTemps(temps, proportion):
    second = tempsEnSeconde(temps)
    second = second * proportion / 100
    return secondeEnTemps(second)


def exo5():
    afficheTemps(proportionTemps((2, 0, 36, 0), 0.2))


def tempsEnDate(temps):
    return (1970 + temps[0] // 360,
            temps[0] % 360 // 30,
            temps[0] % 30,
            temps[1],
            temps[2],
            temps[3])


def afficheDate(date=-1):
    if date == -1:
        pass
        return

    def strMonth(date):
        if date[1] == 0:
            return ""
        elif date[1] == 1:
            return ", un mois"
        else:
            return ", " + str(date[1]) + " mois"

    def strYear(date):
        return "année " + str(date[0])

    print(strYear(date) + strMonth(date))
    afficheTemps((date[2], date[3], date[4], date[5]))


def exo6():
    temps = secondeEnTemps(1000000000)
    afficheTemps(temps)
    afficheDate(tempsEnDate(temps))
    afficheDate()


def exo7():
    import time
    afficheDate(time.gmtime())


def bisextile(jour):
    second = jour * 86400
    annee = tempsEnDate(secondeEnTemps(second))[0]
    print("De 2020 à", str(annee) + ", les années :")

    for i in range(2020, annee, 4):
        if(annee % 400 != 0):
            print(i)
    print("sont bisextile")


def exo8():
    bisextile(20000)


def nombreBisextile(jour):
    pass

def tempsEnDateBisextile(temps):
    pass


def exo9(): 
    temps = secondeEnTemps(1000000000)
    afficheTemps(temps)
    afficheDate(tempsEnDateBisextile(temps))


exo1()
exo2()
exo3()
exo4()
exo5()
exo6()
exo7()
exo8()
