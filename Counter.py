"""
Módulo collections - Counter

Collections - High-performance container datetypes

Counter: Recebe um interável como parâmetro e cria um objeto do tipo collections counter que é parecido com um
dicionário, contendo como chave o elemento da lista passada como parâmetro, e como valor, a quantidade de ocorrências
desse elemento.


# Exemplo 1

# Realizando o import

from collections import Counter

# Podemos utilizar qualquer interável. Aqui usamos uma lista:

lista = [1, 1, 1, 2, 2, 3, 3, 1, 7, 7, 3, 4, 4, 4, 5, 5]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 4, 3: 3, 4: 3, 2: 2, 7: 2, 5: 2})
# Veja que, para elemento da lista, o Counter criou uma chave e colocou como valor, a quantidade de ocorrências.
============================================================================

# Exemplo 2

from collections import Counter

print(Counter("Yuri Felipe Guedes Fernandes"))
# Counter({'e': 6, ' ': 3, 'u': 2, 'r': 2, 'i': 2, 'F': 2, 'd': 2, 's': 2, 'n': 2, 'Y': 1, 'l': 1, 'p': 1, 'G': 1, 'a': 1})

# O Counter contou todas as ocorrências dos elementos da string

===================================================================

# Exemplo 3

from collections import Counter

texto = "Super Mario 64 é um jogo eletrônico de plataforma desenvolvido pela Nintendo Entertainment Analysis &
Development e publicado pela Nintendo. Lançado em 1996 para o Nintendo 64, é o primeiro título da série Super Mario
a oferecer gráficos tridimensionais (3D). O jogador controla o protagonista Mario, que percorre pelo castelo da
princesa Peach na missão de resgatá-la de Bowser. Super Mario 64 apresenta uma jogabilidade em mundo aberto, com
o seu grau de liberdade sendo através de áreas relativamente grandes compostas principalmente por polígonos
tridimensionais, em vez de apenas sprites bidimensionais (2D). Ele enfatiza a exploração em vastos mundos, que
exigem que o jogador complete várias missões, além das ocasionais pistas de obstáculos lineares (como nos jogos
de plataforma tradicionais). Ele preserva muitos dos elementos de jogabilidade e personagens dos jogos anteriores
da franquia, bem como o estilo visual."

palavras = texto.split()

print(palavras)

res = (Counter(palavras))

print(res)

# Encontrando as 5 palavras com maior ocorrência no texto

print(res.most_common(5))
"""


