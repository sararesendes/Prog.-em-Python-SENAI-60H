# 1: Verificando se o número é par ou ímpar

numero = int(input( 'numero: '))

match numero:
    case numero if numero % 2 == 0:
        print('Par')
    case _:
        print('Impar')