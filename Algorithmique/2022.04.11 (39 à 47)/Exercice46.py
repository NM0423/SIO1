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
#test
print(tri([7, 15, 8, 9, 2, 14, 11]))