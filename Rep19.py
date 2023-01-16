# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

quant = int(input('Digite a quantidade de números que deseja: '))

lista = []
for i in range(quant):
    num = int(input(f'Digite o {i+1}°: '))
    if 0 <= num <+ 1000:
        lista.append(num)
    else:
        print('Digite um números entre 0 e 1000')
print(f'O menor valor é {min(lista)}\n'
      f'O maoir valor é {max(lista)}\n'
      f'A soma dos valores é {sum(lista)}')