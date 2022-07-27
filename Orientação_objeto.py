"""
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza mapeamento de objetos do mundo real para modelos computacionais

- Paradigma de programação é a forma/metodologia utilizada para pensar/desenvolver sistemas.

Principais elementos da Orientação a objetos:
- > Classe -> Modelo do objeto do mundo real sendo representado computacionalmente;
-> Atributo -> Características do objeto;
-> Método -> Comportamento do objeto (funções)
-> Construtor -> Método especial utilizado para criar os objetos;
-> Objeto -> Instância da classe.

"""

class Produto:
    pass

ps4 = Produto() # Esse "Produto()" é conhecido como construtor. É o método construtor da classe produto.
# O ps4 é um objeto da classe produto.
print(ps4)
print(type(ps4))