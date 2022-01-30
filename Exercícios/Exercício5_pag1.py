"""
Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

"""
num = [10, 33, 49, 50, 86, 40, 39, 20, 18, 57]
print(num)
contador = 0
cont2 = 0
for i in num:
    if (i%2) == 0:
        contador = contador + 1    
    else:
        cont2 = cont2 + 1

print("O vetor possui", contador,"números pares.")
print("O vetor possui", cont2, "números ímpares.")
        

