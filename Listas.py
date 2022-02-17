"""
Listas

Listas em Python funcionam como vetores/ matrizes - também chamados de arrays em outras linguagens - com a diferença
de serem DINÂMICAS e também de podermos colocar QUALQUER tipo de dados.

-> Linguagens C e Java (Definição de Arrays):
    - Possuem tamanho e tipo de dado fixo, ou seja, nestas linguagens, se você criar um array do tipo int(inteiro)
e com tamanho 5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

-> Em PYTHON
DINÂMICO: Não possui tamanho fixo. Ou seja, podemos criar a lista e simplismente ir adicionando elementos.
(Porém, esta lista não será infinita! Você poderá adicionar elementos enquanto houver memória disponível).

QUALQUER TIPO DE DADO: Não possui tipo de dado fixo. Ou seja, podemos colocar qualquer tipo de dado.

OBS: As LISTAS  em PYTHON são REPRESENTADAS por colchetes: []

# Podemos facilmente checar se um determinado elemento está na lista.

num = 9
if num in lista4:
    print(f"O número {num} está contido na lista!")
    print(lista4[num])
else:
    print(f"O número {num} não está contido na lista!")
    print(lista4[num])

# PODEMOS FACILMENTE ORGANIZAR UMA LISTA

lista1.sort()
print(lista1)
=========================================================================

# PODEMOS FACILMENTE CONTAR O NÚMERO DE OCORRÊNCIAS DE UM VALOR EM LISTA

print(lista1.count(1))

# ADICIONAR ELEMENTOS EM LISTAS

Para adicionar elementos em listas, utilizamos a função append.

print(lista1)
lista1.append(50)
print(lista1)

print(lista3)
lista3.append("Felipe Guedes")
print(lista3)

# COM O COMANDO APPEND, NÓS SÓ CONSEGUIMOS ADICIONAR UM ELEMENTO POR VEZ. TENTAR INTRODUZIR MAIS DE UM ELEMENTO
# RESULTARÁ EM ERRO. POR EXEMPLO: LISTA3.APPEND(10, 20, 30) -> ERRO.

print(lista3)
lista3.append([10, 20, 30])
print(lista3)

# DA FORMA COMO FOI FEITA NO EXEMPLO ACIMA, NÃO FOI ADICIONADO MAIS DE UM ELEMENTO. NA VERDADE FOI ADICIONADO UM
# UNICO ELEMENTO DO TIPO LISTA. OU SEJA, FOI ADICIONADO UMA LISTA DENTRO DE OUTRA LISTA. LISTA3.APPEND([10, 20, 30]).

if [10, 20, 30] in (lista3):
    print("Encontrei a lista desejada!")
else:
    print("Não encontrei a lista que você procura!")

if ("Felipe Guedes") in (lista3):
    print("Encontrei o nome desejado!")
else:
    print("Não encontrei o nome que você procura!")

# Diferente do comando "append", o comando extend consegue adicionar mais de um elemento por vez nas listas.
# O extend coloca cada valor na lista como um adicional.
# O extend não aceita valor único. Não importa se é do tipo lista. Só aceita mais de um valor!
lista1.extend([120, 130])
print(lista1)

lista3.extend(["Pietro"" ""e"" ""Oliver"])
print(lista3)
====================================================================================

# Podemos adicionar um novo elemento na lista informando a posição do indície.
lista1.insert(0, "Keidy Balieiro")
print(lista1)
# Isso não substitui o valor inicial. O mesmo será alocado para a direita da lista.

# Podemos facilmente juntar duas listas (somar)

lista6 = lista1 + lista2
print(lista6)

# Neste caso, estaremos criando uma nova lista.

# Podemos obter o mesmo resultado usando o comando extend.
# Usando o extend, não estaremos criando uma nova lista, mas sim adicionando outras informações.

lista1.extend(lista2)
print(lista1)

#Podemos facilmente inverter uma lista.
#Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

#Forma 2
print(lista1[::-1])
print(lista2[::-1])

nome = "Felipe"
print(nome[::-1])

#Usamos para copiar uma lista (desta forma, cria-se uma nova lista com as mesmas informações da lista copiada)

lista6 = lista2.copy()
print(lista6)

#Para saber a quantidade de elementos de uma lista > comando "len"

print(len(lista1))

#Podemos remover facilmente o último elemento de umma lista
#OBS: O pop não somente remove o último elemento, como também devolve o elemento retirado.
print(lista1)
lista1.pop()
print(lista1)

#O pop também pode apagar um item por índice (Usei o número 2. Então ele irá apagar o item localizado  na posição 2)
#Os elementos à direita são deslocados para a esquerda.
#Se não houver o indice informado, a tentativa resultará em erro.
lista1.pop(2)
print(lista1)

#Podemos remover todos os elementos(Zerar a lista)
print(lista1)
lista1.clear()
print(lista1)

#Podemos facilmente repetir elementos em uma lista.

nome = [1, 2, 3]
nome = nome * 2
print(nome)

#Podemos facilmente converter uma string para um lista, usando o comando "SPLIT".
#Exemplo 1

curso = "Programação em python: Essencial"
print(curso)
curso = curso.split()
print(curso)

#Obervação: Por padrão o SPLIT separa os elementos da string por meio dos espaços entre elas.
#Exemplo 2
#No exemplo 2, o comando SPLIT foi executado com outra forma. Dessa vez foi informado ao comando que o separador
# é a vírgula. (curso1.split(",")

curso1 = "Programação,em,python"
print(curso1)
curso1 = curso1.split(",")
print(curso1)

#Convertendo uma lista em uma string

lista6 = ["Programação", "em", "Python:", "Essencial"]
print(lista6)

#Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

curso = '$'.join(lista6)
print(curso)

# Podemos colocar qualquer tipo de dado numa lista, inclusive misturando esses dados
lista6 = [1, 2, 34, True, "Geek", "d", [1, 2, 3], 453453]
print(lista6)
print(type(lista6))


#Exemplo 1: Utilizando FOR

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)


#Iterando sobre listas

#Exemplo 2: Utilizando while

carrinho = []
produto = " "

while produto != 'Sair':
    print("Adicione um produto na lista ou digite 'SAIR' para sair: ")
    produto = input()
    if produto != 'Sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Utilizando variáveis em listas
numero = [1, 2, 3, 4, 5]
print(numero)
num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)
=============================================
#posição ~~~~0~~~~~~~~1~~~~~~~~2~~~~~~~3~~~~
cores = ["verde", "amarelo", "azul", "branco"]

print(cores[0])
print(cores[2])

#Da pra fazer acesso aos elementos de forma indexada inversa
# O numero -1 seria o maior número dos negativos, já que seguindo, o valor só tende a diminuir.
# Por exemplo -1, -2, -3, -4

print(cores[-1])
print(cores[-2])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#posição ~~~~0~~~~~~~~1~~~~~~~~2~~~~~~~3~~~~
cores = ["verde", "amarelo", "azul", "branco"]
===========================================================
# Função enumerate(): serve para gerar uma chave numérica sequencial que pode ser associada a uma lista.

#Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

===============================================================
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 2, 44, 42, 27]
lista2 = ["G", "e", "e","k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]
lista3 = []
lista4 = list(range(11))
lista5 = list["Geek Universityt"]

==================================================================
#Listas aceitam valores repetidos
lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

=================================================================
# Outros métodos não tão importantes mas que também são úteis.

# Encontrando o índice de um elemento na lista.

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice da lista está o valor 6?
print(numeros.index(6))

# Em qual índice da lista está o valor 9?
print(numeros.index(9))

#Obs: Caso não exista o valor na lista, será apresentado erro ValueError!

# Em casos de duplicidade de valores na lista
print(numeros.index(5))
# Retorna o índice do primeiro valor encontrado na lista

# Podemos fazer uma busca dentro de um range, ou seja, podemos escolher em qual índice a busca começa.
print(numeros.index(5, 1)) # Buscando a partir do índice 1
# Caso o valor não seja encontrado na lista, será apresentado erro ValueError.

# Podemos ainda fazer uma busca mais específica dentro de um range (início e fim)
print(numeros.index(8, 3, 6)) # Faça busca entre o índice 3 e 6

==================================================================================
# Revisão Slicing
# Lista [inicio:fim:passo]
# Range (inicio:fim:passo)

# Trabalhando com Slice de lista com o parâmetro "INICIO"

lista = [1, 2, 3, 4]
print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes

# Também posso fazer a busca usando número negativo no índice
print(lista[-1:]) # Neste caso específico o "-1" retorna o número 4.

#TRABALHANDO COM SLICE DE LISTA COM PARÂMETRO "FIM"
print(lista[:2]) # Começa em 0, pega até o índice 2 - 1

print(lista[:4]) # Começa em 0, pega até o índice 4 - 1

print(lista[:3]) # Começa em 0, pega até o índice 3 - 1

print(lista[1:3]) # Começa em 1, pega té o índice 3 - 1

# Trabalhando com slice de lista com o parâmetro "PASSO"

print(lista[1::2]) # Começa em 1 e vai até o final pulando de 2 em 2

print(lista[::-1]) # A contagem começa de trás para frente. Se torna uma contagem regressiva.

==============================================================================

# Invertendo valores em uma lista/ poderia ser invertendo a ordem também

nomes = ["Yuri", "Felipe", "Guedes", "Fernandes"]
nomes[0], nomes[1], nomes[2], nomes[3] = nomes[1], nomes[0], nomes[3], nomes[2]
print(nomes)

# Outra forma de inverter os valores da lista

palavras = ["Pietro", "Oliver"]
palavras.reverse()
print(palavras)

=============================================================================
# Como realizar somas, procurar o valor máximo, procurar o valor mínimo e tamanho da lista
# Só é possível com valores inteiros. (ponto flutuante)

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) #Soma
print(max(lista)) #Máximo valor
print(min(lista)) #Mínimo valor
print(len(lista)) #tamanho da lista

==========================================================================
# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]

print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
==============================================================================

# Desempacotamento de lista

lista = [1, 2, 3, 4, 5, 6]

num1, num2, num3, num4, num5, num6 = lista
print(num1, num2, num3)
print(num4, num5, num6)

# OBSERVAÇÃO = Se tivermos mais elementos para desempacotar do que variávei para receber, resultará em erro!

======================================================================================
# Fazendo uma cópia de lista para outra lista. (SHALLOW COPY AND DEEP COPY)

lista = [1, 2, 3, 4, 5, 6]

#Forma1 - Deep copy

print(lista)
nova = lista.copy()

print(nova)

nova.append(7)
nova.append(8)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy(), copiamos os dados de uma lista para uma nova lista, porém elas se mantiveram
# totalmente independentes uma da outra. Ou seja, a primeira lista não foi afetada.
# Isso em Python é chamado de DEEP COPY (Cópia profunda).

# Forma2 - SHALLOW COPY

lista = [1, 2, 3, 4, 5, 6]
print(lista)

nova = lista
print(nova)

nova.append(7)
print(lista)
print(nova)

# Neste exemplo, fizemos a cópia por meio da atribuição de valores.
# Após realizar a modificação em uma das listas, a alteração se refletiu em ambas listas.
# Em Python, isso é chamado de Shallow Copy.
"""
