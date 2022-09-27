# Exercice 44
print("\n"+"Exercice 44"+"\n")

# Pseudo-code

# Fonction miroir(tab):
# Variables locales : i, j, tmp, tab
# DEBUT Fonction
#    i <- 0
#    j <- len(tab)-1
#    Tant Que i != j:
#        tmp <- tab[i]
#        tab[i] <- tab[j]
#        tab[j} <- tmp
#        i += 1
#        j +=1
#    Fin Tant Que
#    retourner tab
# FIN Fonction

# Py
def miroir(tab):
    i = 0
    j = len(tab)-1
    while i != j:
        tmp = tab[i]
        tab[i] = tab[j]
        tab[j] = tmp
        i += 1
        j -= 1
    return tab
#test
print("[1,2, 3]")
print(miroir([1, 2, 3]))



# ALT
def miroirM1(tab):
    m = []
    for i in range(len(tab)-1, -1, -1):
        m.append(tab[i])
    return m

print("\nmiroirM1 : \n[1, 2, 10]")
print(miroirM1([1, 2, 10]))



def miroirM2(tab):
    m = len(tab)*[0]
    j = len(tab)-1
    for i in range(0, len(tab)):
        m[i] = tab[j]
        j -= 1
    return m

print("\nmiroirM2 : \n[22, 15, 6]")
print(miroirM2([22, 15, 6]))


def miroirM3(tab):
    a = 0
    b = len(tab)-1
    m = tab[:]
    while a != b:
        m[a] = tab[b]
        m[b] = tab[a]
        a += 1
        b -=1
    return m

print("\nmiroirM3 : \n[12, 24, 36, 48, 60]")
print(miroirM3([12, 24, 36, 48, 60]))
    