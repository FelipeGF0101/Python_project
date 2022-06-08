'''
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saídas de erros geradas pelas execução do nosso código.

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja, você escreveu algo que o Python não reconhece como parte da linguagem.

# Exemplos SyntaxError

A)
def funcao:
    print('Geek University')

B)
def = 1

C)
return # Puro e simples

2 - NameError -> Ocorre quando uma variável ou função não foi definida

# Exemplos NameError

A)
print(geek)

B)
geek()

C)
a = 18

if a < 10:
    msg = 'É maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

# Exemplos TypeError

A)
print(len(5))

B)
print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando um índice inválido.

# Exemplos IndexError

A)
lista = ['Geek']
print(lista[2])

B)
lista = ['Geek']
print(lista[0][10])

C)
tupla = ('Geek',)
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto mas vvalor inapropriado

# Exemplo ValueError

A)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

# Exemplos KeyError

A)
dic = {'python': 'University'}
print(dic['Geek'])

7 - AttributeError -> Ocorre quando uma variável não tem uma atributo/função

# Exemplos AttributeError

A)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python (4 espaços)

# Exemplos IndentationError

A)
def noa():
print('GEEK')

# OBS: Exceptions e Erros são sinônimos na programação.

# OBS: Importante ler e prestar atenção na saída de erros
'''
