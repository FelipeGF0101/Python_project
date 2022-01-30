"""
Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C.

"""
import random
A = random.sample(range(0, 20), 10)
A1 = set(A)
print(A)

B = random.sample(range(0, 20), 10)
B1 = set(B)
print(B)

C = A1-B1
print(C)