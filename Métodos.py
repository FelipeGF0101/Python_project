"""
POO - Métodos

- Métodos (funções) -> Repesentam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de Classe.

"""
# Métodos de Instância

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:

    contador = 4999 # Atributo de classe

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    
    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100 

p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(20)) # Desconto de 20%

print(Produto.desconto(p1, 40)) # self, desconto

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', ' Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f'Senha User1: {user1._Usuario__senha}') # Acesso de forma errada de um atibuto de classe.

# INCORRETO    
#    def __correr__(self, metros): # Não é recomendado criar nomes de métodos usando dunder. Métodos dunder são internos da linguagem python.
#        print(f'{self.__nome} está correndo {metros} metros.')

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.

# Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

# OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

# ATENÇÃO! Por mais que possamos criar nossar próprias funções utilizando dunder (underline no início e no fim) não é aconselhado. Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas internas das linguagem. Então, evite ao máximo. De preferência nunca o faça.

# Métodos são escritos em etras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.
 
# UTILIZANDO UM ENCRIPITADOR DE SENHAS
print()
from passlib.hash import pbkdf2_sha256 as cryp

class Utilizador:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 200000, salt_size = 16)

    def nome_inteiro(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Utilizador(nome, sobrenome, email, senha)
else:
    print('Senha não confere...')
    exit(42)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Utilizador__senha}') # Acesso errado.

print()

# ===============================================================

# MÉTODOS DE CLASSE
# Métodos de Classe em Python, são conhecidos como Métodos Estáticos em outras linguagens.

class Fulano:

    contador = 0

    @classmethod
    def conta_fulano(cls):
        print(f'Classe{cls}')
        print(f' Temos {cls.contador} usuário(s) no sistema.')

    @classmethod
    def ver(self):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Fulano.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 20000, salt_size = 16)
        Fulano.contador = self.__id

    def nome_completo1(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha1(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

user = Fulano('Felipe', 'Guedes', 'felipe@gmail.com', '12345')

Fulano.conta_fulano() # forma correta / Utilizamos o nome da classe mais o nome do método.
user.conta_fulano() # forma incorreta

# MÉTODOS PRIVADOS

print()

class Fulano1:

    contador = 0

    @classmethod
    def conta_fulano(cls):
        print(f'Classe{cls}')
        print(f' Temos {cls.contador} usuário(s) no sistema.')

    @classmethod
    def ver(self):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Fulano1.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 20000, salt_size = 16)
        Fulano1.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario}')

    def nome_completo1(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha1(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Fulano1('Felicity', 'jones', 'felicity@gmail.com', '1234')

print(user._Fulano1__gera_usuario()) # Acesso, de forma ruim...

print()

# MÉTODO ESTÁTICO

class Fulano2:

    contador = 0

    @classmethod
    def conta_fulano(cls):
        print(f'Classe{cls}')
        print(f' Temos {cls.contador} usuário(s) no sistema.')

    @classmethod
    def ver(self):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Fulano2.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds = 20000, salt_size = 16)
        Fulano2.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario}')

    def nome_completo1(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha1(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]

print(Fulano2.contador)

print(Fulano2.definicao())

fula2 = Fulano2('Felicity', 'jones', 'felicity@gmail.com', '1234')

print(fula2.contador)

print(user.definicao())

# PRATICANDO 

class Pessoa:

    contador = 0

    def __init__(self, nome, sobrenome, idade):
        self.__id = Pessoa.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        Pessoa.contador = self.__id
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
pes1 = Pessoa('Felipe', 'Guedes', '31')

print(pes1.__dict__)

print(Pessoa.nome_completo(pes1))