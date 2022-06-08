'''
Sorted

OBS: Não confunda com a função sort(), apesar do nome. O sort() só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

# Exemplo

numeros = [6, 1, 8, 2, 3, 7, 5, 4]
print(sorted(numeros)) # Ordena do menor para o maior
# O sorted SEMPRE retorna uma lista com os elementos do iterável ordenado
# Com o sorted o iteravel permanece inalterado. Ele só ordena ao printar na tela.

# Adicionando parâmetros ao sorted()

print(sorted(numeros, reverse=True)) # Ordena do maior para o menor

print(set(sorted(numeros)))
print(tuple(sorted(numeros)))

# ==========================================================

from multiprocessing import Value

usuarios = [
    {"username": "Samuel", "Tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "Tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "Tweets": []},
    {"username": "Bob123", "Tweets": []},
    {"username": "Doggo", "Tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Gal", "Tweets": [], "Cor": "Preto", "Musica": "Rock"}

]

print(f'\n{usuarios}')
print("=================================================================")
# Ordenando por ordem alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print("=================================================================")
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))
print("=================================================================")
# Ordenando pelo número de Tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["Tweets"])))

'''

# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock n'roll", "tocou": 32}

]

# Ordenando da menos tocado para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
# Ordenando da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))