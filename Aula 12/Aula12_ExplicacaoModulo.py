
# # calculos_estatisticos.py

# import statistics


# f  =  [1,2,3,6,5,5,7]
# def moda(frequencia):
#     # moda é o que mais aparece 
#     moda =  statistics.mode(frequencia)
#     return moda


# f  =  [1,2,3,6,5,5,7]
# f.sort()
# # print(f)

# def mediana(f):
#     mediana =  statistics.median(f)
#     return mediana


# # x  =  [10,10,10,12,15]
# def media(f):
#     media =  statistics.mean(f)
#     return media
    


# # visualização.py

# def visualizar(texto):
#     return texto


# def imagem1():
#     return '😁'


# def imagem2():
#     return '👍'

# import random 

# #jogo.py



# def advinha(chute):
#     n =  random.randint(1,10)
#     if n == chute:
#         return 'ganhou', n
#     else:
#         return 'perdeu', n
    
#     # main.py

# import modulos.calculos_estatisticos as cl
# from modulos.jogo import advinha
# import modulos.visualizacao
# from modulos import *


# def main():
#     f =  [1,2,3,5,5,6]
#     moda_1  = cl.moda(f)
#     print(moda_1)


#     mediana_1 =  cl.mediana(f) 
#     print(mediana_1)


#     media_1 =  cl.media(f)
#     print(media_1)


#     print('****' * 15)



#     t =  int(input('Número: '))
#     resultado = advinha(t)
#     print(resultado)



#     print('****' * 15)



#     mostrar_1 =  modulos.visualizacao.imagem1()
#     print(mostrar_1)
#     mostrar_2 =  modulos.visualizacao.imagem1()
#     print(mostrar_2)
#     mostrar_3 =  modulos.visualizacao.visualizar('text')
#     print(mostrar_3)


# main()




# import modulos.calculos_estatisticos as cl
# from modulos.jogo import advinha
# import modulos.visualizacao


# def main():
#     f =  [1,2,3,5,5,6]
#     moda_1  = cl.moda(f)
#     print(moda_1)


#     mediana_1 =  cl.mediana(f) 
#     print(mediana_1)


#     media_1 =  cl.media(f)
#     print(media_1)


#     print('****' * 15)



#     t =  int(input('Número: '))
#     resultado = advinha(t)
#     print(resultado)



#     print('****' * 15)



#     mostrar_1 =  modulos.visualizacao.imagem1()
#     print(mostrar_1)
#     mostrar_2 =  modulos.visualizacao.imagem1()
#     print(mostrar_2)
#     mostrar_3 =  modulos.visualizacao.visualizar('text')
#     print(mostrar_3)


# main()