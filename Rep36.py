# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a
# tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados
# também pelo usuário, conforme exemplo abaixo:

tabuada = int(input('Montadar a tabualda de: '))
comeco = int(input('Começar por: '))
terminar = int(input('Terminar em: '))

if terminar <= comeco:
    print('Você não pode digitar um número final menor que o inicial ')
    terminar = int(input('Terminar em (Maior que o inicial): '))

print(f'Vou montar a tabuada de {tabuada} começando em {comeco} e termidando em {terminar}')

for i in range(comeco, terminar + 1):
    print(f'{tabuada} x {i} = {tabuada * i}')