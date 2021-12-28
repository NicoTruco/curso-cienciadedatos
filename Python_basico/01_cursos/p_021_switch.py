def condicionSwitch(mes):
    #Diccionario Clave Valor
    # Si es 1, Devuelve January, etc
    jj = {
        1: "January",
        2: "February",
        3: "March",
    }
    # Retorna Valor, si no existe devuelve un texto
    return jj.get(mes, "Opción Invalida Texto")

# Testeamos la aplicación 

print ("Mes",condicionSwitch(1))
print ("Mes",condicionSwitch(2))
print ("Mes",condicionSwitch(5))
