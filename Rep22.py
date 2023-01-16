 # Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número
 # ele é divisível.

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