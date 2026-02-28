import statistics

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

empresas = {
"Empresa 1": empresa1,
"Empresa 2": empresa2,
"Empresa 3": empresa3,
"Empresa 4": empresa4
}

for nome, salarios in empresas.items():
    print("\n", nome)
    print("Média:", statistics.mean(salarios))
    print("Mediana:", statistics.median(salarios))
    print("Moda:", statistics.mode(salarios))
    print("Desvio padrão:", statistics.stdev(salarios))

# Escolheria a empresa 2, pois ela apresenta uma média salarial mais equilibrada e menor desvio padrão.
# indicando menor variação, menos risco de desigualdade salarial e mais estabilidade financeira.