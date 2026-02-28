#Exercício 1:
#Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
    numero = int(input("Digite um número inteiro: "))
    print("Número digitado:", numero)
    
except ValueError:
    print("Erro! Você não digitou um número inteiro")