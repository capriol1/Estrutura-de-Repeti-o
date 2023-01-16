# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a
# números inteiros positivos e menores que 16.

print(f'1- Calcular o fatorial \n'
      f'2- Para sair')

op = int(input('Informe a opção: '))
while True:
    if op == 1:
        n = int(input('Informe um número: '))
        fatorial = 1
        if 0 <= n <= 16:
            for i in range(1, n +1):
                fatorial *= i
            print(f'O fatorial de {n} é {fatorial}')
        else:
            print('O fatorial está limitado a números inteiros positivos e menores que 16')
    if op == 2:
        break
    else:
        print('Se deseja continuar digite 1')
        op = int(input('R.: '))