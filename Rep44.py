# . Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:1 , 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor
# zero

print(f'1, 2, 3, 4 - Votos para os resoectivos candidados\n'
      f'1 - Cleber Machado\n'
      f'2 - João Cleber\n'
      f'3 - Marcus João\n'
      f'4 - Diogo Marcus\n'
      f'5 - Voto Nulo\n'
      f'6 - Voto Branco')

totalCand1 = 0
totalCand2 = 0
totalCand3 = 0
totalCand4 = 0
totalVotosNulo = 0
totalVotosBranco = 0
geralTotal = 0

print('0 para encerrar')
while True:
    voto = int(input('Voto: '))

    if voto == 0:
        break

    if voto == 1:
        totalCand1 += 1
    elif voto == 2:
        totalCand2 += 1
    elif voto == 3:
        totalCand3 += 1
    elif voto == 4:
        totalCand4 += 1
    elif voto == 5:
        totalVotosNulo += 1
    elif voto == 6:
        totalVotosBranco += 1

geralTotal = totalCand1 + totalCand2 + totalCand3 + totalCand4 + totalVotosNulo + totalVotosBranco
percentualNulo = (totalVotosNulo / geralTotal) * 100
pecentualBranco = (totalVotosBranco / geralTotal) * 100

print(f'O total de votos do candidato 1 é {totalCand1}\n'
      f'O total de votos do candidato 2 é {totalCand2}\n'
      f'O total de votos do candidato 3 é {totalCand3}\n'
      f'O total de votos do candidato 4 é {totalCand4}\n'
      f'O total de votos nulos é {totalVotosNulo}\n'
      f'O total de votos brancos é {totalVotosBranco}\n'
      f'O percentual de votos nulos {percentualNulo:.2f}%\n'
      f'O percentual de votos brancos {pecentualBranco:.2f}%')