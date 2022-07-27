"""
StringIO

ATENÇÃO: PARA LER OU ESCREVER DADOS EM ARQUIVOS DO SISTEMA OPERACIONAL O SOFTWARE PRECISA TER PERMISSÃO:
- PERMISSÃO DE LEITURA
- PERMISSÃO DE ESCRITA

StringIO -> Utilizado para ler e criar arquivos em memória.

"""
# Para utilizar o stringIo é preciso fazer o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio para inserirmos texto depois.
arquivo = StringIO(mensagem) # É equivalente a arquivo = open('arquivo.txt', 'w')

# Agora, tendo o arquivo, podemos utilizar tudo que já sabemos.
print(arquivo.read())

# Escrevendo outros textos
arquivo.write('Outro texto')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())