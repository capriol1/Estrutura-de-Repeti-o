# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário
# deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo

num = int(input('Digite o número que deseja a tabuada: '))

for i in range(1, 11):
    print(f'{num} x {i} = {num * i}')