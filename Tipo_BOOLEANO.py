"""
Tipo Booleano

Álgebra Booleana, criada por George Boole

2 Constantes:Verdadeiro ou Falso

Em python:
True -> Verdadeiro
False -> Falso

Obs: Sempre com a inicial maiúscula.

Errado:
true;
false.

Certo:
True;
False.

"""
ativo = True
print(ativo)

"""
Operações básicas
"""
# Negação (Em python, utiliza-se o 'not')
# Not: Fazendo a negação, se o valor booleano for verdadeiro, o resultado será Falso.
# se for Falso, o resultado será Verdadeiro.

print(not ativo)

logado = False

# Ou (Em python, utiliza-se o 'or')
# É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro (true)

"""
True or True: True
True or False: True
False or True: True
False or False: False

Ou seja: 
Em caso de dois valores positivos: Resultado positivo(True);
Em caso de um valor positivo e um negativo: Resultado positivo(True);
Em caso de um valor negativo e um positivo: Resultado positivo(True);
Em caso de dois valores negativos: O resultado será negativo.
"""
print(ativo or logado)

# E (Em python, utiliza-se 'and')
# É uma operação binária. Ambos os valores devem ser verdadeiros.

"""
True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""