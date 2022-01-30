"""
Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições pares os valores do primeiro e nas posições ímpares os valores do segundo.
"""
import random
import itertools

A = random.sample(range(0, 20), 10)

B = random.sample(range(0, 20), 10)

print('Liata A: ' + str(A))
print('Lista B: ' + str(B))

# zip() pode ser usado para vincular as listas e, em seguida, chain()pode ser usado para executar o acréscimo alternativo
# dos elementos conforme desejado.
C = list(itertools.chain(*zip(A, B)))
print(C)

"""
O módulo 'ITERTOOLS' nos traz 4 funções que simplificam o uso de análises combinatórias, como permutações e combinações, por exemplo:
> product
> permutations
> Combinations
> combinations_with_replacement

FUNÇÃO PRODUCT:
Assinatura da função: product(*iterables, repeat=1)
Essa função computa o produto cartesiano dos iteráveis de entrada.

PRODUTO CARTESIANO: é a multiplicação entre pares ordenados de conjuntos distintos.

O parâmetro *iterable possibilita a passagem de um número de variável de entradas.

Para calcular o produto de um iterável consigo mesmo, utiliza-se o argumento opcional repeat para especificar o número de repetições.

Por exemplo: considere os conjuntos (1,2) e (a,b). O resultado do produto cartesiano desses dois conjuntos será (1, a), (1, b), (2,a), (2,b).

A saída desta função são tuplas ordenadas.

Exemplo:

from itertools import product 

print(list(product([1, 2], repeat = 2)))
print(list(product([1, 2], [1, 2])))     
print(list(product(['Python'], ['Academy', 'Rocks']))) 
print(list(product([1, 2], [3, 4], [5, 6])))

==============================================================================================================
FUNÇÃO PERMUTATIONS:

Assinatura da função: permutations(iterable[, r])

Utilizado para gerar os elementos como únicos baseado em suas posições, e não em seus valores.

Por conta dessa característica, a saída de list(permutations([1, 1])) será [(1,1), (1,1)] e não apenas [(1, 1)].

O parâmetro r é o tamanho da permutação e se não especificado ele é definido como o comprimento do iterável de entrada.

from itertools import permutations

print(list(permutations([1, 2])))
print(list(permutations([1, 2, 3])))
print(list(permutations([1, 2, 3], r=2)))

==================================================================================================================

FUNÇÃO COMBINATIONS:

Assinatura da função: combinations(iterable[, r])

Essa função traz todas as combinações do iterável 'iterable' de tamanho r, sem substituição.

Se você já estudou estatística para concurso se lembra desse tipo de questão: calcule a quantidade de possíveis combinações de X elementos, escolhidos de tanto em tanto.

Essa função é muito poderosa e pode auxiliar em diversos tipos de problemas diferentes.

Vamos analisar uma questão comum de entrevistas de emprego:

> Você tem três notas de R$ 20, cinco de R$ 10, duas de R$ 5 e cinco notas de R$ 1. De quantas maneiras você pode pagar uma conta de R$100?

from itertools import combinations

# Notas disponíveis
notas = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

soma_100 = []

# Loop sobre o tamanho de combinações possíveis
for n in range(1, len(notas) + 1):
  # Loop sobre as possíveis combinações verificando se somam 100
  for combinacao in combinations(notas, n):
    if sum(combinacao) == 100:
      soma_100.append(combinacao)

# Remove os itens repetidos
resultado = list(set(soma_100))

print(f'As possíveis combinações de notas que somam R$ 100 são:{len(resultado)}')
print(resultado)

=======================================================================================================

FUNÇÃO COMBINATIONS_WITHS_REPLACEMENT

Assinatura da função: combinations_with_replacement(iterable, r)

Esta função retorna uma combinação de elementos de comprimento r a partir dos elementos iterável 'iterable', com substituição.

Os elementos individuais podem se repetir, diferente do que acontece na função combinations.

from itertools import combinations

print(list('combinations_with_replacement'([1, 2], r=1)))
print(list('combinations_with_replacement'([1, 2], r=2)))
print(list('combinations_with_replacement'([1, 2, 3], r=2)))
print(list('combinations_with_replacement'('ABC', r=2)))

Agora vamos entender as diferenças entre combinations e combinations_with_replacement.

Suponha as chamadas combinations([1, 2, 3], r=2) e combinations_with_replacement([1, 2, 3], r=2), que resultam em [(1, 2), (1, 3), (2, 3)] e [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)], respectivamente.

Veja que a saída da segunda função inclui (1, 1) e (2, 2). Essa é a diferença para combinations, isto é: elementos individuais podem se repetir.

============================================================================================================

ITERADORES DE ENCERRAMENTO

Os iteradores de encerramento são usados para processar iteráveis de entrada finitos e produzir saídas com base na função utilizada.

Os métodos presentes nessa subdivisão são: accumulate, chain, chain.from_iterable, compress, dropwhile, filterfalse, grouby, islice, starmap, takewhile, tee e zip_longest.

Agora vamos um à um.

FUNÇÃO ACCUMULATE

Assinatura da função: accumulate(iterable[, func])

Esta função recebe dois argumentos, o iterável iterable e a função func que será aplicada a cada iteração.

Se nenhuma função for passada, a função operator.add é utilizada por padrão.

Se o iterável de entrada estiver vazio, o iterável de saída também estará vazio.

A cada iteração um acumulador é utilizado para auxiliar no cálculo das iterações seguintes.

import itertools 
import operator 
  
lista = [2, 2, 4] 
    
# Função a ser utilizada: operator.add (padrão)
print(list(itertools.accumulate(lista))) 
# Função a ser utilizada: operator.mul (multiplicação)
print(list(itertools.accumulate(lista, operator.mul))) 
# Função a ser utilizada: operator.sub (subtração)
print(list(itertools.accumulate(lista, operator.sub))) 
# Função a ser utilizada: min
print(list(itertools.accumulate(lista, min))) 

Para entender, vamos pegar a primeira chamada itertools.accumulate(lista).

Sabemos que a função func será a operator.add (padrão) que recebe dois valores como parâmetro e os soma.

O que accumulate vai fazer, iteração à iteração, é:

Na primeira iteração, o acumulador se inicia em 0 e soma o primeiro elemento da lista de entrada, que no caso é 2.
Em seguida, o acumulador está com o valor 2, e soma o segundo elemento da lista, portanto 2 + 2 = 4.
Na última iteração, o acumulador está em 4 e recebe o valor 4 para ser somado, totalizando 8.
Dessa forma, a saída será a lista [2, 4, 8]
Também podemos definir funções e passar como o parâmetro func, da seguinte forma:

import itertools 

lista = [2, 2, 4] 

exponenciacao = lambda a, b: a ** b
    
print (list(itertools.accumulate(lista, exponenciacao)))
====================================================================================================================

FUNÇÃO CHAIN

Assinatura da função: chain(*iterables)

Como seu próprio nome sugere, sua função é encadear iteráveis.

Ela funciona esgotando os elementos do primeito iterável, seguindo para o próximo, esgotando-o e assim por diante.

Sua entrada permite um número variável de iteráveis.

import itertools 
  
lista = list([2, 2, 4] )
conjunto = set({1, 2, 3})
print(list(itertools.chain(lista, conjunto, range(5))))

"""
