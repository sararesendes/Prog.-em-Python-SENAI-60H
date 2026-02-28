# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

try:
    lista = ["maçã", "banana", "uva", "laranja", "limao"]
    indice = int(input("Digite o índice que você quer acessar: "))
    print("O elemento no índice é:", lista[indice])

except IndexError:
    print("Erro! Esse índice não existe na lista.")

except ValueError:
    print("Erro! precisa digitar um número inteiro.")
