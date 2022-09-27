# Exercice n°50
print("\nExercice n°50 \n")

def compte_b(chaine):
    compteur_b = 0
    for i in range(0, len(chaine)):
        if chaine[i] == "b":
            compteur_b += 1
    return compteur_b

print("Nombre de 'b' dans \"bob\" :", compte_b("bob"))


