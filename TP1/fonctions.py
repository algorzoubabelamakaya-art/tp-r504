# Q2.2 - première version 
# def puissance(a, b):
#     return a ** b

# Q2.4 - avec vérification de type 
# def puissance(a, b):
#     if not type(a) is int:
#         raise TypeError("Only integers are allowed")
#     if not type(b) is int:
#         raise TypeError("Only integers are allowed")
#     return a ** b

# Q4.6 - avec gestion du cas 0 puissance négative 
# def puissance(a, b):
#     if not type(a) is int or not type(b) is int:
#         raise TypeError("Only integers are allowed")
#     if a == 0 and b < 0:
#         raise Exception("0 à une puissance négative est indéfini")
#     return a ** b

# Partie 5 
def puissance(a, b):
    # on vérifie que a ET b sont bien des entiers (int)
    if not type(a) is int or not type(b) is int:
        raise TypeError("Only integers are allowed")

    # cas particulier : 0 à une puissance négative (ex: 0^-1 = 1/0) -> indéfini
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