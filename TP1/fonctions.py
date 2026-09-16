# question 4.6 - version active
def puissance(a, b):
    # on vérifie que a ET b sont bien des entiers (int)
    # si l'un des deux ne l'est pas, on déclenche une erreur TypeError
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    # cas particulier : 0 à une puissance négative (ex: 0^-1 = 1/0)
    # c'est mathématiquement indéfini, donc on lève une exception volontairement
    if a == 0 and b < 0:
        raise Exception("0 à une puissance négative est indéfini")

    # si tout est bon, on calcule et renvoie a élevé à la puissance b
    return a ** b