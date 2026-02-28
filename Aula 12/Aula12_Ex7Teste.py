def restaurante():
    lista = ["Salada", "Macarronada", "Sanduiche", "Sorvete"]
    while True:
        print("CARDÁPIO: ")

        for n in range (len(lista)):
            print (n + 1, "-", lista[n])

        opcao = int(input("Digite sua escolha pelo número: "))

        if opcao == 0:
            print ("Obrigado pela visita!")
        elif opcao >= 1 and opcao <= len(lista):
            print ("Você optou por: ", lista[opcao - 1])
        else: 
            print ("Opção inválida! Tente novamente.")

restaurante()
