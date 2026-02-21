# 3: Verificando se uma string é vazia ou não

texto = int(input( 'Digite algo: '))

match texto:
    case "":
        print('String vazia')
    case _:
        print('String não vazia')