
def duracion(playlist):
    #Obtengo los minutos y segundos de cada canción
    #mediante slicing de los valores 'duration'
    minutos = list(map(lambda n: int(n['duration'][0]), playlist))
    segundos = list(map(lambda n: int(n['duration'][2:]), playlist))
    
    #Guardo la sumatoria total de cada uno
    total_minutos = sum(minutos)
    total_segundos = sum(segundos)
    
    #Como los segundos podrían superar el minuto (>60s) le aplico
    #una división entera para guardar los minutos y después me guardo
    #los segundos restantes de la división (<60s)
    total_minutos += total_segundos // 60
    total_segundos = total_segundos % 60
    
    #Muestro la duración total de la playlist
    print(f'Duración total: {total_minutos}m {total_segundos}s')
    
    #Para comparar las canciones necesito la duración de cada una en segundos
    #por lo que creo una lista nueva a partir de la lista de
    #minutos (convertida a segundos) y de la lista de segundos
    conversion = list(map(lambda n: n * 60, minutos))
    
    for n in range(len(conversion)):
        conversion[n] += segundos[n]
    
    #Encuentro la posición de la canción más larga y de la más corta
    indice_max = conversion.index(max(conversion))
    indice_min = conversion.index(min(conversion))
    
    #Muestro el resultado
    print(f'Canción más larga: "{playlist[indice_max]['title']}" ({playlist[indice_max]['duration']})')
    print(f'Canción más corta: "{playlist[indice_min]['title']}" ({playlist[indice_min]['duration']})')
    