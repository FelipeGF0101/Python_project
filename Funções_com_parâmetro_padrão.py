'''
Funções com parâmetros padrão (Default Paramters)

- Funções onde a passagem de parâmetros seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

======================================
Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))

print(quadrado())

=================================================================

# Forma comum 
def exponencial(numero, potencia):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

def exponencial(numero, potencia = 2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3)) # Se o valor não for fornecido, retornará ERRO
print(exponencial(3, 5)) # Eleva à potência informada pelo usuário


def exponencial(numero = 4, potencia = 2):
    return numero ** potencia
print(exponencial())

# OBS: Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro número, e será calculado o quadrado deste número;
# Se o usuário passsar 2 argumentos, o primeiro será atribuído ao parâmetro número e o segundo ao parâmetro potência. Então será calculada esta potência.

 ========================================================================

 # OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar ao final da declaração

# ERRO!
def teste(potencia, num = 2)):
    return num ** potência

print(teste(6))

================================================
# Outros exemplos
def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))

print(soma(4)) # TypeError
print(soma()) # TypeError

# Para não gerar TypeError, o código deve ser assim:

def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))

print(soma(4)) 
print(soma())

=========================================================

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor = False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek'
    elif nome == 'GEEK':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}' 

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(True))
print(mostra_informacao(nome='Felipe'))

# Por que utilizar parâmetros com valor default?
# - Nos permite ser mais flexíveis nas funções.
# - Evita erros com parâmetros incorretos;
# - Nos permite trabalhar com exemplos mais legíveis de código

# Quais tipos de dados podemos utilizar como valores default para  parâmetro?
# - Qualquer tipo de dado:
# - Números string, floats, booleanos, listas, tuplas, dicionários, funções etc

=================================================================

# Exemplos
def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma): # Se o usuário fornecer um outro parâmetro, ele será substituído.
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3)) # A função mat já recebeu o parâmetro para soma, caso nenhum outro parâmetro seja passado para ela.
print(mat(2, 2, subtracao))

=============================================================
# Escopo - Evitar problemas e confusões

# Variáveis globais
# Variáveis locais

instrutor = 'Geek' # Variável global

def diz_oi():
    return f'oi {instrutor}'

print(diz_oi())

# Outro exemplo

def diz_oi():
    instrutor = 'Python' # Mesmo que exista uma variável global, a função usa preferencialmente uma variável local
    return f'Oi {instrutor}'

print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof = 'Geek' # Variável local
    return f'Olá {prof}'

print(diz_oi())

# A variável local só existe dentro da função criada. Caso tente usar a variável fora da função, o programa retorna-rá Error
print(prof) # NameError

# ATENÇÃO com variáveis globais (se puder evitar, evite.)

total = 0 

def incrementa():
    total = total + 1 # UnboundLocalError ( A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

# Forma correta

def incrementa():
    global total # Usando o 'global', estamos avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())

==========================================================

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador # Variável NONLOCAL, quer dizer que não estou usando a variável local nem uma variável global, estou usando a variável que se encontra em outra função
        contador = contador + 1
        return contador
    return dentro()

print(fora())

'''
