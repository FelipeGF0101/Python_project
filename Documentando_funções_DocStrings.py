'''
Documentando funções com DocStrings

OBS: Podenos ter acesso à documentação de um função em python utilizando a propriedade especial .__doc__
- Podemos ainda fazer acesso à documentação com a função help()

def diz_oi():
    """Uma função simples que retorna a string 'Oi!"""
    return 'Oi!'
print(diz_oi())

#print(help(diz_oi))

print(diz_oi.__doc__)
'''


def exponencial(numero, potencia = 2):
    """
    Função que retorna por padrão o quadrado de 'número' ou 'número' à 'potência' informada
    parametro número: Número que desejamos gerar o exponencial
    parametro potencia: Potência que queremor gerar o exponencial. Por padrão é 2
    return: Retorna o exponencial de 'número' por 'potência'
    """
    return numero ** potencia

print(exponencial(3))

print(exponencial.__doc__)
