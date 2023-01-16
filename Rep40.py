# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 1999);
# c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e. Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio

codigoCityMenor = 0
codigoCityMaior = 0

maiorAcidentes = 0
menorAcidentes = 10000000000

somaViculos = 0
somaAcidentes = 0
somaCity2000 = 0

cityComMenos2000 = 0
count = 0

while count < 5:
    codigo = int(input(f'Informe o código de cidade: '))
    veiculos = int(input('Informe a quantidade de veículos de passeio: '))
    acidentes = int(input('Informe a quantidade de acidentes: '))

    count += 1
    somaViculos += veiculos
    somaAcidentes += acidentes

    if acidentes > maiorAcidentes:
        maiorAcidentes = acidentes
        codigoCityMaior = codigo

    if acidentes < menorAcidentes:
        menorAcidentes = acidentes
        codigoCityMenor = codigo

    if veiculos < 2000:
        somaCity2000 += acidentes
        cityComMenos2000 += 1

print(f'A cidade com maior índice de acidentes é {codigoCityMaior}\n'
      f'Com {maiorAcidentes} acidentes\n'
      f'A cidade com menro índice de acidentes é {codigoCityMenor}\n'
      f'Com {menorAcidentes} acidentes\n'
      f'\n'
      f'A média de veículos das 5 cidades é {somaViculos / 5}\n'
      f'A média de acidentes das 5 cidades é {somaAcidentes / 5}\n'
      f'A média de acidentes nas cidades com menos de 2000 veículos de passeio é {somaCity2000 / cityComMenos2000 }')