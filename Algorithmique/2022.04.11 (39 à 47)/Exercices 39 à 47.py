# Exercice 39

# 1. Un tableau est une variable qui contient plusieurs éléments facilement accessibles et possédant chacun un indice.
# 2. Il est représenté par des crochets [].
# 3. En indiquant le nom du tableau suivi de l'indice entre crochets. ex : tab[i].
# 4. Avec une boucle.
# 5. tab = [1, 2, 3] + [4, 5]    ou    tab1 += [4, 5]
# 6. tab.append(elt)    ou    tab = tab + [elt]
# 7. tab = N*[randint(0, 9)]



# Exercice 40
print("\n"+"Exercice 40"+"\n")

tab = [3, 1, 2, 3, 8, 9, 3]
print("Avant :", tab)
for i in range(0, len(tab)):
    if tab[i] == 3:
        tab[i] = 8
print("Après :", tab)



# Exercice 41
print("\n"+"Exercice 41"+"\n")

def affiche_tab(tab):
    for i in range(0, len(tab)):
        print("tab["+str(i)+"] =", tab[i])
#test
tableau41 = [0, 1, 2, 3, 8, 9, 7, 4, 6, 5]
print(affiche_tab(tableau41))



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

# 4)
# Algorithme : AlgoRefExo42
from random import randint
#
n = int(input("Quelle taille le tabExo42 doit-il faire ? "))
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


# Exercice 43
print("\n"+"Exercice 43"+"\n")

# Pseudo-code

# Fonction triple(tab):
# Variables locales : tab, copie_tab, i
# DEBUT Fonction
#     copie_tab <- tab[:]
#     Pour i Allant De 0 à len(copie_tab) exclus:
#         copie_tab[i] <- copie_tab[i]*3
#     Fin Pour
#     retourner copie_tab

# Python
def triple(tab):
    copie_tab = tab[:]
    for i in range(0, len(copie_tab)):
        copie_tab[i] *= 3
    return copie_tab



# Exercice 44
print("\n"+"Exercice 44"+"\n")

# Pseudo-code

# Fonction miroir(tab):
# Variables locales : i, j, tmp, tab
# DEBUT Fonction
#    i <- 0
#    j <- len(tab)-1
#    Tant Que i != j:
#        tmp <- tab[i]
#        tab[i] <- tab[j]
#        tab[j} <- tmp
#        i += 1
#        j +=1
#    Fin Tant Que
#    retourner tab
# FIN Fonction

# Py
def miroir(tab):
    i = 0
    j = len(tab)-1
    while i != j:
        tmp = tab[i]
        tab[i] = tab[j]
        tab[j] = tmp
        i += 1
        j -= 1
    return tab



# Exercice 45
print("\nExercice 45\n")

# Pseudo-code

# Algorithme : tab_Fibonacci
# Variables : fibo
# DEBUT

# fibo <- 20*[0]
# fibo[0] <- 5
# fibo[1] <- 2
# Pour i Allant De 2 A len(fibo) exclus:
#    fibo[i] <- fibo[i-1] + fibo[i-2]
# Fin Pour
# Afficher : fibo
# FIN

fibo = 20*[0]
fibo[0] = 5
fibo[1] = 2
for i in range(2, len(fibo)):
    fibo[i] = fibo[i-1] + fibo[i-2]

print("fibo = ", fibo)



# Exercice 46
print("\nExercice 46 : Tri à bulle\n")

# 1)
# Pseudo-code

# Fonction tribulles(tab)
# Variables locales : tab, i, j, tmp
# DEBUT Fonction
#     Pour i Allant De 0 A longueur(tab)-1 exclu:
#         Pour j Allant De i+1 A longueur(tab) exclu:
#             Si tab[i] > tab[j]:
#                 tmp <- tab[j]
#                 tab[j] <- tab[i]
#                 tab[i] <- tmp
#             Fin Si
#         Fin Pour
#     Fin Pour
#     retourner tab
# FIN Fonction



# Python
def tri(tab):
    for i in range(0, len(tab)-1):
        for j in range(0, len(tab)-1):
            if tab[j] > tab[j+1]:
                tmp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = tmp
    return tab