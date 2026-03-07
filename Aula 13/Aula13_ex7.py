import time

#**7 -  Números ímpares reversos**
#Exiba uma contagem regressiva de números ímpares de 99 a 1.

def impares_reverso():
    for i in range(99, 0, -1):
        time.sleep(1)
        if i % 2 != 0:
            print(i)

impares_reverso()