"""
Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro. Se o códifo for zero, finalize programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre o vetor na ordem inversa. Caso, o código seja diferente de 1 e 2 escreva uma mensagem informando que o código é inválido.
"""
lista = []

for num in range(0,5):
    num = float(input("Digite um número: "))
    lista.append(num)

cod = int(input("Digite o código (0, 1, 2): "))
if cod == 0:
    print("Finalizando programa!")
elif cod == 1:
    print(lista)
elif cod == 2:
    lista.reverse()
    print(lista)
else:
    print("Código inválido!")
