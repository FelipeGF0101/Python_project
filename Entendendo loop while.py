"""
Loop While

Loop while = Loop enquanto (estrutura de repetição "enquanto")

While:
Expressão Booleana:
    \\Execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleana: é toda expressão cujo resultado é verdadeiro ou falso.

Por exemplo:

num = 5
num < 5
resultado: false

Exemplo 1
numero = 1
while numero < 11:
    print(numero)
    numero = numero + 1

#Em um loop while, é importante cuidar do critério de parada.

"""
#Exemplo 2
resposta = ''

while resposta != 'sim':
    resposta = input(" Já acabou Jessica? ")
