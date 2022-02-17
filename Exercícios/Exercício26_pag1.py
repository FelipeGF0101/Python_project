"""
Faça um programa que calcule o desvio padrão de um vetor v contendo n = 10 números, onde m é a média do vetor

Devemos calcular a média para achar o desvio padrão

Fómula:

Elementos (x);
Número de elementos(n);
Média;
Variância(v);
Desvio padrão(dp).

"""
import math
elementos = [5, 8, 4, 9, 9, 7, 8, 3, 6, 2]
vari = []
# Primeiro: Encontrar a média aritmética.

media = (sum(elementos))/10
media = int(media)


for i in elementos:
    num = (i - media)**2
    vari.append(num)
variancia = (sum(vari))/10

dp = math.sqrt(variancia)
print(f'{dp:.1f}')
