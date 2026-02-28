# DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  

def inicio():
    print("Bem-vindo ao restaurante!")



def restaurante():
    lista = ["Salada", "Macarronada", "Sanduiche", "Sorvete"]
    print("Nosso cardápio:", lista)
    

    escolha = input("Digite o nome do prato que deseja: ")
    if escolha in lista:
        print("Você escolheu:", escolha)
    else:
        print("Opção inválida.")

inicio()
restaurante()

