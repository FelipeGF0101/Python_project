"""
LOOP FOR / ESTRUTURA DE REPETIÇÃO

LOOP = Estrutura de repetição
FOR = Um dos tipos de estrutura de repetição

Python

for item in intereavel:
    //execução do loop

Utilizamos loops para iterar sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geel university'

- Lista
    [1, 3, 5, 7, 9]

- Range
    numero = range(1, 10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) #Temos que transformar em uma lista

#Exemplo de for 1 = iterando sobre uma string
for letra in nome:
    print(letra)

#Exemplo de for 2 = iterando sobre um lista
for numero in lista:
    print(numero)

#Exemplo de for 3 = iterando sobre um rang

(-----------------------------------------------)
range(valor_inicial, valor_final)
Obs: O valor final não é inclusive

for numero in range(1, 10):
    print(numero)
(-----------------------------------------------)
for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

# Quando não precisamos de um valor, podemos usar o sinal underline (_) para descartá-lo.
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

(-----------------------------------------------------------)

quantidade = int(input('Quantas vezes você deseja repetir o loop?''\n'))

for n in range(1, quantidade + 1):
     print(f'imprimindo {n}')

# No comando 'range', o valor final não é incluso na lista.
# Para incluir o último valor, basta adicionar + 1 à quantidade. Por exemplo: for n in range(1, quantidade + 1):
# Para incluir uma posição a mais na lista, inicie a contagem à partir do 0 (zero).
# Por exemplo: for n in range(0, quantidade):

quantidade = int(input('Quantas vezes você deseja repetir o loop?''\n'))
soma = 0

for n in range(1, quantidade +1):
    numero = int(input(f'informe o {n}/{quantidade} valor: '))
    soma = soma + numero
print(f'A soma é igual é {soma}')
(-------------------------------------------------------------)
nome = 'Felipe Guedes'
for letra in nome:
    print(letra, end='') # Use ", end=''" para imprimir na mesma linha.

# Tabela de emojis unicode:https:// apps.timwhitlock.info/emoji/tables/unicode

#original: 	U+1F606
# Para substituir o '+', basta acrescentar três zeros em seu lugar.
#Modificado: U0001F606

for num in range(1, 11):
    print('\U0001F606' * num)

quantidade = int(input('Quantas vezes você deseja repetir o loop?''\n'))

for n in range(1, quantidade + 1):
     print('\U0001F606' * n)
"""
