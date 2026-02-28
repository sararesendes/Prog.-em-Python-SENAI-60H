## Exercícios com funções:
# variáveis locais, globais e parâmetros
# ***1*** 
# ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***

# def comparar_numeros(num1, num2):
#     resultado1 = "par" if num1 % 2 == 0 else "ímpar"
#     resultado2 = "par" if num2 % 2 == 0 else "ímpar"
    
#     print("O número", num1, "é", resultado1)
#     print("O número", num2, "é", resultado2)
# comparar_numeros(1,4)

def comparar_numeros(num1, num2):
    if num1 % 2 == 0:
        print(num1, "é par")
        
    else:
        print(num1, "é ímpar")
        
    if num2 % 2 == 0:
        print(num2, "é par")
    else:
        print(num2, "é ímpar")

comparar_numeros(7, 3)