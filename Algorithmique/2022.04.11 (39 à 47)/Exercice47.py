# Exercice 47
print("\nExercice 47 : Bogo-tri\n")

# 1)
# Pseudo-code

# Fonction : ordre(tab)
# Variables locales : tableau : tab,
#                     entiers : i, compteEltOrdre
#                     booléen : bonOrdre
# DEBUT Fonction
#     bonOrdre <- Faux
#     compteEltOrdre <- 0
#     Pour i Allant De 0 à longueur(tab)-1:
#         Si tab[i] < tab[i+1]:
#             compteEltOrdre <- compteEltOrdre + 1
#         Fin Si
#     Fin Pour
#     Si compteEltOrdre = longueur(tab):
#         bonOrdre <- Vrai
#     Fin Si
#     retourner : bonOrdre
# FIN Fonction


# Py
def ordre(tab):
    bonOrdre = False
    compteEltOrdre = 1
    for i in range(0, len(tab)-1):
        if tab[i] < tab[i+1]:
            compteEltOrdre += 1
    if compteEltOrdre == len(tab):
        bonOrdre = True
    return bonOrdre
#test
print(ordre([7, 8, 9, 1]))
print(ordre([7, 8, 9, 10]))

# 2)
# a/ tab et bogotab => tableaux, i => entier
# b/ La ligne 8 concatène 2 copies de tab