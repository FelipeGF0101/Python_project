"""
Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem valores negativos.
"""
vetor = [-3, 4, 3, -5, 8, 9, -23, -9, 7, 10]
cont=0
print(vetor)

for index, value in enumerate(vetor):
    if value < 0:
        vetor[index] = 0

print(vetor)

