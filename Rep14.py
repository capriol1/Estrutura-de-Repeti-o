# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade
# de números impares

pares = 0
impares = 0

for i in range(10):
    num = int(input(f'Informe {i+1}° número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'A quantidade total de números pares é {pares}\n'
      f'A quantidade total de números ímpares é {impares}')