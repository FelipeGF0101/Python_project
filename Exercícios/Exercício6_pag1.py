"""
Faça um programa que receba do usuário um vetor com 10 posições. Em seguida, deverá ser impresso
o maior e o menor elemento do vetor.

"""
lista = []
valor = 0

for c in range(0,10):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

print(lista)


print(max(lista))
print(min(lista))