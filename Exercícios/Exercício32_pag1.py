"""
Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa elementos repetidos). Calcule e mostre os vetores resultantes em cada caso abaixo:

> Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
> Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y.
> Diferença entre x e y: todos os elementos de x que não existam em y.
> Intersecção entre x e y: apenas os elmentos que aparecem nos dois vetores.
> União entre x e y: todos os elementos de x, e todos os elementos de y que não estão em x.
"""
x = []
y = []
xny = []
xjy = []
junt = []
cont = 0
cont1 = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in x:
        x.append(n)
        cont = cont + 1
       
    else:
        print('Valor duplicado!')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break

    if cont == 5:
        print('Vetor x completo!') 
        break       

while True:
    n = int(input('Digite um valor: '))
    if n not in y and n not in x:   
        y.append(n)
        cont1 = cont1 + 1
              
    else:
        print('Valor duplicado!')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
     
    if cont1 == 5:
        print('Vetor y completo!') 
        break
print('======' * 6)
print(f'Esses são os elementos de x: {x}.')
print('======' * 6)
print(f'Esses são os elementos de y: {y}.')
print('======' * 6)
soma = list(map(lambda v1, v2: v1 + v2, x, y))
print(f'A soma dos elementos de x com os elementos de y localizados na mesma posição é: {soma}')
print('======' * 6)
mult = list(map(lambda v1, v2: v1 * v2, x, y))
print(f'A multiplicação dos valores de x e y é: {mult}')
print('======' * 6)
# Apesar de eu já ter impossibilitado a repetição de valores entre as duas listas
for i in x:
    junt.append(i)
    if i not in y:
        xny.append(i)
if i in x and i in y:
        xjy.append(i)
else:
    print('Não existem elementos repetidos entre os vetores!')
    print('======' * 6)
    if i in y != i in x:
        junt.append(i)

print(f'Aqui estão todos os elementos de x que não existem em y: {xny}.')
print('======' * 6)
print(f'Aqui estão todos os elementos, não repetidos, de x e de y: {junt}.')
