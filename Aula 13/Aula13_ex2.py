import random
#2 - Crie 3 números aleatórios

def seq_tres_num_aleatorios():
    lista = []

    for i in range (3):
        numero = random.randint(1, 100)
        lista.append(numero)

    return lista

print (seq_tres_num_aleatorios())