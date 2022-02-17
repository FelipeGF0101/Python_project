"""
Leia dois conjuntos de números reais, armazenando-os em vetores e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar é dado por: x1 * y1 + x2 * y2 +...+xn*yn.

"""
# u.v = número
# Vetor 'U', escalar '.', vetor 'v'

# ângulo agudo -> produto escalar positivo > 0
# ângulo obtuso -> produto escalar negativo < 0
# ângulo reto -> produto escalar igual a zero == 0

import random

x = random.sample(range(-5, 10), 5)

y = random.sample(range(-5, 10), 5)

print('Vetor x:', x)
print('Vetor y:', y)
print('=====' * 10)

pEscalar = (x[0] * y[0]) + (x[1] * y[1]) + (x[2] * y[2]) + (x[3] * y[3]) + (x[4] * y[4]) 
print(f'O produto escalar: ({x[0]} * {y[0]}) + ({x[1]} * {y[1]}) + ({x[2]} * {y[2]}) + ({x[3]} * {y[3]}) + ({x [4]} * {y[4]}) = {pEscalar}')
print('=====' * 10)
if pEscalar > 0:
    print(f'O resultado do produto escalar foi {pEscalar}. Deste modo, podemos concluir que os vetores formam um ÂNGULO AGUDO.')
elif pEscalar < 0:
    print(f'O resultado do produto escalar foi {pEscalar}. Deste modo, podemos concluir que os vetores formam um ÂNGULO OBTUSO.')
elif pEscalar == 0:
    print(f'O resultado do produto escalar foi {pEscalar}. Deste modo, podemos concluir que os vetores formam um ÂNGULO RETO.')