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


