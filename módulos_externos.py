"""
Módulos externos

Utilizamos o gerenciador de pacotes Python chamao Pip_ Python Installer Package

Você pode conhecer todos os pacotes externos oficiais: https://pypi.org

Colorama -> É utilizado para permitir impressão de textos coloridos no terminal

# Instalando o pacote colorama
# Utilizando o pacote instalado
from colorama import Back, init, Fore, colorama_text
from sqlalchemy import ForeignKey

init()
print(Fore.MAGENTA + 'Meu nome é Felipe Guedes')
print('Meu nome é Pietro Balieiro')

"""
import pydf

pdf = pydf.generate_pdf('<h1>Felipe Guedes<h1>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
