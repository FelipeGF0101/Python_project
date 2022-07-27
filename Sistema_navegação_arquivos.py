'''
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer uso do módulo os.
os -> Operating System - Sistema operacional

================================================================

# Fazer o import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
print(os.getcwd()) # Retorna o path (caminho) absoluto

# Para mudar o diretório, podemos utilizar o chdir() -> Volta um diretório, é como o comando (cd ..)
os.chdir('..')

print(os.getcwd())

===================================================================
# Fazer o import
import os

# Podemos checar se um diretório é absoluto ou relativo
# print(os.path.isabs('caminho de diretórios'))

# OBS: para usuários Windows
# Se você estiver utilizando um computador com windows, terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('c:\\')) # No windows deve ser usado dupla barra \\

============================================================
# Fazer o import
import os

# Podemos identificar o sistema operacional com o módulo os:
print(os.name) # nt (windows)

# Podemos ter mais detalhes no sistema operacional
#print(os.uname()) # Esse comando funciona no posix (linux e Mac)

# Não temos essa função no windows

================================================
OBS: ESSES COMANDOS NÃO DERAM CERTO PRA MIM

# Fazer o import
import os

# Criando e mudando diretórios
print(os.getcwd()) # C:\Users\yurif\Desktop\PROGRAMAÇÃO GERAL\pythonProject

# os.path.join(os.getcwd(), 'pastateste') # Criando uma pasta
res = os.path.join(os.getcwd(), 'pastateste') # Criando uma pasta
os.chdir(res)

print(os.getcwd())

===========================================================
# Podemos listar os arquivos e diretórios com o listdir()
print(os.listdir('nome do diretório'))

# Podemos listar arquivos e diretórios com mais detalhes com scandir()

print(os.scandir('nome do diretório'))

# Outra forma

arquivos = list(os.scandir())

print(arquios)

print(arquios[0].name)

============================================

print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)
print(arquivos[0].path)
print(arquivos[0].stat())

# OBS: Quando utilizamos a função scandir() nós precisamos fechá-la, assim quando abrimos um arquivo

scanner.close()
'''
