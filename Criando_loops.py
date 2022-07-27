"""
Criando sua própria versão de loop

for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Geek')

"""
def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break

# meu_for('Geek')

def novo_loop(iteravel):
    cont = 0
    it = iter(iteravel)
    while cont != len(iteravel):
        cont = cont + 1
        print(next(it))

