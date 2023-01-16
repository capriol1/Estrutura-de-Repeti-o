# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber
# um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado
# pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor
# em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
# deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

while True:
    print('Lojas Tabajara')
    produto = 1
    total = 0
    while True:
        preco = float(input(f'Produto {produto} : '))
        produto += 1
        total += preco
        if preco == 0:
            break

    print(f'Total: R$ {total:.2f}')

    troco = float(input('Dinheiro: R$ '))
    print(f'Troco: R$ {troco - total:.2f}')

