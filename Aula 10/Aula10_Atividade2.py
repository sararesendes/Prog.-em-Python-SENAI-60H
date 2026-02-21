#Atividade 2
# Crie um sistema de notas alunos, com as seguintes operações:
# ***Utilize While ou for***
#  **Sistema de notas de alunos**
# - ***Visão do professor***
# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média
# - Utilize ***loops for, while, condicionais, variáveis, listas, tuplas ou dicionários…***
# ***IMPORTANTE:***
# - Ao finalizar o código, insira na borda do script, no última linha:
# input(’Digite enter para sair’)

usuarios = {
"professor1": "1234",
"professor2": "abcd",
"admin": "0000"
}

acesso_liberado = False

for tentativa in range(3):
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

# Verifica se o usuário existe e se a senha está correta
if usuario in usuarios and usuarios[usuario] == senha:
    print("\nAcesso liberado!\n")
    acesso_liberado = True
    break
else:
    print("Usuário ou senha incorretos.\n")

# Se errar 3 vezes
if not acesso_liberado:
    print("Conta bloqueada! Você errou 3 vezes.")

# Se login estiver correto
else:
    alunos = {} # Dicionário para armazenar alunos e médias
    quantidade = int(input("Quantos alunos deseja cadastrar? "))
    for i in range(quantidade):
        nome = input("\nNome do aluno: ")
        notas = []
        
        for j in range(3):
            nota = float(input(f"Digite a nota {j+1}: "))
            notas.append(nota)
            media = sum(notas) / len(notas)
            
            alunos[nome] = media

print("\n===== RESULTADO FINAL =====\n")

for nome, media in alunos.items():

print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")

if media >= 6:
print("Situação: Aprovado\n")
else:
print("Situação: Reprovado\n")


input('Digite enter para sair')
 