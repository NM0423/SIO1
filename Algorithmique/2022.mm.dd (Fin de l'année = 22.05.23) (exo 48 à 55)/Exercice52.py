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


