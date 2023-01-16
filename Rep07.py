#Faça um programa que leia 5 números e informe o maior número.

for i in range(5):
    num = int(input(f'Digite o {i+1}°: '))

maior = 0
if num > maior:
    print(f'O maoir número informanda é {num}')