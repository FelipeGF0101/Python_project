"""
Recebendo dados do usuário.

input() -> Todo dado recebido via input é do tipo string.

Em PYTHON, string é tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas.

Exemplos:
- Aspas simples -> 'Felipe Guedes'
- Aspas duplas -> "Felipe Guedes"
- Aspas simples triplas -> '''Felipe Guedes'''
- Aspas duplas triplas -> "''Felipe Guedes"''
===========================================================================================
# Entrada de dados

print('Qual é o seu nome?')
nome = input()

# Uma outra forma de introduzir dados
nome =input('Qual o seu nome??')

# Processamento
# Exemplo de print antigo 2.x
# Saída de dados

#Exemplo de print 'antigo' - versão 2x do python
print('Seja bem-vindo(a) %s' % nome)
=============================================================================================
#Exemplo moderno de print - versão 3x do python
print('Seja bem-vindo(a) {0}' .format(nome))

#Exemplo de print mais atual - versão 3.7 do Python
print(f'Seja bem vindo(a) {nome}')

#Entrada de dados
# Uma forma mais fácil
idadei=input('Qual a sua idade??')

print('Qual a sua idade?')
idade = input()

#Processamento
#Saída de dados

#Exemplo de print 'antigo' - versão 2x do python
print('O %s tem %s anos' % (nome, idade))

#Exemplo moderno de print - versão 3x do python
print('O {0} tem {1} anos' .format(nome, idade))

#Exemplo de print mais atual - versão 3.7 do Python
print(f'O {nome} tem {idade} anos.')

# Cast é a conversão de um tipo de dado para outro
print(f'O {nome} nasceu em {2021 -int(idade)}')

"""
# EXERCÍCIO

# print('Qual é o seu nome? ')
# nome = input()
# print('Qual é a sua idade? ')
# idade = input()
# print('Qual sua cor favorita? ')
# cor = input()

# print('O nome dele é {0}. A sua idade é {1} e a sua cor favorita é {2}'.format(nome, idade, cor))

# Forma usada atualmente
# print(f'Seu nome é {nome}, sua idade é {idade}, sua cor é {cor}.')

# Usando o 'cast' para saber qual a data de nascimento do indivíduo
#print('Qual o seu nome? ')
#nome = input()

#print('Qual a sua idade? ')
#idade = input()

#print(f'O seu nome é {nome} e você nasceu em {2021 - int(idade)}')

# Outra forma de realizar o cast

print('Qual o seu nome? ')
nome = input()

idade = int(input('Qual a sua idade? '))

print(f' Seu nome é {nome} e você nasceu em {2021 - idade}')
