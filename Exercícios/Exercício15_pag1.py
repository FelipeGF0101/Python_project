"""
Leia um vetor com 20 número inteiros. Escreva os elementos do vetor eliminando elementos repetidos.

"""
vetor = [9, 4, 3, 5, 8, 8, 2, 3, 9, 10, 48, 2, 3, 8, 2, 4, 9, 4, 5, 2]
print(vetor)

# Forma 1
# Transformando uma lista em set(conjunto).
# O conjunto exclui da lista os valores repetidos. 
set(vetor)
print(set(vetor))
# O problema desse método é que ele não mantém a ordem correta dos valores da lista original.


# Forma2
from collections import OrderedDict
OrderedDict.fromkeys(vetor)
vetor_final = list(OrderedDict.fromkeys(vetor)) 
vetor_final # Convertendo novamente para lista

print(vetor_final)

# Antes de mais nada, é preciso saber que OrderedDict é uma estrutura de dados muito similar a um dicionário. A grande diferença é que o OrderedDict guarda internamente a ordem de inserção dos elementos. Assim, quando iteramos sobre um objeto desse tipo, ele irá retornar seus elementos na ordem em que foram inseridos.

# O método fromkeys() cria um dicionário usando como chaves os valores passados como primeiro parâmetro e como valor o que for passado como segundo parâmetro (ou none, caso não passemos nada).

# Agora que temos um dicionário com as chaves mantidas em ordem de inserção, podemos chamar o método keys() para obter somente as chaves.

