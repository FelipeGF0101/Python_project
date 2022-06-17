import primeiro

def funcao2():
    primeiro.funcao1()

if __name__ == '__main__':
    funcao2()
    print('Segundo.py está sendo executado diretamente')
else:
    print('Segundo.py foi importado')