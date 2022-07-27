"""
Teste de memória com Generators

# Sequência de Fibonacci
1, 1, 2, 3, 5, 8, 13

"""
# Função usando listas = 449MB
def fib_lista(max):
    num = []
    a, b = 0, 1
    while len(num) < max:
        num.append(b)
        a = b
        b = a + b
    return num

# Função usando geradores 3MB

def fib_gen(max):
    a = 0
    b = 1
    contador = 0
    while contador < max:
        a = b
        b = a + b
        yield a
        contador = contador + 1

for n in fib_gen(100):
    print(n)