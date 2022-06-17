"""
Escrevendo em arquivos 

# OBS: Ao abrir um arquivo para leitura não podemos realizar a escrita nele, apenas ler. 
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo.

# Exemplo de escrita

with open('NovoTexto.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quanas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

# Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
# Esta função recebe uma string como parâmetro, caso contrário, teremos TypeError.

# OBS: Ao abrir um arquivo para escrita, o arquio é criado no sistema operacional.

# OBS: ABRINDO UM ARQUIVO PARA ESCRITA COM O MODO 'W', SE O ARQUIVO NÃO EXISTIR, ELE SERÁ CRIADO, CASO ELE JÁ EXISTA,
O ANTERIOR SERÁ APAGADO E UM NOVO SERÁ CRIADO. DESSA FORMA, TODO O CONTEÚDO NO ARQUIO ANTERIOR É PERDIDO.

========================================================

# Exemplo de escrita
# Forma Paythonica

with open('NovoTexto.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quanas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

# Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
# Esta função recebe uma string como parâmetro, caso contrário, teremos TypeError.

# OBS: Ao abrir um arquivo para escrita, o arquio é criado no sistema operacional.

# Forma tradicional de escrita em arquivo (Não paythonica)
arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer. \n')
arquivo.write('Mais um texto.')

arquivo.close()

===========================================================

with open ('geek.txt', 'w') as arquivo:
    arquivo.write('Geek' * 1000)

"""
with open ('frutas.txt', 'w', encoding="utf-8") as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite "sair": ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break