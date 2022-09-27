# Exercice n°54
print("\nExercice n°54 \n")

def tab_mots(chaine):
    tab = []
    i = 0
    while i < len(chaine)-1:    # Rappel : longueur - 1 = dernier élément
        j = i+1
        while chaine[j] != " " and j < len(chaine):
            j += 1
        tab += [chaine[i:j]]
        if j+1 < len(chaine)-1:    # S'éxécute tant que j+1 ne correspond pas au dernier caractère
            i = j+1
        elif chaine[j+1] != " ":    # S'éxécute si le dernier caractère n'est pas un espace 
            tab += chaine[j+1]
            i = j+1
        else:   # S'éxécute si j+1 correspond au dernier caractère et que celui-ci est un espace
            i = j+1
    return tab

print(tab_mots("La réponse est 42 !"))


       