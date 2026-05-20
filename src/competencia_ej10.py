def simular_ronda(actual, parcial):
    """Calcula el puntaje de cada competidor en la ronda actual
    (suma de los tres jueces) y lo guarda en una lista. Además
    calcula quién fue el ganador de la ronda.
    
    Parámetros
    - actual: diccionario de la clave 'scores'. Contiene el par 
    'nombre': {puntaje de los jueces}
    - parcial: diccionario que almacena el resultado de la ronda actual
    
    Retorno
    - ganador: nombre del ganador de la ronda
    """

    #Itero sobre el diccionario 'scores'
    for indice,competidor in enumerate(actual):
        #Guardo el puntaje de cada participante
        puntajes = list(actual[competidor].values())
        parcial[competidor] = sum(puntajes)
    
    #Obtengo el nombre del ganador
    ganador = max(parcial, key=parcial.get)
    
    return ganador

def imprimir_posiciones(parcial, numero, titulo):
    """Muestra los resultados de la última ronda.
    Ordena el diccionario con los resultados parciales y
    muestra el puntaje de cada competidor de forma descendente
    
    Parámetros:
    - parcial: diccionario que contiene el par 'nombre': puntaje de ronda
    - numero: de la última ronda
    - titulo: de la última ronda
    """
    #Ordeno el diccionario
    parcial = dict(sorted(parcial.items(), key= lambda elem: elem[1], reverse= True))
    
    #Variables usadas dentro del for
    mensaje = f'Ronda {numero} - {titulo}:\n'
    primero = True
    
    for competidor in parcial:
        #Voy añadiendo la información a la cadena mensaje
        if primero:
            mensaje +=f'Ganador/a: {competidor} ({parcial[competidor]})\n'
            primero = False
        else:
            mensaje += f'{competidor} ({parcial[competidor]})\n'
    
    #Imprimo la tabla de posiciones
    print(mensaje)

def guardar_ronda(competidores, parcial, ganador):
    """Guarda la información procesada por simular_ronda() en un diccionario.
    
    Parámetros
    - competidores: el diccionario. Contiene el par 
    'nombre': [puntaje total, puntaje maximo, rondas ganadas]
    - parcial: diccionario que almacena el resultado de la última ronda
    - ganador: de la última ronda
        
    """
    #Itero sobre el diccionario
    for indice,competidor in enumerate(competidores):
        #Sumo el puntaje de la ronda anterior al puntaje total
        competidores[competidor][0] += parcial[competidor]
        #Actualizo el maximo de puntaje de ronda
        if parcial[competidor] > competidores[competidor][1]:
            competidores[competidor][1] = parcial[competidor]
    
    #Sumo una victoria al ganador  
    competidores[ganador][2] += 1

def imprimir_final(competidores):
    """Muestra una tabla con toda la información de la competencia.

    Parámetros:
    - competidores: diccionario que contiene el par 
    'nombre': [puntaje total, puntaje maximo, rondas ganadas]
        
    """
    #Ordeno el diccionario de forma descendente
    competidores = dict(sorted(competidores.items(), key= lambda elem: elem[1][0], reverse= True))
    
    #Imprimo la tabla
    titulo = 'Tabla de posiciones final:\nCocinero     Puntaje     Rondas ganadas     Mejor Ronda     Promedio'
    separador = '-'*70
    print(titulo)
    print(separador)
    
    for competidor in competidores:
        resultado = f'{competidor:<13} {competidores[competidor][0]:<15} {competidores[competidor][2]:<17} {competidores[competidor][1]:<13} {competidores[competidor][0] / 5:.1f}'
        print(resultado)