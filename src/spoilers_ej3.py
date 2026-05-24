#Introducir por teclado una lista de palabras separadas por coma.
#Reemplazar todas las apariciones de cada palabra por asteriscos.
#Mostrar el resultado
def leer_palabras(mensaje):
    """Lee un string por teclado y lo devuelve como una lista de cada palabra.
    Las palabras deben estar separadas por coma.
    Parámetros
        mensaje: texto que muestra en consola con indicaciones
    Retorno
        procesado: lista con las palabras
    """
    
    palabras = input(mensaje)
    limpio = [palabra.strip() for palabra in palabras.split(',')]
    return limpio
    
def procesar_texto(review):
    """Procesa un string recibido como parámetro y censura las palabras leídas por teclado

    Parámetros
        review: string con el texto original
    
    Retorno
        procesado: string con las palabras censuradas
    """
    
    #Creo dos listas con el texto a censurar y las palabras a censurar
    spoilers = leer_palabras('Ingrese las palabras consideradas spoiler (separadas por coma): ')
    review = review.split()
    
    #Recorro spoilers y busco si coincide alguno en review
    for spoiler in spoilers:
        for indice,palabra in enumerate(review):
            #Si encuentro, reemplazo por asteriscos
            if(spoiler.lower() == palabra.lower()):
                review[indice] = '*'*len(palabra)
    
    #Le doy formato string
    procesado = ' '.join(review)
    
    return procesado