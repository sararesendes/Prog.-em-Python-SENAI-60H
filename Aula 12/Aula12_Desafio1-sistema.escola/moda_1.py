import estatistica

notas = []

quantidade = int(input("Quantos alunos? "))

for i in range(quantidade):
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    
print("Média:", estatistica.media(notas))
print("Moda:", estatistica.moda(notas))
print("Desvio padrão:", estatistica.desvio_padrao(notas))
print("Menor nota:", estatistica.menor_nota(notas))
print("Maior nota:", estatistica.maior_nota(notas)) 