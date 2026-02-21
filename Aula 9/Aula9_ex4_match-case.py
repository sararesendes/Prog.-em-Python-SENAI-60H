# 4: Verificando se um número é maior, menor ou igual a 10

numero = int(input( 'Digite um numero: '))

match numero:
    case 10:
        print('O número digitado é igual a 10')
    case n if n > 10:
        print('O número digitado é maior que 10')
    case _:
        print('O número digitado é mmenor que 10')