'''
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas.
Já a função reversed() funciona com qualquer iterável
Sua função é inverter o iterável

'''
lista = [1, 2, 3, 4, 5]

res = reversed(lista)
print(res)
# A função reversed() retorna um iterável chamado List Reverse Iterator
# Podemos converter o elemento retornando para uma Lista, Tuplaou conjunto.

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# Conjunto(set)
print(set(reversed(lista))) # OBS: Em conjuntos não definimos a ordem dos elementos.

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

nome = 'Felipe'

print(reversed(nome), ''.join(list(reversed(nome))))

# Já vimos como fazer isso mais fácil com o slice de strings
print('Geek University' [::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)