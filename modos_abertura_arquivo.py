"""
Modos de abertura de arquivo

r -> Abre o arquivo para leitura - padrão
w -> Abre o arquivo para escrita - sobrecreve caso o arquivo já exista
x -> Abre o arquivo para criação exclusiva, falhando se o arquivo já existe
a -> Abre o arquivo para escrita, anexando ao final do arquio se ele existir
b -> modo binário
t -> modo de texto (padrão)
+ -> aberto para atualização (leitura e escrita)

http://docs.python.org/3/library/functions.html#open

===================================================

# Utilizando o 'x'

with open('novoarquivo.txt', 'x', encoding='utf-8') as arquivo:
    arquivo.write('Testando o x.\n')
    arquivo.write('Colocando mais informação')

# Utilizando o 'x' com tratamento de erros

try:
    with open('novoarquivo.txt', 'x') as arquivo:
        arquivo.write('Teste de conteúdo 2 \n')
except FileExistsError:
    print('Arquivo já existe')

==============================================

# Utilizando o 'a'

with open('novoarquivo.txt', 'a', encoding='utf-8') as arquivo:
    while True:
        informacao = input('Insira novas informações: ')
        if informacao != 'sair':
            arquivo.write(informacao)
            arquivo.write('\n')
        else:
            break

with open('novoarquivo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.seek(0)
    arquivo.write('\n')
    arquivo.write('No topo. \n')

# OBS: Com o modo 'a' nós não controlamos o cursor.
"""
with open('novoarquivo.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Testando um novo início \n')
    arquivo.write('Testando aqui em cima. \n ')
    arquivo.write('No topo do mundo. \n')
    arquivo.write('No topo. \n')
    arquivo.write('Meu nome é Felipe. \n')
    arquivo.write('Lá embaixo.\n')
    arquivo.write('Testando sem o + \n')


