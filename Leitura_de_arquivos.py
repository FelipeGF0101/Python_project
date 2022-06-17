"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open(), que literalmente significa 'abrir'.

open() -> A forma mais simples de utilização nós passamos apenas um parâmetro de entrada, que neste caso é o caminho do arquivo a ser lido.
Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

# OBS: Casa o encoding='cp1252' seja diferente de encoding='utf-8', basta fazer a alteração na hora de escrever o código.
EXEMPLOS: arquivo = open('palavras.txt', 'r', encoding='utf-8')

mode r -> Modo de leitura. r -> read() -> ler

========================================
arquivo = open('texto.txt')

print(arquivo)

print(type(arquivo))
========================================
"""
# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
# Exemplo

arquivo = open('texto.txt', 'r', encoding='utf-8')

print(arquivo.read())

# OBS: O python, utiliza um recurso para trabalhar com arquivos, chamado cursor. Esse cursor funciona como o cursor quando estamos escrevendo.
# OBS: A função read() lê todo o conteúdo do arquivo. 
