# Faça   um   programa   que   peça   dois   números,   base   e   expoente,   calcule   e   mostre   o   primeiro   número   elevado   ao
# segundo número. Não utilize a função de potência da linguagem.

base = int(input('Digite a base da potência: '))
expoente = int(input('Digite o expoente da potência: '))
potencia = 1

for i in range(expoente):
    potencia *= base
    i += 1

print(f'{base} ^ {expoente} = {potencia}')