def forRanoInicioFinal(arregloValor):
    # Recorre el arreglo, por cada línea(item)
    # Por cada item extrae los dos campos 
    #  utilizando ==> .items():
    for nombreHarrys,colorHarrys in arregloValor.items():
        print("Fruta", nombreHarrys, "de Color", colorHarrys)
# Testeamos la aplicación 
# Creamos una variable data con 6 posiciones
frutas = {'Fresa':'roja'
        , 'Limon':'verde'
        , 'Papaya':'naranja'
        , 'Manzana':'amarilla'
        , 'Guayaba':'rosa'}
forRanoInicioFinal(frutas)
