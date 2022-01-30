"""
Módulo collections - Deque

Podemos dizer que o Deque é uma lista de alta performance

"""
# Import
from collections import deque

# Criando Deques

deq = deque("Felipe")
print(deq)

# Adicionando elementos no Deque

deq.append('e') # Adiciona no final
print(deq)

deq.appendleft('f') # Adiciona no início
print(deq)

# Remover elementos

print(deq.pop()) # Remove e retorna o últmo elemento
print(deq)

print(deq.popleft()) # Remove e retorna o primeiro elemento
print(deq)