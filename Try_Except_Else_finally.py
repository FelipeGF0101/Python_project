"""
Try / Except / Else / Finally

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

num = 0

try:
    num = int(input('Informe um valor: '))
except ValueError:
    print('Valor incorreto')

print(f'Você digitou {num}')

# Utilizando o ELSE
# Else ->  É executado somente se não acorrer erro.

try:
    num = int(input('Informe um valor: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Utilizando Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando o finally')

# OBS: O bloco finally é SEMPRE executado. Independente se houe exceção ou não.
# O finally, geralmente é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo
# Exemplo 1

def dividir(a, b):
    return a/b
try:
    num1 = int(input('Informe o primeiro número: '))
    num2 = int(input('Informe o segundo número: '))
except ValueError:
    print('O valor precisa ser numérico!')
else:
    print(dividir(num1, num2))

# Exemplo 2

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo 3 - Tratamento genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except :
        return 'Ocorreu um problema'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
"""
# Exemplo 4 - Tratamento semi - genérico

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))