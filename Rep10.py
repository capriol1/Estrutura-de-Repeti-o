# Faça   um   programa   que   receba   dois   números   inteiros   e   gere   os   números   inteiros   que   estão   no   intervalo
# compreendido por eles

num1 = int(input('Informe o primeiro número do intervalo: '))
num2 = int(input('Informe o segundo número do intervalo: '))
print(f'Os números que estão no intervalo entre {num1} e {num2} são: ')
for i in range(num1+ 1, num2):
    print(i)