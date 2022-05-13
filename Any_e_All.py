'''
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.

# Exemplo all()
print(all([0, 1, 2, 3, 4])) # Todos os número são verdadeiros, exceto o 0. Dessa forma, o programa retorna um valor False.
print(all([1, 2, 3, 4])) # Todos os número são verdadeiros. Dessa forma, o programa retorna um valor True. 
print(all([])) # Lista vazia restorna True

print(all('Geek')) # Todos os número são verdadeiros? True
print(all([1, -2, 3, 4])) # Todos os número são verdadeiros, exceto o 0. Dessa forma, o programa retorna um valor False. 

nomes =['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes])) # Nesse caso, como todos os elementos da lista começam com a letra 'C', o retorno será 'True'

# Outro exemplo:
nomes1 =['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Daniel']

print(all([nome[0] == 'C' for nome in nomes1])) # Aqui o retorno será 'False' pois nem todos os elementos da lista começam com a letra 'C'

========================================================================================

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna 'False'


'''
print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, 3, 4])) # True

print(any([0, False, {}, (), []])) # False

nomes =['Calos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa'] 

print(any([nome[0] == 'V' for nome in nomes]))