#Método que recibe dos parámetros
# Nombre y edad
def condicion(nombre,edad):
    # Condición que detemina cual print realizar
    # Observe los ":" del if  ==> Then
    # Observe los ":" del Else
    if edad < 18:
        # si es menor de 18
        print(nombre, "es una persona menor de Edad")
        return
    
    # como se utilizó return no es necesario el else
    # si es Mayor de 18
    print(nombre, "es un persona mayor de Edad")

condicion("Harrys", 17);
condicion("Maria", 21);
