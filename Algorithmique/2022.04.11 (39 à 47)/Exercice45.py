# Exercice 45
print("\nExercice 45\n")

# Pseudo-code

# Algorithme : tab_Fibonacci
# Variables : fibo
# DEBUT

# fibo <- 20*[0]
# fibo[0] <- 5
# fibo[1] <- 2
# Pour i Allant De 2 A len(fibo) exclus:
#    fibo[i] <- fibo[i-1] + fibo[i-2]
# Fin Pour
# Afficher : fibo
# FIN

fibo = 20*[0]
fibo[0] = 5
fibo[1] = 2
for i in range(2, len(fibo)):
    fibo[i] = fibo[i-1] + fibo[i-2]

print("fibo = ", fibo)