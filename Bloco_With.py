"""
Bloco With

Passos para se trabalhar com arquivos

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos utilizados são fechados após o bloco with.

"""

# O block with

with open('texto.txt') as arquivo:
    print(arquivo.readlines())

# O próprio with abre e fecha o arquivo. É como uma função que executa determinado procedimento e o encerra ao final.

# Outro exemplo:

with open('texto.txt') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed) # Resposta: FALSE

# Executando o mesmo comando fora do bloco
print(arquivo.closed)
# Resposta: TRUE