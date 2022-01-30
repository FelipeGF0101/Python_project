"""
Escrva um programa que leia 10 números inteirose os armazene em um vetor. Imprima o vetor, o maior elemento e a posição em que ele se encontra:

"""
lista = [20, 30, 42, 12, 49, 90, 90, 90, 38, 48, 18, 29, 90]

print(len(lista))
print(lista)
print(max(lista))
print(lista.index(90)) # Essa forma mostra apenas o resultado de um valor. Se tiver mais valores repetidos na lista, ele ignora o restante.

import numpy as np

lista = np.array(lista)

result = np.where(lista == 90)

print(result)

