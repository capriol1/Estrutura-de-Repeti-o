""" Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas.
A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e
as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a
descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As
notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:"""

notas = []
nome = input('Atleta: ')
for i in range(7):
     notas.append(float(input('Nota: ')))

maiorNota = max(notas)
menorNota = min(notas)
notas.remove(max(notas))
notas.remove(min(notas))

media = sum(notas) / len(notas)


print(f'Resultado final:\n'
      f'Atleta: {nome}\n'
      f'Melhor nota: {maiorNota}\n'
      f'Pior nota: {menorNota}\n'
      f'Média: {media:.2f}')