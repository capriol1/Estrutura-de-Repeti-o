# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos
# valores.

quant = int(input('Digite a quantidade de números que deseja: '))

lista = []
for i in range(quant):
    num = int(input(f'Digite o {i+1}°: '))
    lista.append(num)
print(f'O menor valor é {min(lista)}\n'
      f'O maoir valor é {max(lista)}\n'
      f'A soma dos valores é {sum(lista)}')