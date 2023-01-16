# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
# segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número
# do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

numeroDoMaisAlto = 0
numeroDoMaisBaixo = 0

maisAlto = 0
maisBaixo = 500

count = 0

while count < 10:
    numero = int(input('Digite o número do aluno: '))
    altura = int(input('Digite a altura do aluno (em cm): '))
    count += 1
    if altura > maisAlto:
        maisAlto = altura
        numeroDoMaisAlto = numero
    if altura < maisBaixo:
        maisBaixo = altura
        numeroDoMaisBaixo = numero

print(f'O número do aluno mais alto é {numeroDoMaisAlto}\n'
      f'Com {maisAlto}cm\n'
      f'O número do aluno mais baixo é {numeroDoMaisBaixo}\n'
      f'Com {maisBaixo}com')