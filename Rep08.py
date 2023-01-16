#  Faça um programa que leia 5 números e informe a soma e a média dos números.

cont = 0
soma = 0
media = 0

while cont < 5:
    num = int(input('Informe um número: '))
    soma = num + num
    media = soma / 5
    cont += 1
print(f'A soma dos números é {soma}\n'
      f'A média dos números é {media}')