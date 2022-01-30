"""
DICIONÁRIOS:
OBS: Em algumas linguagens de programação, os dicionários python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por cgaves {}.
print(type({}))

OBS: Sobre dicionários
 - Chave e valor são separados por dois pontos > 'chave:valor'
 - Tanto a chave quanto valor podem ser de qualquer tipo de dado.
 - Podemos misturar tipos de dados.

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(BR='Brasil', EUA='Estados Unidos', PY='Paraguai')
# A segunda forma transforma os parênteses em chaves
print(paises)
print(type(paises))

================================================================
# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que a lista/tupla
print(paises['BR'])
print(paises['PY'])

#print(paises['ru'])
# OBS: CASO TENTARMOS FAZER UM ACESSO UTILIZANDO UMA CHAVE INEXISTENTE, RETORNARÁ ERRO.

# Forma 2 - Acessando via get - Recomendada

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado keyerror.
print(paises.get('BR'))
print(paises.get('EUA'))
# print(paises.get('RU'))
# Quando declaramos uma chave inexistente, temos como retorno o tipo de dado none.

=========================================================================
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

pais = (paises.get('py'))

if pais:
    print(f'Encontrei o país {pais}') # Aqui encontra-se o Paraguai.
else:
    print('Não encontrei o país')
==========================================================================
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

pais = (paises.get('ru')) # Aqui resulta em ' Não encontrei o país '

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')

==========================================================================
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

pais = (paises.get('ru', 'Não encontrado')) # Neste caso, resulta em 'Encontrei o país Não encontrado'.
# Dessa forma, o tipo None sempre terá um valor.

print(f'Encontrei o país {pais}')
==========================================================================
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

# Podemos definir um valor para caso não encontrarmos o objeto com a chave informada.
pais = (paises.get('PY', 'Não encontrado')) # Neste caso, resulta em 'Encontrei o país Paraguai
# Se o código encontra o valor da chave no dict (dicionário), o valor aqui declarado não é usado.

print(f'Encontrei o país {pais}')
=========================================================================
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'PY': 'Paraguai'}

print('br' in paises) # Quando buscamos pelo nome da chave, este deve ser exatamente igual ao que consta no
# dicionário (dict). Exemplo: {'BR':Brasil} a busca deve ser por ('BR') e não por ('br')
print('ru' in paises) # Quando a chave é inexistente no dicionário, o resultado é false.
print('Estados unidos' in paises) # A busca em dicionários só é feita pela chave e não pelo valor.
# Por exemplo: paises = {'EUA': 'Estados Unidos'} a busca deve ser: print('EUA' in paises).
==========================================================================

# PODEMOS UTILIZAR QUALQUER TIPO DE DADO (INT, FLOAT, STRING, BOOLEAN), INCLUSIVE LISTA, TUPLA, DICIONÁRIO, CCOMO CHAVE
# DE DICIONÁRIO.

localidades = {
    (00.0000, 00.0000): 'Escritório em Tókyo',
    (11.1111, 11.1111): 'Escritório em Nova York',
    (22.2222, 22.2222): 'Escritório em São Paulo',
}
# Tuplas são bastante interessantes de serem utilizadas como chaves de dicionários, pois as mesmas são imutáveis.

print(localidades)
print(type(localidades))

=======================================================================
# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))
print(receita['jan'])

# Forma 1 - Forma mais comum

receita['abr'] = 350
print(receita)

receita['mai'] = 400
print(receita)

# Forma 2

novo_dado = {'jun': 450}
receita.update(novo_dado)
print(receita)

novos_dados = {'jul': 500, 'ago': 550, 'set': 600} # Receita.update({'jul':500}) Teria o mesmo efeito.
receita.update(novos_dados)
print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['set'] = 650
print(receita)

# Forma 2

receita.update({'ago': 600})
print(receita)

# CONCLUSÃO1: A forma de adicionar novos elementos ou atualizar dados é a mesma.
# CONCLUSÃO2: Em dicionários, NÃO podemos ter chaves repetidas.
====================================================

# Como remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# Forma1

ret = receita.pop('mar')
print(ret)

print(receita)
# OBS1: Aqui precisamos SEMPRE informar a chave, e caso não encontre o elemento, um KeyError é retornado.
# OBS2: Ao removermos um objeto, o valor desse objeto é sempre retornado.

# Forma2

del receita['fev']
print(receita)

# Se a chave não existir, será gerado um keyerror.
# Obs: neste caso o valor removido não é retornado
==========================================================

# Utilidade do uso dos dicionários
# Imagine que você tem o ecomerce, onde temos um carrinho de compras na qual adicionamos produtos.


Carrinho de compras:
    Produto 1:
        - Nome:
        - Quantidade:
        - Valor:

    Produto 2:
        - Nome:
        - Quantidade:
        - Valor:

# Exemplos:
# 1 - Poderíamos utilizar Listas para isso? Sim

carrinho = []

produto1 = ['play station 4', 1, 2300.00]
produto2 = ['God of War', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Neste caso, teríamos que saber qual é o índice de cada informação do produto.

# 2 - Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('play station 4', 1, 2300.00)
produto2 = ('play station 4', 1, 150.00)

carinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação do produto.

# Poderíamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'Nome': 'Play station 4', 'Quantidade': 1, 'Valor': 2300.00}
produto2 = {'Nome': 'God Of War', 'Quantidade': 1, 'Valor': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza em cada informação.
==================================================================
# Métodos de dicionários

d =dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Esse método retorna: {'a':1, 'b':2, 'c':3}

# como limpar um dicionário (limpar dados):

d.clear()
print(d)

# Copiando um dicionário para outro:
# Forma 1

novo = d.copy() # Copia os dados do dicionário para 'novo'.
print(novo)

novo['d'] = 4
print(novo)
======================================================


# Métodos de dicionários

d =dict(a=1, b=2, c=3)
print(d)
print(type(d))

# Copiando um dicionário para outro:

# Forma2 >> Shalow copy <<

novo = d
print(novo)

novo['d'] = 4
print(d)
print(novo)
=====================================================================

# Forma não usual de criar dicionários:

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['Nome', 'Pontos', 'Email', 'Profile'],'Desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir para cada chave o valor informado.

valor = {}.fromkeys('teste', 'letra')
print(valor)
print(type(valor))

num = {}.fromkeys(range(1, 11),'numero')
print(num)

"""