# **6 - Tabuada de multiplicação**
# ***Utilize print() na saída***
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (while ou for )

def tabuada(numero):
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

num = int(input("Digite um número inteiro: "))
tabuada(num)
