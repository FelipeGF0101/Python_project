'''
LEN - ABS - SUM - ROUND

# len

len() -> retorna o tamnaho (ou seja, o número de itens) de um iterável


# Só pra revisar

print(len('geek university'))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len()
print('Geek Uniersity'.__len__())

============================================================================
# ABS

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal


# Exemplo abs()

print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

# OBS: O abs() não se aplica a string

=====================================================================================

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial.

# OBS:> O valor inicial default = 0


# Exemplos SUM

print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))

print(sum([3.145, 5.678]))
print(sum((1, 2, 3, 4, 5)))
print(sum({1, 2, 3, 4, 5}))

# print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})) Aqui vai resultar um erro, pois a função não consegue somar.
# Deve-se especificar o que a função deve somar. Conforme exemplo abaixo:

print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

=============================================================================================
# ROUND

round() -> Retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada retorna o inteiro mais próximo da entrada. 

'''
# Exemplos round()

print(round(10.2))
print(round(10.5))
print(round(10.6))
print(round(1.21212121, 2))
print(round(1.2199999, 2))

