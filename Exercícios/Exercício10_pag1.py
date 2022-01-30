"""
Faça um programa para ler a nota de 15 alunos e armazene num vetor, calcule e imprima a média geral.
"""
notas = 0
alunos = []
calc = 0
for n in range(1, 16):
    notas = int(input('Digite a nota do aluno: '))
    alunos.append(notas)

print(alunos)

for notas in alunos:
    calc = calc + notas/15

print(f'A média das notas da turma foi:{calc:.1f}')