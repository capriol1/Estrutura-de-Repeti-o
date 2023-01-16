# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida,
# valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo

valorDivida = float(input('Informe o valor da divida: R$'))
parcela = 1
juros = 0
print("Valor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")

while True:
    juros = (5/3) * parcela + 5
    if parcela == 1:
        juros = 0

    valorJuros = valorDivida * (juros / 100)
    valorTotal = valorDivida + valorJuros
    valorDaParcela = valorTotal / parcela
    print(f'R${valorTotal:.2f}\t\t'
          f'R${valorJuros:.2f} \t\t'
          f'{parcela}\t\t'
          f'R${valorDaParcela:.2f}      ')
    if parcela == 1:
        parcela-= 1
    parcela+=3

    if parcela>12:
        break