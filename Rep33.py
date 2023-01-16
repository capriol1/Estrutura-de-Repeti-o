#  Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média
# das temperaturas

print('Para sair digite 0')
lista = []
count = 0
while True:
    temp = float(input('Informe a temperatura: '))
    lista.append(temp)
    count += 1
    if temp == 0:
        count -= 1
        break
lista.pop()

print(f'A maior temperatura é {max(lista)}\n'
      f'A menor temperatura é {min(lista)}\n'
      f'A média das temperaturas é {sum(lista) / count:.2f}')