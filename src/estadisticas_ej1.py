import string

def analizar_texto(texto):
    def separar_lineas(texto,cant):
        """
        -Recibe el texto y la cantidad de líneas
        -Guarda dentro de una lista cada línea del texto por separado
        -Devuelve la lista
        """
        
        lista = []
        for n in range(cant-1):
            lista.append(texto[:texto.find('.\n')+1])
            aux = texto[texto.find('.\n')+2:]
            texto = aux
        lista.append(texto[:])
        return lista
    
    def contar_lineas(texto):
        """
        -Recibe el texto
        -Cuenta cada ocurrencia del salto de línea lo cual equivale
        a una línea nueva (y si la última línea no tiene dicho salto
        la cuenta igual)
        -Devuelve la cantidad de lineas
        """
        
        lineas = texto.count('.\n')

        if not(texto.endswith('\n')):
            lineas += 1
        return lineas
    
    def contar_palabras(texto):
        """
        -Recibe el texto
        -Lo divide en una lista con cada palabra
        -Devuelve la longitud de dicha lista lo cual equivale al total
        de palabras
        """
        
        return len(texto.split())
    
    def encontrar_mayores(lista,cant,prom):
        """
        -Recibe una lista con las líneas del texto, la cantidad de lineas, 
        y el promedio de palabras por línea
        -Crea un diccionario que guarda una línea como clave y la cantidad de
        palabras como valor. Luego crea un String con cada línea que supere el
        promedio de palabras por línea
        -Devuelve el String
        
        """
        
        dic = {lista[n]: len(lista[n].split()) for n in range(cant)}
        resultado = f'Líneas por encima del promedio ({promedio})\n'
        for n in range(cant):
            if(dic[lista[n]] > prom):
                resultado += f'- {lista[n]} ({dic[lista[n]]}) palabras\n'
        return resultado
    
    #Variables
    cantidad_lineas = contar_lineas(texto)
    cantidad_palabras = contar_palabras(texto)
    promedio = cantidad_palabras / cantidad_lineas
    lista = separar_lineas(texto, cantidad_lineas)
    
    #Lo que va a devolver la función
    resultado = """
    Total de líneas: {0}
    Total de palabras: {1}
    Promedio de palabras por línea: {2}
    
    {3}
    """.format(cantidad_lineas,
               cantidad_palabras,
               promedio,
               encontrar_mayores(lista,cantidad_lineas,promedio))
    
    return resultado