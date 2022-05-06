'''
DEFININDO FUNÇÕES

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada. 


# Exemplos:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (built-in) do python print()

print(cores)

curso = 'Programação em Python: Essencial'
print(curso)

# curso.append('mais dados...') #AttributeError


cores.append('roxo')
print(cores)

cores.clear()
print(cores)

# COMO DEFINIR FUNÇÕES?

Em python, a forma geral de definir uma função é:

def nome_da_função(parâmetros_de_entrada):
    bloco_da_função

Onde:

nome_da_função -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (snake case):

parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um sepadado por vírgula, podendo ser opcionais ou não.

bloco_da_função -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.

Neste bloco, pode ter ou não retorno da função. 

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos ':'.

Dois pontos é utilizado em python para definir blocos.

'''

# Definindo a primeira função

def diz_oi():
    print('OI!')

'''
OBS: 
1 - Veja que, dentro das nossas funções podemos utilizar outras funções.
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer 'OI';
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;

'''

# Utilizando funções

# Chamada de execução
diz_oi()

'''
ATENÇÃO:

Nunca esqueça de utilizar o parênteses ao executar um função.
EXEMPLO:

# Errado
diz_oi

# Certo
diz_oi()

# Errado
diz_oi () # Não tem espaço
'''

# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('nesta data querida')
    print('muitas felicidades')
    print('muitos anos de vida')

cantar_parabens()

# Variação do exemplo 2

import time
def cantar_parabens():
    time.sleep(1)
    print('Parabéns pra você')
    time.sleep(1)
    print('nesta data querida')
    time.sleep(1)
    print('muitas felicidades')
    time.sleep(1)
    print('muitos anos de vida')

cantar_parabens()

# Exemplo 3
def contador():
    cont = 0
    for n in range(0, 10):
        cont = cont + 1
        print(cont)

contador()

# Exemplo 4

def contador_2():
    for n in range(5):
        contador()

contador_2()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.

canta = cantar_parabens
canta()
