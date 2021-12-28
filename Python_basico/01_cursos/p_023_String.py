def condicionSwitch(genero):
    #Diccionario Clave Valor==> Retorna de inmediato el valor
    return  {
        'F': 'Femenino',
        'M': 'Masculino',
    }.get(genero,'Error en Parámetro')

# Testeamos la aplicación 
print ("Mario",condicionSwitch('M'))
print ("Marisel",condicionSwitch('F'))
print ("Marcos",condicionSwitch('K'))

