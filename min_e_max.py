'''
Min e Max

Max() -> Retorna o maior valor em um iteravel ou maior de dois ou mais elementos

# Exemplos -> MAX()

lista = [1, 8, 4, 99, 34, 129]
print(max(lista)) 

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla)) 

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto)) 

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f':129}
print(max(dicionario)) # f 

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f':129}
print(max(dicionario.values())) # 129


# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

print(max('a', 'ab', 'abc'))

print(max('a', 'b', 'c', 'd', 'z'))

print(max(3.145, 5.789))

print(max('Geek Universisty'))

print(max('Yuri', 'Felipe', 'Paralelepipedo'))

print(max('Yuri', 'Felipe', 'Paralelepipedo', 'z'))

print(max('abelha', 'bola', 'casa', 'dado', 'zebra'))

==========================================================

MIN() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos


# Exemplos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista)) 

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla)) 

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto)) 

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f':129}
print(min(dicionario)) # a 

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f':129}
print(min(dicionario.values())) # 1


# Faça um programa que receba dois valores do usuário e mostre o menor

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

print(min('a', 'ab', 'abc'))

print(min('a', 'b', 'c', 'd', 'z'))

print(min(3.145, 5.789))

print(min('Geek Universisty'))

print(min('Yuri', 'Felipe', 'Paralelepipedo'))

print(min('Yuri', 'Felipe', 'Paralelepipedo', 'z'))

print(min('abelha', 'bola', 'casa', 'dado', 'zebra'))

'''
# Outros exemplos

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# Por ordem alfabética
print(max(nomes)) # Tim
print(min(nomes)) # Arya

# Por tamanho da string
print(max(nomes, key=lambda nome: len(nome))) # Ollivander
print(min(nomes, key=lambda nome: len(nome))) # Tim

# ==========================================================

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock n'roll", "tocou": 32}

]

print(max(musicas, key=lambda musica:musica['tocou']))
print(min(musicas, key=lambda musica:musica['tocou']))

print('Desafio! Imprima somente o título da música mais e menos tocada.')
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica:musica['tocou'])['titulo'])

print('Desafio! Como encontrar a música mais tocada e a menos tocada sem usar max(), min() e lambda?')
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(f'A música MAIS tocada foi: {musica["titulo"]}')

min = max
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(f'A música MENOS tocada foi: {musica["titulo"]}')
