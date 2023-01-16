# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é
# aquele que é divisível somente por ele mesmo e por 1.

num = int(input('Digite um números inteiro: '))
mult = 0

for i in range(2, num):
    if num % i == 0:
        print('Mútiplo de ',i)
        mult += 1
if mult == 0:
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')