# Estrutura Repetição: A ultrapasse ou iguala a população de B

a = 80000
b = 200000
ano = 0
while a <= b:
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    ano = ano + 1
print(f'{ano} anos')

