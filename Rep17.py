# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input('Informe um número: '))
fatorial = 1

for i in range(1, n +1):
    fatorial *= i
print(f'O fatorial de {n} é {fatorial}')