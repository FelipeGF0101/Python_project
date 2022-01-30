"""
Faça um programa que leia um vetor de 10 posições e verifique se existem valores iguais e os escreva na tela.
=================================================================================================

# Forma que ainda não entendo direito

from collections import defaultdict

# Define a lista de valores
lista = [2, 2, 3, 4, 4, 5, 5, 8, 9, 3]

# Define o objeto que armazenará o índice de cada elemento
keys = defaultdict(list)

# Percorre todos os elementos da lista
for key, value in enumerate(lista):
    keys[value].append(key)

# Exibe o resultado
for value in keys:
    if len(keys[value]) > 1:
        print(value, keys[value])

# Retorno:

# 2 [0, 1]
# 3 [2, 9]
# 4 [3, 4]
# 5 [5, 6]

"""

# Forma mais simples

vetor = [3, 4, 4, 5, 7, 7, 8, 9, 10, 9]

print(vetor)
repet = vetor.count(4)

print(repet)