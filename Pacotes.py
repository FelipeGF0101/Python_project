"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos;

Pacote -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py.
Nas versões do Python 3.x, não é mais obrigatória a utilização deste arquivo, mas normalmente ainda é utilizado para manter compatibilidade. 

# EXEMPLO DE UTILIZAÇÃO:

from exemplo_de_pacote import geek1, geek2
from exemplo_de_pacote.pacote2 import geek3, geek4

print(geek1.pi)

print(geek1.funcao1(4, 6))

print(geek2.curso)

print(geek2.funcao2())

print(geek3.funcao3())

print(geek4.funcao4())

"""
# UTILIZANDO APENAS UMA FUNÇÃO DO MÓDULO GEEK1

from exemplo_de_pacote.geek1 import funcao1
from exemplo_de_pacote.pacote2.geek4 import funcao4

print(funcao1(6, 9))

print(funcao4())