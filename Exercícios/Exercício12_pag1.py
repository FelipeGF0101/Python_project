"""
Faça um programa para ler 5 valores, e em seguida, mostrar todos os valores lidos juntamente com o maior, o menor e a média do valores.
"""
lista = []
media = 0
for i in range(5):
    num = int(input('Digite o valor: '))
    lista.append(num)
    for num in lista:
        media = (media + num)/5

print(lista)
print(max(lista))
print(min(lista))
print(media)