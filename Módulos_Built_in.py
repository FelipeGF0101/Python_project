"""
Trabalhando com módulos built-in (módulos integrados, que já veem instalados no Python)

Python/ Módulos built-in/
-------------------------

# Utilizando alias (apelidos) para módulos/funções
import random as rdm
# Quando se apelida uma função, deve-se usar o apelido dado, pois o python não reconhece mais com o nome original.

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *
from random import *
# import random

# Tanto o (from random import*) quanto o (import random) importam todas as funções, porém se diferem na utilização. No import random: print(random.random()) | No from random import *: print(random()) | Ou seja, no import * não se faz mais necessário o uso do nome da biblioteca.

# importando todo o módulo

import random

print(random.random())

===================================================================

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

# Utilizando alias (apelidos) para módulos/funções

# É possível apelidar mais de uma função ao mesmo tempo
from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())

"""
# Costumamos utilizar tuple para colocar múltiplos imports de um mesmo módulo

from random import(
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))