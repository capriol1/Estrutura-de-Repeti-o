#  Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade
# da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a
# média calculada.

quantTurma = int(input('Informa a quantidade de pessoas da turma: '))
soma = 0
for i in range(quantTurma):
    idade = int(input(f'{i+1}. Informe sua idade: '))
    soma += idade
    media = soma / quantTurma
print(f'A média da turma é {media}')
if media > 0 and media <= 25:
    print('A turma é jovem')
elif media > 26 and media <= 60:
    print('A turma é adulta')
else:
    print('A turma é idosa')