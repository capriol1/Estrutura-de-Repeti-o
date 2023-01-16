"""Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada
atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e
depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da
execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do
atleta. A saída do programa deve ser conforme o exemplo abaixo"""

saltos = []

while True:
    nome = input('Nome: ')
    if nome == '':
        print('Programa encerrado')
        break
    print(f'Atleta: {nome}')
    for i in range(5):
        saltos.append(float(input(f'{i+1}° Salto: ')))

    maiorSalto = max(saltos)
    menorSalto = min(saltos)

    saltos.remove(max(saltos))
    saltos.remove(min(saltos))

    media = sum(saltos) / len(saltos)

    print(f'Melhor salto: {maiorSalto} m\n'
          f'Pior salto: {menorSalto} m\n'
          f'Média: {media:.2f} m\n'
          f'\n'
          f'Resultado final:\n'
          f'{nome}: {media:.2f} m')
