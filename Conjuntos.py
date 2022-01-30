"""
Conjuntos

- Quando falamos em conjuntos, estamos fazendo referências à Teoria dos conjuntos da matemática.

- Aqui em Python, os conjuntos são chamados de sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice. Ou seja, conjuntos não são indexados.

-> Conjuntos são bons para se armazenar elementos mas não nos importamos com a ordenação deles.
Quando não precisamos nos preocupar com as chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (set) e mapas (dicionários) em Python:

- Um dicionário tem chave/valor;
- Um conjunto tem apenas valor.

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Neste conjunto existem valores repetidos.

print(s)
print(type(s))
# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar error e não fará parte do conjunto.

# Forma 2 (mais comum)

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# É possível transformar uma string em conjunto(set)
# Por exemplo:
# nome = ("Felipe Guedes")
# print(set(nome)
# {'d', 'i', 'F', 'G', 'p', 'e', 's', ' ', 'l', 'u'}

# É possível transformar um lista em set (conjunto)
# Por exemplo:
# lista = [1, 2, 2, 3, 5, 4, 4, 6]
# print(lista)
# print(set(lista))
# {1, 2, 3, 4, 5, 6}

# É possível transformar uma tupla em set(conjunto)
# Por exemplo:
# num = (1, 2, 3, 4, 5, 6, 5, 6, 7)
# print(num)
# print(set(num))

# PODEMOS VERIFICAR SE DETERMINADO ITEM ESTÁ NO CONJUNTO:

if 3 in s:
    print("O número três está contido no conjunto.")
else:
    print("O número três não está contido no conjunto.")
===========================================================

# Importante lembrar que, além de não termos valores duplicados, não temos ordem.

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'lista:{lista} com {len(lista)} elementos')

#
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionário:{dicionario} com {len(dicionario)} elementos')

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'conjunto:{conjunto} com {len(conjunto)} elementos')
=======================================================================
# Assim como todo outro conjunto python podemos colocar tipos de dados misturados em sets.

s ={1, "b", True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
=======================================================================
# Uso interessante com sets:

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu, e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter
# repetição.

cidades = ["Belo horizonte", "São paulo", "Campo grande", "Cuiabá", "Campo grande", "São paulo", "Cuiabá"]

print(cidades)
print(len(cidades))
# Aqui sabemos o número total de visitantes = 7

# Agora precisamos saber o número de cidades únicas

print(len(set(cidades)))
# São um total de 4 cidades únicas.

=========================================================================

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade não gera erro. Simplesmente é ignorado e não adicionado ao conjunto.
print(s)

# Conjuntos são mutáveis, pois aceitam a adição de valores posteriores.

# Removendo valor do conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # Não é índice! Conjuntos não são indexados.
print(s)

# OBS: caso o valor não exista no conjunto, retornará KeyError

# Forma 2

s.discard(2)
print(s)
# Se o valor não for encontrado, nenhum erro é gerado.

====================================================================
# Copiando um conjunto para outro
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Quando usamos o deep copy, nós criamos dois objetos totalmente separados e independentes.

=========================================================================

# Copiando um conjunto para outro
s = {1, 2, 3}

# Forma 2 - Shallow Copy

novo = (s)

novo.add(4)

print(novo)
print(s)

# Quando utilizamos o shallow copy, os conjuntos assumem os mesmos valores.

=======================================================================
s = {1, 2, 3}
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)
=======================================================================

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um formado por estudantes do curso de Python
# e o outro formado por estudantes de Java.

estudantes_python = {" Marcos", "Patrícia", "Ellen", "Pedro", "Júlia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Júlia", "Ana"}

print(estudantes_python)
print(estudantes_java)
# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
unicos2 = estudantes_java.union(estudantes_python)
print(unicos2)

# Forma 2 - Utilizando o caractere pipe |

unicos3 = estudantes_python | estudantes_java
print(unicos3)
===========================================================================
# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um formado por estudantes do curso de Python
# e o outro formado por estudantes de Java.

estudantes_python = {" Marcos", "Patrícia", "Ellen", "Pedro", "Júlia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Júlia", "Ana"}

# Precisamos gerar um conjunto com estudantes que estão em ambos os cursos

# Forma 1 - Utilizando o intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

=================================================================
# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um formado por estudantes do curso de Python
# e o outro formado por estudantes de Java.

estudantes_python = {" Marcos", "Patrícia", "Ellen", "Pedro", "Júlia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Júlia", "Ana"}

# Gerando um conjunto de estudantes que não estejam nos dois cursos

# UTILIZANDO DIFFERENCE

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
===================================================================

# * Soma, Valor max *, valor min *, tamanho

# * Somente se todos os valores forem inteiros ou reais

s = {1, 2, 3, 4, 5, 6, 7, 8}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

Símbolo matemático  	Operador Python	    Descrição
    e∈S	                     in            elemento e é membro de S
    A⊆B	                     <=            A é um subconjunto de B
    A⊂B                      <             A é um subconjunto próprio de B
    A∪B	                     |             A união com B
    A∩B	                     &             A interseção com B
    A∖B	                     -             diferença entre A e B


"""