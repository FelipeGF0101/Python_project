"""
Escreva um programa que leia números inteiros no intervalo [0,50] e os armazene em um vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares do primeiro vetor. Imprima os dois vetores, 2 elementos por linha.

"""

imp = []
import random
from typing import NamedTuple
result = random.sample(range(0, 51), 10)

print(result)

for num in result:
    if num%2 != 0:
        imp.append(num)

print(imp)

# ATÉ O MOMENTO NÃO DESCOBRI UM FORMA DE IMPRIMIR DOIS ITENS POR LINHA.



for num in range(len(imp)):
    print(imp[num:num])