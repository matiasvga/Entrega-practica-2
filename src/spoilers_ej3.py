#Introducir por teclado una lista de palabras separadas por coma.
#Reemplazar todas las apariciones de cada palabra por asteriscos.
#Mostrar el resultado
def procesar_texto(review):
    """Procesa un string recibido como parámetro y censura las palabras leídas por teclado

    Parámetros
        review: string con el texto original
    
    Retorno
        procesado: string con las palabras censuradas
    """
    def leer_palabras():
        """Lee un string por teclado y lo devuelve como una lista de cada palabra

        Retorno
            procesado: lista con las palabras
        """
        
        palabras = input('Ingrese las palabras consideradas spoiler (separadas por coma): ')
        palabras = palabras.split(',')
        limpio = [palabra.strip() for palabra in palabras]
        return limpio
    
    #Creo dos listas con el texto a censurar y las palabras a censurar
    spoilers = leer_palabras()
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