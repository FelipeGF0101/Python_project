"""
TUPLAS - (Tuple)

Tuplas são bastante parecidas com listas.
Existem duas diferenças importantes:

1 - As Tuplas são representas por parênteses () e as listas são representadas por colchetes []

2 - As Tuplas são imutáveis. Isso significa que ao ser criada, ela não aceita alteração. Toda aperação em uma tupla
gera uma nova tupla.

# CUIDADO: As duplas são representadas por parênteses. Mas veja:

tupla1 = (1, 2, 3, 4, 5, 6) # É uma Tupla
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6 # É uma Tupla

print(tupla2)
print(type(tupla2))

# CUIDADO: Tuplas com 1 elemento:

tupla3 = (4) # Não é uma tupla. Para Python esse valor é um int (inteiro).
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # É uma tupla!
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))

# Podemos concluir que não são só os parênteses que definem uma tupla, mas também as vírgulas.

=======================================================================================
# Podemos gerar uma Tupla dinamicamente com o Range.

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

======================================================================================
# Desempacotamento de tupla

tupla = (1, 2, 3, 4)
num1, num2, num3, num4 = tupla

print(num1)
print(num2)

tupla1 = ("Felipe", "Guedes")
nome, sobrenome = tupla1

print(sobrenome)
print(nome)

# Importante = Gera erro se colocarmos um número diferente de elementos para desempacotar
=========================================================================================
tupla1 = (1, 2, 3, 4, 5, 6)
print(max(tupla1)) # Maior número
print(min(tupla1)) # Menor número
print(sum(tupla1)) # Soma de todos os números
print(len(tupla1)) # Total de elementos

======================================================================================
#Concatenação de tuplas
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

tupla2 = (7, 8, 9, 10, 11, 12)
print(tupla2)

print(tupla1 + tupla2)
=======================================================================================
# Verificando se determinado elemento está contido na tupla
tupla1 = (1, 2, 3)
print(3 in tupla1)
print(2 in tupla1)

tupla2 = ("Felipe Guedes")
print("Felipe" in tupla2)

=======================================================================================
# Iterando sobre uma tupla
tupla = (1, 2, 3, 4, 5, 6)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)
======================================================================================
#Contando elementos dentro de uma tupla
tupla = ("A, B , C, D, E, A, B")
print(tupla.count("A"))

nome = tuple("Felipe Guedes")
print(nome)
print(nome.count("e"))
======================================================================================
#Dicas na utilização de tuplas

#Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

# Acesso a elementos de uma tupla também é semelhante ao de uma lista

print(meses[4])

# Iterar com While
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

#Verificando em qual indice o elemento está na tupla

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(meses.index("junho"))
# OBS: Caso o elemento não exista, será gerado erro.

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

#Slicing

# tupla[inicio:fim:passo]

print(meses[0::2])
=======================================
# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro.
# * Isso porque o código traz segurança para os códigos.

==========================================================================
# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla

print(tupla)
print(nova)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
"""
