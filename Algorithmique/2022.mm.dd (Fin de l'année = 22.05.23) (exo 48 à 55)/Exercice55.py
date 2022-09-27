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


