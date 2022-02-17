"""
Faça um programa que receba 6 números inteiros e mostre:

> Os números pares digitados;
> A soma dos números pares digitados;
> Os números ímpares digitados
> A quantidade de números ímpares digitados.

"""

lista = []
lista1 = []
lista2 = []


for i in range(6):
    lista.append(int(input('Insira um valor: '))) # Recebe valores do usuário e armazena na lista
print(lista)

# O trecho de código acima poderia ser feito da seguinte forma: lista = [int(input('Insira os valores: ')) for i in range(6)]

for num in lista:
    if num % 2 == 0:
        lista1.append(num)
    else:
        lista2.append(num)

(sum(lista1))
(len(lista2))

print(f'Os números pares são {lista1}. Os números ímpares são {lista2}. O valor dos números pares somados é de {(sum(lista1))} e a quantidade de valores ímpares é {(len(lista2))}')

