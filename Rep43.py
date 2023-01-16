# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o
# valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve
# informar quando o pedido deve ser encerrado

print(f'Especificação  | Código | Preço\n'
      f'Cachorro Quente   100    R$ 1,20\n'
      f'Bauru Simples      101    R$ 1,30\n'
      f'Bauru com ovo      102    R$ 1,50\n'
      f'Hambúrguer         103    R$ 1,20\n'
      f'Cheeseburguer      104    R$ 1,30\n'
      f'Refrigerante       105    R$ 1,00\n')

cod100 = 0
cod101 = 0
cod102 = 0
cod103 = 0
cod104 = 0
cod105 = 0

valor100 = 0
valor101 = 0
valor102 = 0
valor103 = 0
valor104 = 0
valor105 = 0
valorTotal = 0
while True:
    codigo = int(input('Informe o código(Digite 0 para sair): '))
    if codigo == 0:
        break
    quantitade = int(input('Infome a quandidade: '))

    if codigo == 100:
        cod100 += quantitade
    elif codigo == 101:
        cod101 += quantitade
    elif codigo == 102:
        cod102 += quantitade
    elif codigo == 103:
        cod103 += quantitade
    elif codigo == 104:
        cod104 += quantitade
    elif codigo == 105:
        cod105 += quantitade

    if cod100 > 0:
        valor100 = cod100 * 1.20
    if cod101 > 0:
        valor101 = cod101 * 1.30
    if cod102 > 0:
        valor102 = cod102 * 1.50
    if cod103 > 0:
        valor103 = cod103 * 1.20
    if cod104 > 0:
        valor104 = cod104 * 1.30
    if cod105 > 0:
        valor105 = cod105 * 1.00

valorTotal = valor100 + valor101 + valor102 + valor103 + valor104 + valor105

print(f'O valor do item 100 é R${valor100:.2f}\n'
      f'O valor do item 101 é R${valor101:.2f}\n'
      f'O valor do item 102 é R${valor102:.2f}\n'
      f'O valor do item 103 é R${valor103:.2f}\n'
      f'O valor do item 104 é R${valor104:.2f}\n'
      f'O valor do item 105 é R${valor105:.2f}\n'
      f'\n'
      f'O valor total da compra é R${valorTotal:.2f}')
