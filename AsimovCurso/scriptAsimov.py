usuario_correto = 'Gabriel'
senha_correta = 1234

print('Bem vindo, faça o login para continuar')
usuario_solicitado = input('USUARIO: ')
senha_solicitada = int(input('SENHA: '))

if usuario_solicitado == usuario_correto:
    if senha_solicitada == senha_correta:
        print(f'Login feito com sucesso, seja bem vindo {usuario_solicitado}')
    else:  
        print(f'Senha Incorreta')
else:
    print(f'Usuário não cadastrado. \nFaça seu cadastrado')