def puissance(a, b):
    # on vérifie que a ET b sont bien des entiers (int)
    # si l'un des deux ne l'est pas, on déclenche une erreur TypeError
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    # cas particulier : 0 à une puissance négative (ex: 0^-1 = 1/0)
    # c'est mathématiquement indéfini, donc on lève une exception volontairement
    if a == 0 and b < 0:
        raise Exception("0 à une puissance négative est indéfini")

    # si l'exposant est négatif, on divise resultat par a, -b fois
    if b < 0:
        resultat = 1
        for _ in range(-b):
            resultat /= a
        return resultat

    # sinon (exposant positif ou nul), on multiplie resultat par a, b fois
    resultat = 1
    for _ in range(b):
        resultat *= a
    return resultat