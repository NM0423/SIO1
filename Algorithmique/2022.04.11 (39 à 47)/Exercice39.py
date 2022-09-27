# Exercice 39

# 1. Un tableau est une variable qui contient plusieurs éléments facilement accessibles et possédant chacun un indice.
# 2. Il est représenté par des crochets [].
# 3. En indiquant le nom du tableau suivi de l'indice entre crochets. ex : tab[i].
# 4. Avec une boucle.
# 5. tab = [1, 2, 3] + [4, 5]    ou    tab1 += [4, 5]
# 6. tab.append(elt)    ou    tab = tab + [elt]
# 7. On déclare un tableau vide puis on ajoute les valeurs dedans

from random import randint
N = randint(0, 9) 
print("Longueur de tab =", N, "\n")
tab = []
for i in range(0, N):
    elt = randint(0, 9)
    tab.append(elt)

for i in range(0, len(tab)):
    print("tab["+str(i)+"] =", tab[i])