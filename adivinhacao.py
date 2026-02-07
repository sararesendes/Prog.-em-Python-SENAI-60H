import random

aleatorio = random.randint(1,10)
chute = int(input('Chute um número: '))

if aleatorio == chute:
    print('acertei em cheio')
    print('0 numero é ', aleatorio)
else:
    print('Errou feio!')
    print('0 numero é ', aleatorio)