"""Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total
 de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma
 pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
 a. Maior e Menor Acerto;
 b. Total de Alunos que utilizaram o sistema;
 c. A Média das Notas da Turma"""

gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']

totalAlunos = 0
somaNotas = 0
maiorAcerto = 0
menorAcerto = 10

while True:
    nota = 0

    for i in range(10):
        resposta = input(f"Resposta da questão {i + 1}: ").upper()
        if resposta == gabarito[i]:
            nota += 1

    totalAlunos += 1
    somaNotas += nota

    print(f"Nota: {nota}")

    outroAluno = input("Outro aluno vai utilizar o sistema? (S/N)").upper()
    if outroAluno != 'S':
        break

print(f"Total de alunos: {totalAlunos}")
print(f"Maior acerto: {max(maiorAcerto,nota)}")
print(f"Menor acerto: {min(menorAcerto,nota)}")
print(f"Média das notas: {somaNotas/totalAlunos:.2f}")