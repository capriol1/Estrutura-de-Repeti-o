# Estrutura Repetição: Nome e senha do usuário tem q ser diferente

nome = str(input('Digite o nome do usuário: '))
senha = input('Digite a senha: ')
while nome == senha:
    print('ERRO!\n'
          'Nome e senha deve ser diferente!')
    nome = str(input('Digite o nome do usuário: '))
    senha = input('Digite a senha: ')