"""
Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das componentes desse vetor,
armazenando o resultado em outro vetor. Os conjuntos tem 10 elementos cada. Imprimir todos os conjuntos.

"""
conj1 = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.5, 9.9]
print(len(conj1))

conj2 = []

for i in conj1: # para cada item no conj1, calcule o quadrado e adicione o resultado no conj2.
    conj2.append(i**2)

print(conj1)
print(conj2)
