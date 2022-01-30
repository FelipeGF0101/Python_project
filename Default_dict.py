"""
Módulo collections - Default Dict

As regras dos dicionários se aplicam aqui também.

Recaptulando dicionários:
dicionario = {"curso": "Programação em python: Essencial"}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # Aqui é só pra relembrar que buscar por uma chave que não existe no dicionário
# gera keyError.

DEFAULT DICT = AO CRIAR UM DICIONÁRIO UTILIZANDO O DEFAULT DICT, NÓS INFORMAMOS UM VALOR DEFAULT, PODENDO UTILIZAR
UM LAMBDA PARA ISSO. ESTE VALOR SERÁ UTILIZADO SEMPRE QUE NÃO HOUVER UM VALOR DEFINIDO. CASO TENTEMOS UTILIZAR UMA
CHAVE QUE NÃO EXISTE, ESSA CHAVE SERÁ CRIADA E O VALOR DEFAULT SERÁ ATRIBUÍDO.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.

"""
# Fazendo o import

from collections import defaultdict

dicionario = defaultdict(lambda: 'Felipe')

dicionario["curso"] = "Programação em Python: Essencial"
print(dicionario)

print(dicionario["outro"]) # Buscar por uma chave que não existe no dicionário comum, retornaria keyError. Mas nesse
# caso, o valor será preenchido pelo lambda.

print(dicionario)
