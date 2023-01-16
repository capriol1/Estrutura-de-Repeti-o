# Estrutura Repetição: peça uma notade 0 a 10

nota = float(input('Digite uma nota de 0 a 10:  '))
while 0 < nota > 10:
    nota = float(input('Digite uma nota de 0 a 10: '))
print('Nota válida')