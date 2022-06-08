'''
Levantando os próprios erros com raise

raise -> Lança exceções

OBS: O Raise não é uma função. É uma palavra reservada, assim como def ou qualquer outra em python.

Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de erro')


#raise ValueError('Valor incorreto')

''' 

# Exemplo real

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')

colore('Geek', 'azul')

# OBS -> O raise, assim como o return, finaliza a função, ou seja, nada após o raise é executável.

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if not cor in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')
    
print(colore('Felipe', 'preto'))