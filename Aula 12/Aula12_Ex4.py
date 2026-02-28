# ***4***
# ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade == 18:
        print("Você tem 18 anos!")
    else:
        print("Sua idade é diferente de 18.")

verificar_idade()