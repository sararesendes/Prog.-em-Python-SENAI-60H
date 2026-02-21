# 5: Classificando uma idade em faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)

idade = int(input( 'Digite a idade: '))

match idade:
    case n if n <= 12:
        print('Criança')
    case n if n <= 17:
        print('Adolescente')
    case n if n < 35:
        print('Jovem')
    case n if n <= 64:
        print('Adulto')
    case _:
        print('Idoso')