"""
Faça um programa para ler 5 valores, e em seguida, mostre a posição onde se encontram o menor e o maior valor.
"""

lista = []

for i in range(5):
    num = int(input('Digite o valor: '))
    lista.append(num)

(max(lista))
(min(lista))

(lista.index((max(lista))))
(lista.index((min(lista))))

print('A lista introduzida pelo usuário foi:',lista,'. O maior e o menor valor:(',(max(lista)), ',',(min(lista)),'). E seus respectivos índices:',(lista.index((max(lista)))), 'e' ,(lista.index((min(lista)))),)