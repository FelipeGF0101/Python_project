"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> inseto

# OBS: A utilização do print() para debugar código é uma prática ruim
def dividir (a,b):
    try:
        return int(a)/ int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'
print(dividir(4, 7))

# OBS: Existem formas mais profissionais de debugar código, utilizando o debugger.
# Em python, podemos fazer isso em diferentes IDE's, como o pycharm ou utilizando o PDB.

def dividir(a, b):
    try:
        return int(a)/int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Exemplo com o PDB -> Python Debugger

# Para utilizar o Python Debugger, precisamos * importar a biblioteca PDB e então utilizar a função set_trace()


# COMANDOS BÁSICOS DO PDB
# l (para listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a execução - finaliza o debugging)

# FORMA 1
import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# FORMA 2

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)

# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas no início do arquivo.
# Por isso, ao invés de colocarmos o import do pdb no início do arquivo, nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção.

# FORMA 3

# A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi incorporado como função built-in (integrada)
chamada breakpoint().

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o curso ' + curso
print(final)
"""
# OBS: Cuidado com conflitos entre nomes de variáveis e os comandos do pdb

def soma(l,n, p, c):
    breakpoint()
    return l+n+p+c

print(soma(1,3,5,7))

# Neste caso, usa-se o comando PDB 'p' + 'nome da variável'. Assim: (Pdb) p l ou (Pdb) p n