#Se ingresa un peso y una zona
#Local:    1kg 500, 1-5kg 1000, >5kg 2000
#Regional: 1kg 1000, 1-5kg 2500, >5kg 5000
#Nacional: 1kg 2000, 1-5kg 4500, >5kg 8000
#Si la zona no es válida debe devolver un error
def leer_datos():
    """Lee por teclado el peso y zona del envio.
    Si el peso introducido es mayor a cero continúa con la ejecución.
    Si es menor a cero entonces termina la lectura y devuelve valores
    predeterminados.

    Returns:
        peso: int
        zona: str
    """
    try:
        peso = float(input('Ingrese el peso del paquete (kg): '))
    except ValueError:
        print('Error: el valor introducido no es un número.')
        peso = 0

    if peso > 0:
        zona = input('Ingrese la zona del destino (local/regional/nacional): ')
        
        while not(zona.lower() in ('local', 'regional', 'nacional')):
            print('Zona no válida. Las zonas disponibles son: local, regional, nacional.')
            zona = input('Ingrese la zona del destino (local/regional/nacional): ')
    else:
        peso = 0
        zona = ''
    
    return peso, zona.lower()

def calcular_costo():
    """Calcula el costo del envío según los datos introducidos por teclado.
    Termina la ejecución si se introduce el peso cero o negativo.
    """
    print('(terminar programa introduciendo peso cero)')
    
    precios = {
        'local': [500, 1000, 2000],
        'regional': [1000, 2500,5000],
        'nacional': [2000, 4500, 8000]
    }
    
    peso, zona = leer_datos()
    
    #Si el peso no es cero entonces elije entre las tres tarifas según
    #el peso. (<1kg pos 0, 1-5kg pos 1, >5kg pos 2)
    while peso != 0:
        if (peso > 0) and (peso <= 1):
            resultado = precios[zona][0]
        elif (peso > 1) and (peso <= 5):
            resultado = precios[zona][1]
        elif peso > 5:
            resultado = precios[zona][2]
            
        print(f'Costo de envío: {resultado}')
        
        peso, zona = leer_datos()
    print('Fin del programa.')