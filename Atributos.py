"""
POO - Atributos

Atributos -> Representam as características do objeto. Ou seja, pelos atributos nós conseguimos representar computacionalmente os estados de um objeto. 

Em python, dividimos os atributos em 3 grupos:
    - ATRIBUTOS DE INSTÂNCIA;
    - ATRIBUTOS DE CLASSE;
    - ATRIBUTOS DINÂMICOS.

# ATRIBUTOS DE INSTÂNCIA: SÃO ATRIBUTOS DECLARADOS DENTRO DO MÉTODO CONSTRUTOR

# OBS: MÉTODO CONSTRUTOR: É UM MÉTODO ESPECIAL UTILIZADO PARA A CONSTRUÇÃO DO OBJETO

EXEMPLO:
class Lampada:
    def __init__(self, voltagem, cor): # def '__init__ ' é o método construtor.
        self.__voltagem = votagem
        self.__cor = cor
        self.__ligada = False


# Em python, por convenção, ficou estabelecido que, todo atributo de uma classe é público, ou seja, pode ser acessado em todo o projeto.
# Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se duplo underscore no inicio de seu nome. Isso é conhecido também como Name Mangling.

# Atributos públicos

class Automovel:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Atributos privados (usa-se dupla underline no início do nome '__nome')
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    
    def mostra_senha(self): 
        print(self.__senha) # Fazendo acesso ao atributo dentro da própria classe.

    def mostra_email(self):
        print(self.email)

# OBS = Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe.

# Exemplo

user = Acesso('user@gmail.com', '123456')

print(user.email) # Resultado = user@gmail.com

# Forma incorreta de acessar atributo privado
# print(user.__senha) # AttibuteError

print(user._Acesso__senha) # Resultado = 123456 | Temos acesso. Mas não deveríamos fazer este acesso. (Name Mangling)

# Criando um método dentro da própria classe, é possível acessar o público e o privado.
Exemplo:
user.mostra_senha() 
user.mostra_email()

==========================================================================

# O QUE SIGNIFICA ATRIBUTOS DE INSTÂNCIA?
# SIGNIFICA QUE AO CRIARMOS INSTÂNCIAS/OBJETOS DE UMA CLASSE, TODAS AS INSTÂNCIAS TERÃO ESTES ATRIBUTOS.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

user1.mostra_email()
user2.mostra_email()

================================================================================

# Atributos de Classe

# Atributos de classe, são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

class Produto:
    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1 # Cada produto criado, (p1, p2) o contador recebe + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id # O atributo de classe 'contador' vai receber o valor de id.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

#print(p1.imposto) # -> .05
#print(p2.imposto) # -> .05

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python são chamados de atributos estáticos.

"""
# Classes com Atributo de Instância Público

class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome # O objeto Usuario, no atributo nome, receberá nome.
        self.email = email
        self.senha = senha


# Uma função fora da classe é chamada de função. Porém, estando dentro de uma classe, passa-se a chamar método.

# O PRIMEIRO PARÂMETRO DE UM MÉTODO É SEMPRE O SELF.
# Não é obrigatório o uso da palavra self, mas usa-se self por convenção dos usuários de python.

# Atributos públicos e Atributos privados
# Atributos de instância podem ser públicos ou privados

# Atributos públicos

class Automovel:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Atributos privados (usa-se dupla underline no início do nome '__nome')
class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha
    
    def mostra_senha(self): 
        print(self.__senha) # Fazendo acesso ao atributo dentro da própria classe.

    def mostra_email(self):
        print(self.email)

# Atributos de Classe

# Atributos de classe, são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja, ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os atributos de classe todas as instâncias terão o mesmo valor para este atributo.

class Produto:
    # Atributo de classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos
#   - Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg' # Note que na classe Produto não existe o atributo peso

print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor:.2f}, Peso: {p2.peso}.' )

# Deletando atributos
print(p1.__dict__) # {'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}  
print(p2.__dict__) # {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia', 'valor': 6.2895, 'peso': '5kg'}

del p2.peso
del p2.valor

print(p1.__dict__) # {'id': 1, 'nome': 'PlayStation 4', 'descricao': 'Video Game', 'valor': 2415.0}
print(p2.__dict__) # {'id': 2, 'nome': 'Arroz', 'descricao': 'Mercearia'}

"""
EXERCITANDO

class Automovel:
    def __init__(self, modelo, marca, cor, ano):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano

    def mostra_modelo(self):
        print(self.modelo)
    
    def mostra_marca(self):
        print(self.marca)
    
    def mostra_cor(self):
        print(self.cor)
    
    def mostra_ano(self):
        print(self.ano)

carro1 = Automovel('Tucson', 'Hyundai', 'Chumbo', '2015')

print(carro1.ano)

carro1.mostra_modelo()

carro1.mostra_marca()

carro1.mostra_cor()

carro1.mostra_ano()


class Livros:
    def __init__(self, nome, ano, N_paginas):
        self.__nome = nome
        self.__ano = ano
        self.__N_paginas = N_paginas

    def mostra_nome(self):
        print(self._Livros__nome)


infor = Livros('Algoritmos', '2020', '300')

infor.mostra_nome()

# Ou 

print(infor._Livros__N_paginas)
"""
