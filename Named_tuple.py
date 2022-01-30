"""
Módulo Collections = Named Tuple

tupla = (1, 2, 3)

print([2])

Named Tuple = São tuplas diferenciadas. Especificamos um nome para a tupla e depois inserimos parâmetros

"""
# Importando

from collections import namedtuple

# Precisamos definir nome e parâmetro

# Forma 1 = Declaração NamedTuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 = Declaração NamedTuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 = Declaração NamedTuple

cachorro = namedtuple ('cachorro', ['idade', 'raca','nome'])

# Usando

ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

# Acessando os dados

# Forma 1

print(ray[0]) # Idade
print(ray[1]) # raça
print(ray[2]) # nome

# Forma 2

print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome


