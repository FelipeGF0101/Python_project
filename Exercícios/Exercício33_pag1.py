"""
Faça um programa que leia um vetor de 15 posições e o compacte, ou seja, elimine as posições com valor zero. Para isso, todos os elementos à frente do zero devem ser movidos uma posição para trás no vetor.
"""
num = []

for n in range(0, 15):
    num.append(int(input('Insira um valor: ')))

print(num)   
for n in num:
    if n == 0:
        num.remove(n)

print(num)