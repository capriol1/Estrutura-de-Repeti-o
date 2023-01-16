# Estrutura Repitição: validação de nome, idade, salario, sexo, estado civil

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salário: '))
sexo = input('Digite seu sexo(F/M): ').capitalize()
civil = input('Digite seu estado civil(S/C/V/D): ').capitalize()
while len(nome) <= 3:
    nome = input('Seu nome precisa de mais que 3 caracteres: ')
while 0 < idade > 150:
    idade = int(input('Você deve ter idade entre 0 a 150:  '))
while salario < 0:
    salario = float(input('Não tem como ter salário negativo: '))
while sexo != 'F' and sexo != 'M':
    sexo = input('F- Feminino ou M-Masculino: ').capitalize()
while civil != 'S' and civil !='C' and civil != 'V' and civil != 'D':
    civil = input('S-Solteiro, C-Casado, V-Viúvo, D-Divorciado: ').capitalize()