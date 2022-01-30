"""
Módulo Collections - Ordered Dict

# Em um dicionário a ordem de inserção dos elementos não é garantida

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
============================================================================

# OrderedDict -> É um dicionário que nos garante a ordem correta de inserção dos elementos
# Fazendo o import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

"""
# ENTENDENDO A DIFERENÇA ENTRE DICT (DICIONÁRIO) E ORDEREDDICT (DICIONÁRIO ORDENADO)

from collections import OrderedDict

# Dicionários comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # false or true?? True, já que no dicionário comun a ordem dos elementos não importa

# ordereddict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # false or true?? False, já que para o orderedDict a ordem dos elementos é importante
