"""
Listas Aninhadas

- Algumas linguagens de programação (c/java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais ( Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em python nós temos as listas

numeros = [1, 2, 3, 4, 5]
valores = [1, 'b', 3.234, True, 5]
============================================

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 X 3
print(type(listas))

# Como fazemos para acessar os dados? 
print(listas[0][1]) # 2
print(listas[2],[2]) # 8

# Iterando com loops em uma lista aninhada.
for lista in listas:
    for num in lista:
        print(num)
        
"""
# List Comprehension
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for i in range(1, 4)])