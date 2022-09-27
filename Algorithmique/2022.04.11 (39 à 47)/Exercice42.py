# Exercice 42
print("\n"+"Exercice 42 : Algos de référence"+"\n")

# 1)
# Pseudo-code

# Fonction somme(tab)
# Variables locales : somme_elt, i
# DEBUT Fonction
#    somme_elt = 0
#    Pour i Allant De 0 à len(tab) exclus:
#        somme_elt <- somme_elt + tab[i]
#    Fin Pour
#    retourner somme_elt
# FIN Fonction

# Python
def somme(tab):
    somme_elt = 0
    for i in range(0, len(tab)):
        somme_elt = somme_elt + tab[i]
    return somme_elt
#test
print("1) Somme =", somme([2, 4, 10])) # ou tab = [2, 4, 10] puis print(somme(tab))

# 2)
# Pseudo-code

# Fonction compte(val, tab)
# Variables locales : compteur, elt
# DEBUT Fonction
#    apparition <- 0
#    Pour elt Dans tab
#        Si elt = val
#            apparition <- apparition + 1
#        Fin Si
#    Fin Pour
#    retourner compteur
# FIN Fonction

# Python
def compte(val, tab):
    apparition = 0
    for elt in tab:
        if elt == val:
            apparition += 1
    return apparition
#test
print("2)", compte(8, [8, 4, 1, 8, 10, 8]), "apparitions.")

# 3)
# Pseudo-code

# Fonction maximum(tab)
# Variables locales : max
# DEBUT Fonction
#     maxi <- tab[0]
#     Pour i Allant De 1 à len(tab) exclus:
#         Si tab[i] > maxi:
#             maxi <- tab[i]
#         Fin Si
#     Fin Pour
#     retourner maxi
# FIN Fonction

# Python
def maximum(tab):
    maxi = tab[0]
    for i in range(1, len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
    return maxi
#test
print("3) max =", maximum([1, 42, 8, 5]))


# 4)
# Algorithme : AlgoRefExo42
from random import randint
#
n = int(input("Quelle taille tabExo42 doit-il faire ? "))
tabExo42 = []
print()
#
for i in range(n):
    elt = randint(1, 10)
    tabExo42.append(elt)
for i in range(0, len(tabExo42)):
    print("tabExo42["+str(i)+"] =", tabExo42[i])
#
print("4) Somme des valeurs du tableau =", somme(tabExo42), end=".\n   ")
print("8 apparaît", compte(8, tabExo42), "fois dans le tableau", end=".\n   ")
print("max =", maximum(tabExo42), "\n")



#