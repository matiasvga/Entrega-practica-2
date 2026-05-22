def obtener_tendencias(publicaciones):
    hashtags = {}

    for publicacion in publicaciones:
        separado = publicacion.split()
        
        for palabra in separado:
            if '#' in palabra:
                if palabra in hashtags:
                    hashtags[palabra] += 1
                else:
                    hashtags[palabra] = 1
    
    hashtags = dict(sorted(hashtags.items(), key= lambda elem: elem[1], reverse= True))
    
    print('Hashtags trending (más de una aparición):')
    for clave in hashtags:
        if hashtags[clave] > 1:
            print(f'    {clave}: {hashtags[clave]}')
    
    print()
    print(f'Total de hashtags únicos: {len(hashtags)}')