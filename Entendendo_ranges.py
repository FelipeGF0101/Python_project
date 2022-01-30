"""
Entendendo Ranges
-> Precisamos conhecer os LOOP FOR para usar os ranges.
-> Precisamos conhecer o range para usar o loop for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

De forma geral:

Exemplo 01

Range(valor de parada)
Obs: valor de parada não inclusive (Padrão: inicio 0 e passo de 1 em 1).


# Forma 01

for num in range(11):
    print(num)

# Forma 02
Range(valor de início / valor de parada)
Obs: valor de parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1)

Exemplo forma 2
for num in range(1, 21):
    print(num)


# Forma 3
Range(valor de inicio / valor de parada, passo)
Obs: valor de parada não inclusive (inicio especificado pelo usuário e passo especificado pelo usuário)

for num in range(0, 51, 5):
    print(num)


#Forma 4 (inversa)
Range(valor de inicio / valor de parada / passo)
Obs: Valor de parada não inclusive (valor inicial especificado pelo usuário e passo especificado pelo usuário)

#Exemplo 4
for num in range(10, -1, -1):
    print(num)

Obs: Aqui, ao invés de colocar um valor a mais no número inicial, colocamos um valor a menos no valor final, pois
se trata de uma contagem regressiva)

"""

