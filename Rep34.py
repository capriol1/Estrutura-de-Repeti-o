# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número
# primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e
# determine se ele é ou não um número primo
num = int(input('Digite um número inteiro: '))
mult = 0
for i in range(2, num):
    if num % i == 0:
        mult += 1
if mult == 0:
    print(f'{num} é primo')
else:
    print(f'{num} não é primo')