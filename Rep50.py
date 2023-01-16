#Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.


H = 0
N = int(input("Insira o número de termos: "))
for i in range(1, N+1):
    H += 1/i

print(f"Valor de H com {N} termos:{H:.2f}")
