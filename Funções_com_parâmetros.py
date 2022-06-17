'''
FUNÇÕES COM PARÂMETRO (de entrada)

- Funções que recebem dados para serem processador dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:

- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída.

==================================================================================

# Refatorando um função

def quadrado_de_7():
    return 7 * 7

print(quadrado_de_7())

# Função com parâmetro

def quadrado(numero):
    return numero * numero

print(quadrado(7))
print(quadrado(6))
print(quadrado(5))

# Outra forma

def quadrado(numero):
    return numero ** 2

print(quadrado(7))
print(quadrado(6))
print(quadrado(5))

ret = quadrado(2)
print(ret)

===================================================================
# Refatorando a função

def cantar_parabens(aniversariante):
    print('Parabéns pra você ')
    print('Nesta data querida ')
    print('muitas felicidades ')
    print('muitos anos de vida ')
    print(f'Viva o {aniversariante}!')

cantar_parabens('Felipe')

====================================================================
# Funções pode ter n parâmentros de entrada. Ou seja, podemos receber como entrada em uma função
# quantos parâmetros forem necessários. Eles são separados por vígula.

# EXEMPLO

def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return(num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))


print(multiplica(3, 5))


print(outra(3, 2, 'olá '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError
# Exemplos:
# print(soma(2, 3, 4)) TypeError - Passando argumentos a mais
# print(soma(4)) TypeError - Passando argumentos a menos.

==============================================================================

# Nomeando parâmetros

def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'

print(nome_completo('Felipe', 'Guedes'))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaradas na definição de uma função.
# Argumentos são dados passado durante a execução de uma função.

# A ordem dos parâmetros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (keyword arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

'''
# Erro na utilização do return

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))
    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))

