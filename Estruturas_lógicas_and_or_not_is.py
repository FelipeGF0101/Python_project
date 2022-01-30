"""
Estruturas lógicas: and(e), or(ou), not(não), is(é).

- Operadores Unários: not, is;
- Operadores binários: and, or.

REGRAS DE FUNCIONAMENTO:

Para o 'and'(e), todos os valores precisam ser TRUE (verdadeiro).
Para o 'or'(ou), um ou outro valor precisa ser TRUE (verdadeiro).
Para o 'not'(não), o valor do booleano é invertido, ou seja, se for True, vira False; se for False, vira True.
O not possui propriedade de negação.
Para o 'is'(é), o valor é comparado com outro.

OPERADORES LÓGICOS:
CONSIDERE QUE A VARIÁVEL A CONTÉM O VALOR TRUE(VERDADEIRO
E A VARIÁVEL B CONTÉM FALSE(FALSO)
EXEMPLO:
(A AND B) É FALSE
(A OR B) É TRUE
NOT(A AND B) É TRUE

OPERADORES RELACIONAIS:
OPERADOR DESCRIÇÃO
==          IGUAL
!=          NÃO IGUAL
>           MAIOR QUE
<           MENOR QUE
>=          MAIOR OU IGUAL QUE
<=          MENOR OU IGUAL QUE

EXEMPLO:
Considere que a variável A contém o valor 10 e a variável B contém 20.
(A == B) é False
(A != B) é True
(A > B) é False
(A < B) é True
(A >= B) é False
(A <= B) é True

"""
"""
EXEMPLO 1:

Ativo = True
Logado = False

nome = input("Qual o seu nome?\n")

if Ativo or Logado:
    print("Bem vindo!",nome,)
else:
    print(nome,", você não confirmou o seu e-mail. Por favor, abra seu e-mail e confirme sua conta!")
"""
Ativo = True
Logado = False

# Se não estiver ativo:
if not Ativo:
    print('Você precisa ativdar sua conta! Por favor cheque o seu e-mail.')
else:
    print('Seja Bem Vindo!')