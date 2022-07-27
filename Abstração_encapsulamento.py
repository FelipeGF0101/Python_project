"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> Cápsula

                classe
------------------------------------
/                                   /
/       atributos e métodos         /
/-----------------------------------/

# Relembrando Atributos/Métodos privados em Python.

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado chamado __nome e um método privado 
chamado __falar()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas Python não bloqueia este acesso fora da classe. Com python acontece um fenômeno chamado Name Mangling, que faz uma alteração na forma 
de se acessar os elementos privados, conforme:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instância._Pessoa__nome
instância._Pessoa__falar()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados de usuário.

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor

 
# Testando

-> Caso os atributos da classe fossem públicos, eu poderia acessá-los da seguinte maneira:

print(conta1) # <__main__.Conta object at 0x0000028EF82AFD60>

print(conta1.numero) # 400
print(conta1.titular) # Geek
print(conta1.saldo) # 150.00
print(conta1.limite) # 1500

# Problema
# Criando a conta com acesso público, a gente não somente consegue fazer a leitura dos dados, mas também consegue fazer alteração nos dados.
# Por exemplo:
-> Se eu quisesse alterá-los

conta1.numero = 42
conta1.titular = 'Felipe'
conta1.saldo = 999999999
conta1.limite = 8888888888

==============================================

conta1 = Conta('Geek', 150.00, 1500)

print(conta1.__dict__)

conta1.extrato()

# Mesmo estando privado, eu ainda poderia fazer acesso:
print(conta1._Conta__titular) # Name Mangling (mas essa forma é errada)

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__) # {'_Conta__numero': 400, '_Conta__titular': 'Angelina', '_Conta__saldo': 150.0, '_Conta__limite': 1500}

====================================================
# Testando 
conta1 = Conta('Geek', 150.00, 1500)

print(conta1.__dict__) # {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 150.0, '_Conta__limite': 1500}

conta1.depositar(150)

print(conta1.__dict__) # {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 300.0, '_Conta__limite': 1500}

conta1.sacar(50)

print(conta1.__dict__) # {'_Conta__numero': 400, '_Conta__titular': 'Geek', '_Conta__saldo': 250.0, '_Conta__limite': 1500}

# =====================================================

"""
# POSSÍVEIS ERROS

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')
    
    def depositar(self, valor):
        if self.__saldo < 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente.')
        else:
            print('O valor deve ser positivo.')
        
    def transferir(self, valor, conta_destino):
        if valor > 0:
            if self.__saldo < valor:
                print('Saldo insuficiente!')
            else:
        # 1 - Remover o valor da conta de origem.
                self.__saldo -= valor
                self.__saldo -= 10 # Taxa de transferência para por quem realizou a transferência.
        # 2 - Adicionar o valor na conta de destino
                conta_destino.__saldo += valor
        else:
            print('O valor precisa ser positivo!')

conta2 = Conta('Felipe', 200.0, 1500)

print(conta2.__dict__)

conta2.depositar(-50) # O valor precisa ser positivo

print(conta2.__dict__)

conta2.sacar(100)

print(conta2.__dict__)

print()

conta2 = Conta('Felipe', 200, 1500)
conta2.extrato()

conta3 = Conta('Yuri', 400, 3000)
conta3.extrato()

print()

conta3.transferir(100, conta2)
conta2.extrato()
conta3.extrato()