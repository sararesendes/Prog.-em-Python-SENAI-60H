import random

print('Pedra Papel Tesoura')

lista_maquina = ['🪨', '🧻', '✂️']
chute_maquina = random.choice(lista_maquina)

minha_lista = ['🪨', '🧻', '✂️']
print('ESCOLHA SEU ÍCONE')
print('0 - 🪨 | 1 -  🧻 | 2 - ✂️')
meu_chute = int(input('Escolha pelo indice: '))

if chute_maquina == minha_lista[meu_chute]:
    print('**'*10)
    print('EMPATE')
    print('**'*10) 
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])
    
if chute_maquina == '🪨' and minha_lista[meu_chute] == '✂️':
    print('**'*10)
    print('VITÓRIA DA MAQUINA')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])

if chute_maquina == '✂️' and minha_lista[meu_chute] == '🧻':
    print('**'*10)
    print('VITÓRIA DA MAQUINA')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])

if chute_maquina == '🧻' and minha_lista[meu_chute] == '🪨':
    print('**'*10)
    print('VITÓRIA DA MAQUINA')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])


if minha_lista[meu_chute] == '🪨' and chute_maquina == '✂️':
    print('**'*10)
    print('VOCÊ GANHOU!')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])

if minha_lista[meu_chute] == '✂️' and chute_maquina == '🧻':
    print('**'*10)
    print('VOCÊ GANHOU!')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])

if minha_lista[meu_chute] == '🧻' and chute_maquina == '🪨':
    print('**'*10)
    print('VOCÊ GANHOU!')
    print('**'*10)
    print('ESCOLHA MAQUINA - ', chute_maquina)
    print('MINHA ESCOLHA - ',minha_lista[meu_chute])    