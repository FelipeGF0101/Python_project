"""
Leia 10 números inteiros e armazene em um vetor v. Crie dois novos vetores v1 e v2. Copie os valores ímpares de v para v1, e os valores pares de v2. Note que cada um dos vetores v1 e v2 têm no máximo 10 elementos, mas nem todos os elementos são utilizados. No final escreva os elementos UTILIZADOS de v1 e v2. 

# NÃO ENTENDI EXATAMENTE O PEDIDO DO ENUNCIADO!
"""
import random

v = random.sample(range(1, 20), 10)
v1 = []
v2 = []
for num in v:
    if num % 2 == 0:
        v2.append(num)
    else:
        v1.append(num)

print(v1, v2)