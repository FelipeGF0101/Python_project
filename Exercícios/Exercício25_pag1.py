"""
Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não são múltiplos de 7 ou que terminem com 7.

"""
numeros = []

for i in range(0, 101):
    numeros.append(i)
    if i  % 7 == 0:
        numeros.remove(i) 
           
    elif i % 10 == 7:
        numeros.remove(i)


print(numeros)


