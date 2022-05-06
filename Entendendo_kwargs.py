'''
**Kwargs

Poderíamos chamar este parâmetro de **xis, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras em um dicionário.



# Exemplo

def cores_favoritas(**Kwargs):
    print(Kwargs)

cores_favoritas(marcos = 'verde', julia = 'amarelo', fernanda = 'azul', vanessa = 'branco')

# ====================================

def cores_favoritas(**Kwargs):
    for pessoa, cor in Kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}.')

cores_favoritas(marcos = 'verde', julia = 'amarelo', fernanda = 'azul', vanessa = 'branco')
cores_favoritas(felipe = 'preto')

============================================================
# Exemplo mais complexo

def cumprimento_especial(**Kwargs):
    if 'geek' in Kwargs and Kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in Kwargs:
        return f"{Kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem é você...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='oi'))
print(cumprimento_especial(geek='especial'))

========================================================


# Nas nossas funções podemos ter:
# - Parâmetros obrigatórios;
# *args;
# -Parâmetros defout (não obrigatórios);
# **Kwargs

def minha_funcao(idade, nome, *args, solteiro = False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro = True)
minha_funcao(34, 'Felipe', eu = 'Não', voce = 'Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java = False, puthon = True)

================================================================

# Entenda por quê é importante manter a ordem dos parâmetros na declaração
# Forma correta
def mostra_info(a, b, *args, instrutor = 'Geek', **Kwargs):
    return [a, b, args, instrutor, Kwargs]

print(mostra_info(1, 2, 3, sobrenome = 'University', cargo = 'instrutor'))

# Forma errada
def mostra_info(a, b, instrutor = 'Geek', *args, **Kwargs):
    return [a, b, args, instrutor, Kwargs]

print(mostra_info(1, 2, 3, sobrenome = 'University', cargo = 'instrutor'))

=====================================================================
# Desempacotar com **kwargs

def mostra_nomes(**Kwargs):
    return f"{Kwargs['nome']} {Kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(nome = 'Felicity', sobrenome = 'Jones'))

# OU

print(mostra_nomes(**nomes))

def meu_nome(**Kwargs):
   return f"{Kwargs['nome']} {Kwargs['sobrenome']}"

lista1 = {'nome':'Felipe', 'sobrenome':'Guedes'}

print(meu_nome(**lista1))
'''
def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
soma_multiplos_numeros(*lista)

# ========================================

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

 # Se estivermos trabalhando com lista, tupla, conjunto o *args consegue desempacotar.
 # Se formos trabalhar com dicionários, devemos usar o **Kwargs

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS: Os nomes das chaves em um dicionário devem ser os mesmos dos parâmetros da função.