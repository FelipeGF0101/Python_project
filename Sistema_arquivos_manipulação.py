"""
Sistema de Arquivos - Manipulação

import os

# Descobrindo se um arquivo ou diretório existe

# Pesquisando ARQUIVOS
print(os.path.exists('arquivo.txt')) # False
print(os.path.exists('texto.txt')) # True

# Pesquisando DIRETÓRIOS
# PATHS RELATIVOS
print(os.path.exists('nome da pasta')) # Se a pasta existir dentro deste diretório corrent, o retorno será True, se não, False.

# Pesquisando PATHS ABSOLUTOS
# Funciona para arquios e pastas
print(os.path.exists('c:\\Users\\yurif\\Desktop\\PROGRAMAÇÃO GERAL\\pythonProject\\'))

=======================

# Criando arquivos

# forma1
open('arquivo-teste.txt', 'w').close()

# forma2
open('arquivo-teste2.txt', 'a').close()

# forma3
with open('arquivo-teste3.txt', 'w') as arquivo:
    pass # encerra o bloco

# Não funciona mais no windows
os.mknod('arquivo-teste4.txt')

===============================
# Criando diretórios - (de um em um)

os.mkdir('templates')

# OBS: A função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistsError
# É possível criar o diretório passando todo o caminho até o local de criação.

======================================
# É Possível criar mais de um diretório por vez
os.makedirs('nome do diretório\\nomedodiretório') # É possível criar passando o caminho 

# Tratando erro
os.makedirs('nome do diretório', exist_ok=True) # Crie os diretórios. Se já existirem diretórios de mesmo nome, apenas ignore, não apresente erro.

======================================

# Renomeando arquivos e diretórios

# os.rename('nome do diretório', 'novo nome do diretório')
# OBS: Se o diretório não existir teremos um FileNotFoundError

# OBS: Se o diretório que queremos renomear não estiver vazio, teremos um OSError

# Para alterar o nome de um arquivo dentro de um diretório, temos que passar o caminho quando informamos qual é o arquivo a ser renomeado e outra vez informando qual o novo nome do arquivo.

os.rename('c:\\Users\\yurif\\Desktop\\PROGRAMAÇÃO GERAL\\pythonProject\\teste1\\teste1.txt', 'c:\\Users\\yurif\\Desktop\\PROGRAMAÇÃO GERAL\\pythonProject\\teste1\\testando5.txt')

==================================================
# DELETANDO UM ARQUIVO

# ATENÇÃO! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo oudiretório, eles não vão para a lixeira, eles somem.

os.remove('texto.txt')

# OBS: Se você estiver no windows e o arquivo que você for deletar estiver em uso, você terá um erro.

# OBS: Caso o arquio não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um IsADirectoryError

=================================================
# Remoendo diretórios

os.rmdir('nome do diretório')
# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError
# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma àrvore de diretórios
for arquivo in os.scandir('nome do diretório'):
    print(f'{arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

# Podemos remover uma árvore de diretórios vazios

# os.removedirs('caminho do(s) diretório(s)')
# Se algum dos diretórios contiver arquivos ou outros diretórios, o processo para.
# ATENÇÃO: Ao remover arquivos e diretórios com Python eles não vão para a lixeira. Eles vão embora.

from send2trash import send2trash
os.remove('novoarquivo.txt') # Não vai para a lixeira. É deletado imediatamente

send2trash('NovoTexto.txt') # Vai para lixeira. Pode ser restaurado
# Se o arquivo não existir, teremos OSError.
# O send2trash envia para lixeira arquivos e diretórios

============================================

# Trabalhando com arquivos e diretórios temporários
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporário.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()
# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele criando um arquivo para escrevermos um texto. No final, usamos um input() só para mantermos os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver utilizando o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos temporários.

==========================================
import os
import tempfile

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários, só conseguimos escrever bits. Por isso, utilizamos b

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""


