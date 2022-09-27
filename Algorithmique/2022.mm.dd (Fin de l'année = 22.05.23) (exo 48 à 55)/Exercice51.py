# Exercice n°51
print("\nExercice n°51 \n")

def chaine_vers_tab(c):
    t = [""] * len(c)
    for i in range(0, len(c)):
        t[i] = c[i]
    return t

print(chaine_vers_tab("Coucou"))


