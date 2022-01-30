"""
Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor.
"""

vetor = []
vetor1 = []
vetor2 = []

for i in range(10):
    num = float(input('Digite um valor: '))
    vetor.append(num)
    if num < 0:
        vetor1.append(num)
    else:
        vetor2.append(num)
        
print('===================')     
print(vetor)
print('===================')
print(vetor1)
print('===================')
print(vetor2)
print('===================')
print(sum(vetor2))
print('===================')
print(len(vetor1)) 

print('Os valores adicionados ao vetor foram:', vetor,'. A quantidade de valores negativos foi:',(len(vetor1)),'. Os valores negativos foram:', vetor1,'. Os valores positivos foram:', vetor2,'. A soma dos valores positivos é:',(sum(vetor2)))
