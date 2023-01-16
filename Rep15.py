# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série
# até o n−ésimo termo.

n = int(input('Quantos termos deseja mostrar: '))

t1 = 0
t2 = 1
print(f'{t1} - {t2}', end='')
count = 3

while count <= n:
    t3 = t1 +t2
    print(f' - {t3}', end='')
    t1 = t2
    t2 = t3
    count +=1
