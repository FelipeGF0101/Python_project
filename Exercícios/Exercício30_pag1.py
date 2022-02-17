"""
Faça um programa que leia dois vetores de 10 elementos. Crie um vetor que seja a intersecção entre os 2 vetores anteriores, ou seja, que contém os números dos dois vetores. Não deve conter números repetidos.

"""
import random

a = random.sample(range(1, 20), 10) 
b = random.sample(range(1, 20), 10)
c = []

for i in a:
    if i in b:
        c.append(i)
print(a)
print(b)
print(c) 
