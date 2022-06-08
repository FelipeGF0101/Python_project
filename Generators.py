'''
Generators Expression

Em aulas anteriores nós estudamos:
- List comprehension;
- Dicionary Comprehension;
- Set Comprenhension;

Não vimos:
- Tupla comprehension... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

========================================================================

# Poderíamos ter feito utilizando Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension
resposta = [nome[0] == 'C' for nome in nomes]
print(type(resposta))

# Generator
resposta1 = (nome[0] == 'C' for nome in nomes)
print(type(resposta1))

# A diferença entre o List Comprehension e o Generator é que no caso do Generator trabalhamos com tuplas. 

===============================================================
# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('University'))
print(getsizeof(9))
print(getsizeof(91))
print(getsizeof(True))

'''
from sys import getsizeof

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
print(list_comp)

# Gerando uma lista de números com Set Comprehension
Set_comp = getsizeof({x * 10 for x in range(1000)})
print(Set_comp)

# Gerando uma lista de números com Dictionary Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
print(dict_comp)

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set_Comprehension: {Set_comp} bytes')
print(f'Dictionary Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)