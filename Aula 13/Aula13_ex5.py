
#**5 - Soma de números pares**
#Peça ao usuário que insira um número inteiro positivo e, em seguida, calcule a soma de todos os números pares de 2 até o número inserido.

def soma_pares():
    numero = int(input("Digite um número inteiro positivo: "))
    soma = 0
    
    for i in range(2, numero + 1):
        if i % 2 == 0:
            soma += i
            
    return soma

print("A soma dos numeros pares é", soma_pares())

