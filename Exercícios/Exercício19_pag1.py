"""
Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1), sendo i a posição do elemento no vetor. Em seguida imprima o vetor na tela. 

"""
vetor = []

for i in range(1, 51): # Gera um vetor de 50 posições, começando pelo 1 e terminando em 50, ignorando o 51.
    result = (i + 5 * i) % (i + 1) # Para cada item, substitua o i por sua posição dentro do vetor.
    vetor.append(result) # Adiciona cada resultado no vetor vazio 'Vetor'.

print(vetor)
