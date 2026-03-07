import random
#3 - Crie um número aleatório entre 10 a 30 utilize o range()

def numero_aleatorio_10_30():
    numeros = list(range(10, 31))
    numero = random.choice(numeros)
    return numero

print (numero_aleatorio_10_30())