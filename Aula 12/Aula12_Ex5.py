# ***5***
# ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

def descobrir_idade():
    ano_nascimento = int(input("Digite o ano de nascimento: "))
    ano_atual = 2026
    idade = ano_atual - ano_nascimento
    print("Sua idade é:", idade)

descobrir_idade()