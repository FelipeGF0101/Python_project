"""
Mapas = conhecidos em python como dicionários.

Dicionários em python são representados por chaves {}

receita = {'jan': 100, 'fev': 150, 'mar': 200}

# Interando sobre receita

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} : recebi R$: {receita[chave]}')

# Forma recomendável
# Acessando as chaves

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#Forma recomendada
# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')


receita = {'jan': 100, 'fev': 150, 'mar': 200}

# Soma*, valor máximo*, valor mínimo*, tamanho
# * Se o valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""





