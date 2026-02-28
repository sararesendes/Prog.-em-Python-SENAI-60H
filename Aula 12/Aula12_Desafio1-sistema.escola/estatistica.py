def media(notas):
    return sum(notas) / len(notas)


def moda(notas):
    maior_frequencia = 0
    moda = None
    
    for n in notas:
        frequencia = notas.count(n)
    if frequencia > maior_frequencia:
        maior_frequencia = frequencia
        moda = n
    return moda


def desvio_padrao(notas):
    m = media(notas)
    soma = 0
    for n in notas:
        soma += (n - m) ** 2
    
    variancia = soma / len(notas)
    return variancia ** 0.5


def menor_nota(notas):
    return min(notas)

def maior_nota(notas):
    return max(notas)