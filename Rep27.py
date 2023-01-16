# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a
# quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

quantTurmas = int(input('Informe a quantidade de turmas: '))
totalAlunos = 0
for i in range(quantTurmas):
    quantAlunos = int(input(f'Digite a quantidade dde alunos da {i+1}° turma: '))
    if quantAlunos > 40:
        print('A turma não pode ter mais de 40 alunos')
        quantAlunos = int(input(f'Digite a quantidade dde alunos da {i + 1}° turma: '))
    totalAlunos += quantAlunos
    media = totalAlunos / quantTurmas
print(f'O número médio de alunos por turma é {media}')
