# Exercice n°49
print("\nExercice n°49 \n")

# Algorithme : affichage des caractères
c = "Hello world !"
for i in range(0, len(c)):
    print(c[i])



# Exercice n°50
print("\nExercice n°50 \n")

def compte_b(chaine):
    compteur_b = 0
    for i in range(0, len(chaine)):
        if chaine[i] == "b":
            compteur_b += 1
    return compteur_b

print("Nombre de 'b' dans \"bob\" :", compte_b("bob"))



# Exercice n°51
print("\nExercice n°51 \n")

def chaine_vers_tab(c):
    t = [""] * len(c)
    for i in range(0, len(c)):
        t[i] = c[i]
    return t

print(chaine_vers_tab("Coucou"))



# Exercice n°52
print("\nExercice n°52 \n")

# A)
def bin2dec(chaine):
    res = 0
#   for i in range(len(chaine)-1, -1, -1):
#       res += int(chaine[len(chaine)-i-1])*2**i
    for i in range(0, len(chaine)):
        puiss = len(chaine) - i - 1
        res += int(chaine[i])*2**puiss
    return res
            
b2 = "1011"
print(b2+" (base 2) =", bin2dec(b2), "(base10)\n")

# B)
def dec2bin(nb):
    res = str(nb%2)
    div = nb//2
    while div != 0:
        res = str(div%2) + res
        div = div//2
    return int(res)

b10 = 11
print(b10, "(base 10) =", dec2bin(b10), "(base 2)")



# Exercice n°53
print("\nExercice n°53 \n")

# A)
phraseE = input("Saisissez une phrase : ") #La lettre e est absente de cette phrase.
phraseZ = ""
for char in phraseE:
    if char == "e":
        char = "z"
    phraseZ += char
print(phraseZ)

# B)
phraseB = input("Saisissez une phrase : ")
phraseR = ""
i = 0
while i < len(phraseB):
    if phraseB[i:i+3] == "Bob":
        phraseR += "Roger"
        i += 3
    else:
        phraseR += phraseB[i]
        i += 1
print(phraseR)



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



# Exercice n°55
print("\nExercice n°55 \n")

# 1)
# c.
def F(caractere):
    n = ord(caractere) - ord('a')
    r = (n*9)%26
    c = chr(r+ord('a'))
    return c

# 2)
# a.
def chiffre(chaine):
    chaine_chiffree = ""
    for i in range(len(chaine)):
        car = chaine[i]
        if ord(car) >= 97 and ord(car) <= 122:
            car = F(car)
        chaine_chiffree += car
    return chaine_chiffree


            

# b.
# Algorithme A1
from random import randint
t = int(input("Saisissez un entier : "))
rand_str = ""
for i in range(t):
    rand_str += chr(randint(97, 122))
print("\nChaine de départ :", rand_str, "\nVersion chiffrée :", chiffre(rand_str))

# c.
def dechiffre(chaine):
    chaine_dechiffree = ""
    for i in range(len(chaine)):
        car = chaine[i]
        if ord(car) >= 97 and ord(car) <= 122:
            n = ord(car) - ord('a')
            r = (n*3)%26
            car = chr(r+ord('a'))
        chaine_dechiffree += car
    return chaine_dechiffree

print(dechiffre("jwndwyx!"))
# Fin