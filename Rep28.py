# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio
# gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

totalInvestido = 0
quantCD = int(input('Digite a quantidade de CDs: '))

for i in range(quantCD):
    totalInvestido += float(input(f'Digite o valor do {i+1}° CD: '))
    media = totalInvestido / quantCD

print(f'O total investido da coleção de CDs é {totalInvestido}\n'
      f'O valor médio gasto em cada um deles é {media:.2f}')