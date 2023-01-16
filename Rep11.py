# Altere o programa anterior para mostrar no final a soma dos números.

num1 = int(input('Informe o primeiro número do intervalo: '))
num2 = int(input('Informe o segundo número do intervalo: '))
soma = 0

for i in range(num1 + 1, num2):
    soma += i
    print(f'A soma do intervalo é {soma}')