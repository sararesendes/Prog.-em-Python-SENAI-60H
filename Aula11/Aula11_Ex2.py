# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.


try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    resultado = numero1 / numero2
    print("O resultado da divisão é:", resultado)

except ZeroDivisionError: 
      print('Erro! Não é possível dividir por zero.')
except ValueError:
      print('Um texo foi digitado')
except TypeError as erro:
      print(erro)

else:
     print('Fim! ')    