"""
Leia 10 números inteiros e armazene em um vetor. Em seguida escreva os elementos que são primos e suas respectivas posições no vetor.

"""
import random

vetor = random.sample(range(1, 20), 10)
vetor1 = []
vetor2 = []

for num in vetor:
    if num%2 != 0:
        vetor1.append(num)
    
for i in vetor1:
    (vetor.index(i))
    vetor2.append((vetor.index(i)))

print(f'\nO conjunto original tem os seguintes valores {vetor}. Os números primos são {vetor1}. \nOs respectivos indices são {vetor2}.')
