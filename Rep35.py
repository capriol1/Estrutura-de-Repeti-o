# . Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos
# existentes entre 1 e um número inteiro informado pelo usuário.

num = int(input('Digite um número inteiro: '))
lista = []

for i in range(1, num):
    if i % 2 == 1 and i != 2:
        lista.append(i)
print(lista)