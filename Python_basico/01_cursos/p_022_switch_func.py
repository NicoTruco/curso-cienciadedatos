def one():
    return "January Mes 1"
def two():
    return "February Mes 2"
def three():
    return "March Mes 3"
def condicionSwitch(mes):
    #Diccionario Clave Valor==> pero Funciones
    switchMes = {
        1: one,
        2: two,
        3: three,
    }
    # Retorna Valor, Recordar que es una función
    funccionXX =  switchMes.get(mes, lambda:"Opción Invalida Texto")
    return funccionXX() #Retorna la función
# Testeamos la aplicación 
print ("Mes",condicionSwitch(1))
print ("Mes",condicionSwitch(2))
print ("Mes",condicionSwitch(5))
