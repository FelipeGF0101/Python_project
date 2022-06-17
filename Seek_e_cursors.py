"""
Seek e Cursors

seek() -> É utilizada para movimentar o cursor pelo arquivo.

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

# Movimentando o cursor pelo arquivo com a função seek():
# seek() -> A função seek() é utilizada para movimentação do cursor pelo arquivo. Ela recebe um 
# parâmetro que indica onde queremos colocar o cursor.

arquivo.seek(0)
print(arquivo.read())

arquivo.seek(21)
print(arquivo.read())
==========================================================

# readline() -> Função que lê o arquivo linha a linha

retorno = arquivo.readline()

print(type(retorno))

print(retorno)

print(retorno.split(' '))

=============================================================

# READLINES()

print(arquivo.readlines())
print()
print(len(arquivo.readlines())) # Usando a função len() com a readlines() podemos obter o número de linhas do documento de texto

# Outra forma de se obter o número de linhas

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador
e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão. Para isso, utilizamos a função close().

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;

2 - Trabalhar o arquivo;

3 - Fechar o arquivo.

# 1 - Abrir o arquivo
arquivo = open('texto.txt', encoding='utf-8')

# 2 - Trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed) # O closed vai verificar se o arquivo está aberto ou fechado. Nesse caso, retornará False, pois não foi dado nenhum comando para que o arquivo fosse fechado.

# 3 - Fechar o arquivo
arquivo.close() # O close() é responsável por fechar o arquivo.

print(arquivo.closed) # Aqui o closed retornará True, pois antes, usamos o close() para fechar o arquivo.

# OBS: Se tentarmos manipular um arquivo após seu fechamento, teremos um ValueError. 

"""
arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read(100)) # Com a função read() podemos limitar a quantidade de informação mostrada.