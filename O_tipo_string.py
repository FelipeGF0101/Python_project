"""
O tipo string

Em python, um dado é considerado do tipo string sempre que:

- Estiver entre aspas simples: 'Tipo String', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas: "Tipo String", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas: '''Tipo String''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre aspas duplas triplas: """Tipo String""", """234""", """a""", """True""", """42.3"""

nome = 'Felipe Guedes'
print(nome)
print(type(nome))

nome = "Keidy Balieiro"
print(nome)
print(type(nome))

nome = '''Pietro Balieiro'''
print(nome)
print(type(nome))

nome = """Oliver Balieiro"""
print(nome)
print(type(nome))

# O termo /n é usado para pular uma linha. É parecido com o 'escrevaL' do portugol.
# Por exemplo:

nome = 'Yuri \nFernandes'
print(nome)
print(type(nome))

# A quebra de linha também pode ser feita da seguinte forma:

nome = """Apolo 
Chico"""
print(nome)
print(type(nome))

nome = 'bianca'
print(nome.upper())
# O comando -> .upper() <- serve para deixar todos os caracteres da string maiúsculos.
# O comando -> .isupper() <- serve como verificador da condição da string. Se é TRUE or FALSE.
# Se a String é maiúscula ou minúscula. BIANCA = .isupper() = TRUE / bianca = .isupper() = FALSE.

nome = 'BIANCA'
print(nome.lower())
# O comando -> .lower() <- serve para deixar todos os caracteres da string minúsculos.
# O comando -> .islower() <- serve como verificador da condição da string. Se é TRUE or FALSE.
# Se a String é maiúscula ou minúscula. BIANCA = .islower() = FALSE / bianca = .islower() = TRUE.

nome = 'Felipe Guedes'
print(nome.split())
# O comando -> .split() <- serve para criar uma espécie de lista, separando uma string que antes era inteira.

"""nome = 'YURI FELIPE GUEDES FERNANDES'
print(nome.split())
resultado = ['YURI', 'FELIPE', 'GUEDES', 'FERNANDES']
"""
# String 'keidy'     =     [k, e, i, d, y.]
# Corresponde à posição    [0, 1, 2, 3, 4.]
# Número total de caracteres menos 1. Do 0 ao 4, mas na verdade são 5 posições.
nome = 'keidy'
print(nome[0:5])

# String 'Yuri Felipe Guedes Fernandes', usando o comando .split(), funciona dessa forma:
#         [Yuri][Felipe][Guedes][Fernandes]
# Posição:[ 0  ][   1  ][   2  ][    3    ]
nome = 'Yuri Felipe Guedes Fernandes'
print(nome.split()[2:4])
# Slice de string

nome = 'Yuri'
print(nome[2], nome[0])
# Uma das formas.

# Uma forma mais simples de inverter todos os itens da string.
#
nome = 'Yuri Felipe Guedes Fernandes'
print(nome[::-1])