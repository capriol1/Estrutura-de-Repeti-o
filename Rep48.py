# Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido

print('Digite 0 para encerrar o programa')
while True:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero == 0:
        print('Programa encerrado')
        break

    numeroInvertido = str(numero)[::-1]

    print(f"O número invertido é: {numeroInvertido} ")