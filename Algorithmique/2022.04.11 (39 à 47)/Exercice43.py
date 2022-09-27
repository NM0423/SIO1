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
#test
tableau = [2, 3, 5]
print("tab =", tableau)
print("copie de tab =", triple(tableau))