'''
Módulo random
O que são módulos?

- Em python, módulos nada mais são do que outros arquivos Python.

Módulo random -> Possui várias funções para geração de números pseudo-aleatórios.


# OBS: Existem duas formas de se utilizar um módulo ou função deste

# Forma 1 - importando todo o módulo (Não recomendado)
# Consultando documentação da função
# dir(random)
# help(random)

import random 

# random() -> Gera um número real pseudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo,
# ficarão disponíveis (ficarão em memória). Caso você saiba quais funções você precisa utilizar deste módulo, então esta não seria
# a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso, mas a função random() é apenas uma função dentro do módulo random.


# Forma 2 - Importando uma função específica do módulo

from random import random # Forma recomendada!

# No import acima, estamos falando: Do módulo random, importe a função random.

for i in range(10):
    print(random())


# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 10)) # O número 10 não é incluído


# Randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.

# Gerador de apostas para a mega sena.

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ') # começa em 1 e vai até 60


# Choice() -> Mostra um valor aleatório entre um iteráel.
from random import chance
from secrets import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

'''

# Shuffle() -> Tem a função de embaralhar  dados
from random import shuffle


cartas = ['k', 'q', 'j', 'A', '2', '3', 4 ,5, 6, 7]

print(cartas)
shuffle(cartas)
print(cartas)