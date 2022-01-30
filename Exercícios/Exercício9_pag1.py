"""
Crie um programa que leia 6 valores inteiros pares, e em seguida, mostre os valores lidos na ordem inversa.

"""
lista = []
valor = 0

for i in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        lista.append(valor)

print(lista)

print('===============================')
lista.reverse()
print(lista)
