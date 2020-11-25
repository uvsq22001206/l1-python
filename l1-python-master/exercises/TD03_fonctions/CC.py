global var_glob
var_glob = 26


def difference(var_loc):
    return var_glob - var_loc


difference(9)


def troisieme_fonction(pays, continent="Europe", ville="Paris"):
    print(ville, ",", pays, ".", continent)


troisieme_fonction(ville="Londres", pays="Angleterre")
