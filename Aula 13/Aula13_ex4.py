import time

#4 - Contagem regressiva simples
#Escreva um programa que exiba uma contagem regressiva de 10 a 1, e depois imprima "Fogo!".(loop for)

def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
        time.sleep(1)
    print("Fogo!")

contagem_regressiva()