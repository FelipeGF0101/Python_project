"""
Listas

Listas em Python funciona como vetores e matrizes (chamado de arrays em outras linguagens), com a diferença
de serem dinâmicos e também de podermos colocar QUALQUER tipo de dados.

Em linguagens como C ou Java: Arrays
    - Possuem tamanho e tipo de dados fixo; ou seja, nestas linguagens, se você criar um array do tipo inteiro
    e de tamanho 5 por exemplo, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE 5 valores no máximo.

EM PYTHON
DINÂMICO: NÃO POSSUI TAMANHO FIXO; ou seja, nós podemos criar uma lista e ir adicionando elementos.
Qualquer tipo de dado: Nõa possuem tipos de dados fixo, ou seja, podemos colocar qualquer tipo de dado.

As listas em Python são representadas por colchetes. []
"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27] #inteiro

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"] #strings

lista3 = [] #listavazia

lista4 = list(range(11))

lista5 = list("Geek University")

#Podemos facilmente checar se determinado valor está na lista

