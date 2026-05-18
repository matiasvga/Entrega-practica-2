#5 participantes evaluados por 3 jueces durante 5 rondas
#Cada juez otorga del 1 al 10
#Puntaje de ronda = suma de los 3 jueces
#Imprimir: 
# tabla de posiciones parcial al finalizar una ronda
# ganador de la última ronda
# contabilizar rondas ganadas
# tabla final con puntaje total, cantida de rondas ganadas,
# mejor puntaje de ronda, y puntaje promedio por ronda.
# (todo en orden decreciente por puntaje total)

def simular_ronda(actual, nombres):
    #Inicializo lista del puntaje de ronda
    suma = [0,0,0,0,0]
    
    #Itero sobre el diccionario 'scores'
    for indice,competidor in enumerate(actual):
        #Obtengo el puntaje de ronda de cada competidor y lo guardo en la lista
        puntajes = list(actual[competidor].values())
        suma[indice] = sum(puntajes)
    
    #Busco el índice del puntaje máximo de la ronda y 
    #me guardo el nombre del competidor correspondiente
    ganador = nombres[suma.index(max(suma))]
    
    return ganador, suma