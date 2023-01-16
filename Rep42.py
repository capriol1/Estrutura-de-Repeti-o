# . Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos
# seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um
# número negativo
intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
print('Para sair digite um número negativo')
while True:
    num = int(input('Digite um número inteiro entre 0 a 100: '))
    if num < 0:
        break

    if num <= 25:
        intervalo1 += 1

    elif num <= 50:
        intervalo2 +=1

    elif num <= 75:
        intervalo3 =+ 1

    elif num <= 100:
        intervalo4 =+ 1



print(f'De todos os números:\n'
      f'São {intervalo1} no intervalo de [0-25]\n'
      f'São {intervalo2} no intervalo de [26-50]\n'
      f'São {intervalo3} no intervalo de [51-75]\n'
      f'São {intervalo4} no intervalo de [76-100]')