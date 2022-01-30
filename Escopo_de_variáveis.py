"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende todo o programa.

2 - Variáveis Locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado no bloco onde foi declarada.

Variável:
    - Para declarar uma variável em Python:
        - nome_da_variável = valor_da_variável

Python é uma linguagem de tipagem dinâmica, ou seja, quando declaramos uma variável em Python, nós não fazemos a
declaração do tipo de dado desta.
Esta tipagem da variável é feita quando atribuimos valor à ela.

Em outras linguagens, como C e Java, é necessário fazer a atribuição de tipo, conforme exemplo abaixo:
Em C:
int numero = 40
(Em python 'float')real numero = 40.02

Em Java:
int numero = 40
(Em puthon 'float')real numero = 40.02

"""
# Exemplificando a uma variável:

numero = 430
print(numero)

# Para mostrar o tipo de variável, basta usar o comando 'type'.

numero = 430
print(type(numero))

# O resultado: 430 <class 'int'> (inteiro)

numero = 49.04 # Exemplo de variável Global.
print(type(numero))

# Abaixo um exemplo de variável local:

numero = 5
if numero > 10:
    novo = numero + 10
else:
    numero < 10
    novo = numero - 20
print(novo)

# Neste caso, a variável - numero = 5 - serviu apenas neste bloco.




