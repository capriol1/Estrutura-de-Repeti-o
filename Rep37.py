# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e
# o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu
# código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no
# campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do
# mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

codigoGordo = 0
codigoMagro = 0
codigoAlto = 0
codigoBaixo = 0

maiorPeso = 0
menorPeso = 1000
maiorAltura = 0
menorAltura = 500

somaPeso = 0
somaAltura = 0
somaClientes = 0

while True:
    codigo = int(input('Informe seu código: '))
    if codigo == 0:
        break
    altura = int(input('Informe sua altura (em cm): '))
    peso = float(input('Informe seu peso (em kg): '))

    somaAltura += altura
    somaPeso += peso
    somaClientes += 1

    if altura > maiorAltura:
        maiorAltura = altura
        codigoAlto = codigo

    if altura < menorAltura:
        menorAltura = altura
        codigoBaixo = codigo

    if peso > maiorPeso:
        maiorPeso = peso
        codigoGordo = codigo

    if peso < menorPeso:
        menorPeso = peso
        codigoMagro = codigo


print(f'O código  do mais alto é {codigoAlto}\n'
      f'Com a maior altura de {maiorAltura}\n'
      f'O código de mais baixo é {codigoBaixo}\n'
      f'Com a menor altura de {menorAltura}\n'
      f'\n'
      f'O código com maior peso é {codigoGordo}\n'
      f'Com {maiorPeso}Kg\n'
      f'O código com menor peso é {codigoMagro}\n'
      f'Com {maiorPeso}Kg\n'
      f'\n'
      f'A média de altura dos clientes é {somaAltura/somaClientes:.2f}\n'
      f'A média de peso dos clientes é {somaPeso/somaClientes:.2f}')