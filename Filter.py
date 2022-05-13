"""

Filter

filter() -> Serve para filtrar dados de uma determinada coleção

# Biblioteca para trabalho com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean() # Mean = média
media = statistics.mean(dados)

print(media)

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo 
# uma função é um iterável.

res = filter(lambda x: x > media, dados) # Uma análise dos dados da lista 'dados' para imprimir os que forem maior que o resultado 'média'
print(list(res))

# OBS: Assim, como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

====================================================================

paises = ['', ' Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)

res = filter(None, paises) # O tipo None elimina os espaços vazios da lista.
print(list(res))

res = filter(lambda p: p == 'Brasil', paises) # Retorna a string mensionada 
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))

=========================================================================

# A diferença entre map() e filter() é:

# map() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do iterável.

# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de acordo com a função.

===========================================================================

# Exemplo mais complexo

usuarios = [
    {"username": "Samuel", "Tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "Tweets": ["Eu amo meu gato"]},
    {"username": "Jeff", "Tweets": []},
    {"username": "Bob123", "Tweets": []},
    {"username": "Doggo", "Tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "Gal", "Tweets": []}

]

# Filtrar os usuários que estão inativos no twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['Tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario ['Tweets'], usuarios))
print(inativos)

"""
# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde de que cada nome tenha menos de 5 caracteres.

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) > 5, nomes)))

print(lista)

lista1 = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: nome == 'Ana', nomes)))
print(lista1)

lista2 = list(map(lambda nome: f'Sua instrutora é {nome}', nomes))
print(lista2)
