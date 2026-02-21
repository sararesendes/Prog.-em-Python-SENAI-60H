# 2 -  Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

nomes = []
quantidade = 0

while quantidade < 10:
    nome = input('Digite um nome: ')
    nomes.append(nome)
    quantidade += 1
    print("Lista de nomes digitados:", nomes)  
     
while quantidade < 10:
    print(nomes[quantidade])
    quantidade += 1
