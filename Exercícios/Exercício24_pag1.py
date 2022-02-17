"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em metros. Encontre o aluno mais baixo e o mais alto. Mostre o número do aluno mais baixo e do mais alto, juntamente com suas alturas.

"""

aluno1 = [1, 1.80]
aluno2 = [2, 2.00]
aluno3 = [3, 1.65]
aluno4 = [4, 1.70]
aluno5 = [5, 2.10]
aluno6 = [6, 1.85]
aluno7 = [7, 1.78]
aluno8 = [8, 1.55]
aluno9 = [9, 1.98]
aluno10 = [10, 1.68]

print('=====' * 10)
print(aluno1)
print('=====' * 10)
print(aluno2)
print('=====' * 10)
print(aluno3)
print('=====' * 10)
print(aluno4)
print('=====' * 10)
print(aluno5)
print('=====' * 10)
print(aluno6)
print('=====' * 10)
print(aluno7)
print('=====' * 10)
print(aluno8)
print('=====' * 10)
print(aluno9)
print('=====' * 10)
print(aluno10)

todos = [aluno1[1], aluno2[1], aluno3[1], aluno4[1], aluno5[1], aluno6[1], aluno7[1], aluno8[1], aluno9[1], aluno10[1]]
listaunica = []

for i in todos:
    listaunica.append(i)
print('=====' * 10)
print(listaunica)

min(listaunica)
max(listaunica)


if min(listaunica) == 1.80:
    print(f'O menor aluno é {aluno1}')
elif min(listaunica) == 2.00:
    print(f'O menor aluno é {aluno2}')
elif min(listaunica) == 1.65:
    print(f'O menor aluno é {aluno3}')
elif min(listaunica) == 1.70:
    print(f'O menor aluno é {aluno4}')
elif min(listaunica) == 2.10:
    print(f'O menor aluno é {aluno5}')
elif min(listaunica) == 1.85:
    print(f'O menor aluno é {aluno6}')
elif min(listaunica) == 1.78:
    print(f'O menor aluno é {aluno7}')
elif min(listaunica) == 1.55:
    print(f'O menor aluno é {aluno8}')
elif min(listaunica) == 1.98:
    print(f'O menor aluno é {aluno9}')
elif min(listaunica) == 1.68:
    print(f'O menor aluno é {aluno10}')

if max(listaunica) == 1.80:
    print(f'O maior aluno é {aluno1}')
elif max(listaunica) == 2.00:
    print(f'O maior aluno é {aluno2}')
elif max(listaunica) == 1.65:
    print(f'O maior aluno é {aluno3}')
elif max(listaunica) == 1.70:
    print(f'O maior aluno é {aluno4}')
elif max(listaunica) == 2.10:
    print(f'O maior aluno é {aluno5}')
elif max(listaunica) == 1.85:
    print(f'O maior aluno é {aluno6}')
elif min(listaunica) == 1.78:
    print(f'O maior aluno é {aluno7}')
elif min(listaunica) == 1.55:
    print(f'O maior aluno é {aluno8}')
elif max(listaunica) == 1.98:
    print(f'O maior aluno é {aluno9}')
elif max(listaunica) == 1.68:
    print(f'O maior aluno é {aluno10}')