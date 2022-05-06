'''
Funções com retorno


numeros = [1, 2, 3]
numeros.pop()

ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}') # O pop não só remove o número. Ele também pode retornar o valor recebido.

ret_pr = print(numeros)
print(f'Retorno de ret_pr: {ret_pr}') # o print não retorna nada.

=============================================================================
# Exemplo de função

def quadrado_de_7():
    print(7 * 7)

quadrado_de_7()

ret = quadrado_de_7()

print(f'Retorno: {ret}')
# OBS: Em python, quando uma função não retorna nenhum valor, o retorno é none.

# Vamos refatorar a função acima para que ela retorne um valor.
# OBS: Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return.
# OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a execução da função para outras funções.

def quadrado_de_7():
    return 7 * 7

#Criamos uma variável para receber o retorno da função.
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

# Refatorando a primeira função

def diz_oi():
    return 'Oi '

alguem = 'Felipe'

print(diz_oi() + alguem)

 OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função; 

# Exemplo 1:

def diz_oi():
    print('Estou sendo executado após o retorno...')
    return 'Oi!' # O return finaliza a função. Após o return nada é executado
    print('Estou sendo executado após o retorno...')

print(diz_oi())

2 - Podemos ter em uma função, diferentes returns;

# Exemplo 2:

def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores.

# Exemplo 3:

def outra_funcao():
    return 2, 3, 4, 5

num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4) # Os valores não tem necessariamente que pertencer a uma variável. O return por sí só já poderia retornar os valores, só que seriam imprimidos em forma de tupla, já que foram separados por vírgula.

print(outra_funcao())
print(type(outra_funcao()))

=======================================================================
# Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    # Gera um número pseudo - randômico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

# Refatorando

def joga_moeda1():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda1())

'''
# Erros comuns na utilização do return

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    else: # Aqui o else não seria necessário já que só tem duas possibilidades
        return False

print(eh_impar())

#def eh_impar():
#    numero = 5
#   if numero % 2 != 0:
#        return True
#   return False

#print(eh_impar())

# Jogo de pedra/papel/tesoura
import random

def pedra_papel_tesoura():
    valor = random.randint(1, 4)
    if valor == 1:
        return  'Pedra'
    elif valor == 2:
        return 'Papel'
    return 'Tesoura'

print(pedra_papel_tesoura())