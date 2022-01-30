"""
Faça um programa que leia um vetor de 10 números. Leia um número x. Conte os múltiplos de um número inteiro x num vetor e mostre-os na tela.

"""
# NÃO ENTENDI BEM O ENUNCIADO!

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1=[]
cont = 0
print(lista)

n = int(input("Escolha um número da lista acima para descobrir os seus múltiplos: "))

if n in lista:
    while cont < 10:
        cont = cont + 1
        calc = n * cont
        lista1.append(calc)
    print(lista1)
else:
    print("Escolha um valor válido!")
