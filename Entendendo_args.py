"""
Entendendo *args

- O *args é um parâmetro como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que comece com asterisco

Exemplo: 
*xis

MAs por convenção, utilizamos *args para definí-lo

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1,num2,num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

# print(soma_todos_numeros(4, 6)) TypeError - Porque o programa esperava o valor de 3 parâmetros. Só não daria erro caso os valores fossem estabelecidos na própria função. (num1 = 2, num2 = 6, num3 = 5 por exemplo)

# print(soma_todos_numeros(4, 6, 9, 5)) TypeError

============================================

# Entendendo *args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

print(soma_todos_numeros())
print(soma_todos_numeros(1,))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# Também poderia ser

def soma_todos_numeros(*args):
    return sum(args) # Usando função pra somar tudo.

print(soma_todos_numeros())
print(soma_todos_numeros(1,))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

# É possível trabalhar da mesma forma com float
print(soma_todos_numeros(24.5, 26.3))

# O *args não obriga a passar valores, mas caso utilize outros parâmetros, como por exemplo: def soma_todos_numeros(nome, email, *args), o nome e o email tem que receber valores correspondentes.

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Felipe', 'Guedesgf@gmail.com'))
print(soma_todos_numeros('Felipe', 'Guedesgf@gmail.com', 1,))
print(soma_todos_numeros('Felipe', 'Guedesgf@gmail.com', 2, 3))
print(soma_todos_numeros('Felipe', 'Guedesgf@gmail.com', 2, 3, 4))
print(soma_todos_numeros('Felipe', 'Guedesgf@gmail.com', 3, 4, 5, 6))

=================================================

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza de quem é você...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))

"""
def soma_todos_numeros(*args):
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7] # Aqui a função vai interpretar como um único elemento.
#print(soma_todos_numeros(numeros))

# Desempacotador
num1, num2, num3, num4, num5, num6, num7 = numeros
print(soma_todos_numeros(num1, num2, num3, num4, num5, num6, num7))

# Desempacotando de forma automática
print(soma_todos_numeros(*numeros)) # Aqui ele vai funcionar seja tupla, lista, conjunto. Só não funciona com dicionário

# OBS: O ASTERISCO SERVE PARA QUE INFORMEMOS AO PYTHON QUE ESTAMOS PASSANDO COMO ARGUMENTO UMA COLEÇÃO DE DADOS. DESTA FORmA, ELE SABERÁ QUE PRECISARÁ ANTES DESEMPACOTAR ESTES DADOS.