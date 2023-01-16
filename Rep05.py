#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

cityA = int(input('Digite a população da cidade A: '))
cityB = int(input('Digite a população da cidade B: '))
taxA = float(input('Digite a taxa de crescimento da cidade A: '))
taxB = float(input('Digite a taxa de crescimento da cidade B: '))
ano = 0
while cityA < cityB:
    cityA = cityA + (cityA * (taxA / 100))
    cityB = cityB + (cityB * (taxB / 100))
    ano = ano + 1
print(f'{ano} anos')
