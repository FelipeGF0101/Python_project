"""
Definindo funções

Funções são pequenas porções de código que realizam tarefas específicas.
Pode ou não receber entrada de dados e retornar uma saída de dados.
Muito úteis para executar procedimentos similares por repetidas vezes.

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom fazer uma verificação para que a função seja simplificada.


Já utilizamos várias funções desde que iniciamos este curso:
por exemplo:

print()
len()
max()
min()
count()
e muitas outras...


# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

print(cores)

curso = 'Programa em Python: Essencial'

print(curso)

cores.append('roxo')

print(cores)

#curso.append('Mais dados...') # AttributeError
#print(curso)

cores.clear()
print(cores)

# DRY - Don't Repeat Yourself - Não repita você mesmo/ Não repita seu código

# Mas então, como definir funções?
# Em python, a forma geral de dfinir uma função é:
# def nome_da_funcao(parametros_de_entrada):
#   bloco_da_funcao

# Onde:
# nome_da_funcao -> SEMPRE, com letras minusculas, e se for nome composto, separado por undeline (snake case)
# parâmetros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vígula, podendo ser opcionais ou não.
# bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece. Neste bloco pode ter ou não retorno da função.

# OBS: veja que para definir uma função. utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos: que é utilizado em python para definir blocos.

==========================================================================

# Definindo a primeira função:

# Definição da função
def diz_oi():
    print('Oi!')

# Observações:
# Veja que dentro das nossas funções podemos utilizar outras funções.
# Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi.
# Veja que esta função não recebe nenhum parâmetro de entrada.
# Veja que esta função não retorna nada.

# Utilizando função:
diz_oi()

# ATENÇÃO:
# Nunca esqueça de utilizar o parênteses ao executar uma função!

# Exemplo:
# Errado 
# diz_oi 

# Certo
#diz_oi()

"""
# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Vida o aniversariante')

for n in range(5):
    cantar_parabens()

# Em python, podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável.

# Forma que não se usa. Não faz muito sentido.
canta = cantar_parabens
canta()