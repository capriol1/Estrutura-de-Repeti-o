
salario = 1000
ano = 1995
ano97 = 1997
aumento = 1.5 / 100

while ano < ano97:
    ano += 1
    salario *= 1 + aumento
    aumento *= 2
print(f'O salário no ano {ano97} é de R${salario}')

