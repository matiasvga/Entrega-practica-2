def validar_email():
    """Lee un string por teclado y devuelve un mensaje de si es válido o no
    como correo electrónico

    Retorno:
    - string
    """
    email = input('Ingrese un email: ')
    valido = False
    
    separado = list(email)
    
    #Valido si tiene almenos un arroba
    if separado.count('@'):
        pos_arroba = separado.index('@')
        #Valido si en la primera posición ó si en la última posición
        #NO tiene un punto o un arroba
        if not((separado[0] in ('@', '.') or (separado[-1]) in ('@', '.'))):
            #Valido si desde el arroba hasta el último caracter tiene
            #almenos un punto
            if separado[pos_arroba:-1].count('.'):
                separado.reverse()
                pos_ultimo = separado.index('.')
                #Valido si, a partir del último punto, tiene dos o
                #más caracteres
                if pos_ultimo >= 2:
                    valido = True

    if valido:
        return 'El email es válido.'
    else:
        return 'El email no es válido.'