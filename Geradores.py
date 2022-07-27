"""
Geradores

- Geradores (generator) são Iterators (Iteradores);

OBS: O contrário não é verdadeiro, ou seja, nem todo iterador é um generator.

Outras informações:
- Generators podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Functions (Funções Geradoras):
Funções:
- utilizam return
- retorna uma vez
- quando executada, retorna um valor.

Generator Functions:
- Utilizam yield
- podem utilizar yield múltiplas vezes
- quando executada, retorna um generator

# OBS: Uma Generator Function não é um Generator. Ela gera um generator, ok?

gen = conta_ate(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

=============================

gen = conta_ate(10)
for num in gen:
    print(num)
"""
# Exemplo de Generator Function

def conta_ate(valor):
    contador = 1
    while contador <= valor:
        yield contador
        contador = contador + 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator, ok?

gen = conta_ate(10)
print(next(gen))
print()
for num in gen: # Aqui a contagem começa pelo dois, pois antes já foi usado o next()
    print(num)