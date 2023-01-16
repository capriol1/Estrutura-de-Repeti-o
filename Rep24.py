# Faça um programa que calcule o mostre a média aritmética de N notas.

quantNotas = int(input('Digite a quantidade de notas: '))
soma = 0
for i in range(quantNotas):
    nota = float(input(f'Digite a {i+1}°: '))
    soma += nota
    media = soma / quantNotas

print(f'A média aritmética das notas é {media:.2f}')