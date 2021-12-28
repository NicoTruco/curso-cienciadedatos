def condicionReturn(nombre,edad):
    # Observe que al cumplise la condición
    # aplica un return
    if edad >= 100:
        print(nombre, "Felicidades pasaste los 100 años ")
        return
    if edad >= 70:
        print(nombre, "es un Abuelo")
        return
    if edad >= 50:
        print(nombre, "es un Adulto Mayor")
        return
    if edad >= 17:
        print(nombre, "es un persona mayor de Edad")
        return
    print(nombre, "es una persona menor de Edad") 

# Testeamos la aplicación 
# pasando diferentes parámetros

condicionReturn("Harrys", 17);
condicionReturn("Maria", 21);
condicionReturn("Jose", 51);
condicionReturn("Jarina", 75);
condicionReturn("Harrys", 120);
