"""
Tipo Float
ou
Tipo Real
ou
Tipo Decimal

#OBS:COMO O PYTHON FUNCIONA EM INGLÊS, A SEPARAÇÃO DOS NÚMEROS EM CASAS DECIMAIS É FEITO ATRAVÉS DO
PONTO, E NÃO DA VÍRGULA.
"""

#Errado do ponto de vista do float (decimal), mas gera uma 'tupla' (que será estudado mais a frente)
valor = 1,44
print(valor)
print(type(valor))

#Certo do ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
valor1 = 1.44
valor2 = 1.44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um float(decimal) para um int(inteiro)
"""
OBS: AO CONVERTER VALORES FLOAT PARA INTEIROS, NÓS PERDEMOS PRECISÃO
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

#Podemos trabalhar com números complexos

variavel = 5j
print(type(variavel))