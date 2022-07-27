"""
Decoradores (Decorators)

O que são decorators?
- São funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators também são exemplos de Higher Order Functions;
- Decoratos tem uma sintaxe própria, usando "@" (Syntact Sugar / Açúcar Sintático)

# Decorators como funções (Sintaxe não recomendada / Sem açúcar Sintático)

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 1

teste = seja_educado(saudacao)

teste()

=======================================
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo

def saudacao():
    print('Seja bem-vindo(a) à Geek University')

# Testando 2

def raiva():
    print('EU TE ODEIO!')

raiva_educada = seja_educado(raiva)
raiva_educada()

==================================================

# Decorators com Syntax Sugar (açúcar sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')

apresentando()

"""


