# 2: Verificando se um número é positivo, negativo ou zero

numero = int(input( 'Digite um numero: '))

match numero:
    case 0:
        print('O número digitado é 0')
    case n if n > 0:
        print('O número digitado é positivo')
    case _:
        print('O número digitado é negativo')