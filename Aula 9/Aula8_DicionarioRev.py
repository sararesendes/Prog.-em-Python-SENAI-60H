# cadastro 
dados = {
        'login':[],
        'senha':[],
            'produtos':{
                        '1': ['Computador Dell - R$', 5000.0],
                        '2': ['Fone Apple - R$', 2000.0],
                        '3': ['Mouse Lenovo - R$', 250.0],
                        '4': ['Monitor Lenovo - R$', 3000.0],
                        }
}

print('CADASTRE-SE:')
cad_login = input('Cadastre seu login: ')
cad_senha = input('Cadastre a sua senha:')
dados['login'].append(cad_login)
dados['senha'].append(cad_senha)

# acessar o e-commerce
print('ACESSE A APLICAÇÃO: ')

acesso_login = input('Digite seu login para acessar: ')
acesso_senha = input('Digie sua senha para acesssar: ')

if acesso_login == dados['login'][0] and acesso_senha == dados['senha'][0]:
    print('SEJA BEM VINDO(A) AO E-COMMERCE Z')
    # verificar a lista de produtos
    print("PRODUTOS: " )
    produto = input(f'''
    {dados['produtos']} - escolha 1 - 2 - 3 - 4 ->>>
    ''')

    # comprar um produto
    carrinho = []
    valores = []

    carrinho.append(dados['produtos'][produto][0])
    valores.append(dados['produtos'][produto][1])
    print(carrinho[0],valores[0])


    # pagar o produto

else:
    print('Digitação de senha e login incorreta')
    print('Faça novamente')