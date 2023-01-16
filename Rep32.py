# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A
# saída deve ser conforme o exemplo abaixo:
import math
num = int(input('Informe o número: '))

fatorial = math.factorial(num)

print(f'Fatorial de: {num}')
print(num,'! = ', end='')
for i in range(num - 1):
    print(num, end=' . ')
    num -= 1
print('1 = ', fatorial)