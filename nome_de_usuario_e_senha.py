count = 1
while count == 1:
    usuario = input('Digite o usuario: ')
    senha = input('Digite a sua senha: ')
    if usuario == senha:
        print ('Error! os dados informados são iguais!')
        count = 1
    else:
        print ('Bem vindo!')
        count+=2