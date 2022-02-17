"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a união entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números repetidos.

"""
import random

vetor = []
vetor1 = random.sample(range(1, 20), 10)
vetor2 = random.sample(range(1, 20), 10)

for i in vetor1:
    vetor.append(i)
for i in vetor2:
    if i not in vetor1: 
        vetor.append(i)
print(vetor1, vetor2)
print(vetor)