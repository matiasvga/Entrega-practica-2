#Introducir una lista de nombres separados por coma
#Asignar a cada uo una persona amigo invisible
#Nadie debe tenerse a si mismo
#Al menos 3 participantes
#No debe haber duplicados
import random

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
    
def hacer_sorteo():
    """A partir de una lista con nombres le asigna a cada uno un amigo
    invisible y lo muestra por consola.
    """
    nombres = leer_palabras('Ingrese los participantes (separados por coma): ')
    control = True
    
    while(control):
        #Verifico que hayan al menos tres participantes
        if len(nombres) >= 3:
            minusculas = [elem.lower() for elem in nombres]
            
            #Verifico que no hayan nombres duplicados
            if len(nombres) == len(set(minusculas)):
                print('Sorteo de amigo invisible: ')
                copia = nombres[:]
                
                #Hago len(nombres) asignaciones de amigos invisibles
                for i in range(len(nombres)):
                    distinto = True
                    
                    #Mientras los dos nombres sean la misma persona, sigo
                    #generando dos parejas hasta que sean distintos
                    while(distinto):
                        primero = random.randrange(len(nombres))
                        segundo = random.randrange(len(copia))
                        if nombres[primero] != copia[segundo]:
                            
                            #Si son dos nombres distintos entonces los muestro
                            print(f'{nombres[primero]} -> {copia[segundo]}')
                            
                            #Elimino a ambos de sus listas para que no
                            #se repitan
                            nombres.remove(nombres[primero])
                            copia.remove(copia[segundo])
                            distinto = False
                
                #Termina el bucle de control
                control = False
            else:
                #Caso duplicados
                print('Se detectaron nombres duplicados. Intente otra vez.')
                nombres = leer_palabras('Ingrese los participantes (separados por coma): ')
        else:
            #Caso participantes insuficientes
            print('No hay suficientes participantes. Intente otra vez.')
            nombres = leer_palabras('Ingrese los participantes (separados por coma): ')