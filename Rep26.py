# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada
# eleitor votar e ao final mostrar o número de votos de cada candidato

candidato1 = 0
candidato2 = 0
candidato3 = 0

quantEleitor = int(input('Informe a quantidade total de eleitores: '))
print(f'Para votar\n'
      f'Candidato1- Digite 1\n'
      f'Candidato2- Digite 2\n'
      f'Candidato3- Digite 3')
for i in range(quantEleitor):
    voto = int(input('Digite seu voto: '))
    if voto == 1:
          candidato1 += 1
    elif voto == 2:
          candidato2 += 1
    else:
          candidato3 += 1

print(f'O primeiro candidato teve {candidato1} votos\n'
      f'O segundo candidato teve {candidato2} votos\n'
      f'O terceiro cantdidato teve {candidato3} votos')
