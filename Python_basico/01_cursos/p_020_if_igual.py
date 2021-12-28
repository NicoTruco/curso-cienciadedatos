#Método que recibe dos parámetros  Nombre y edad
def condicionNot(nombre,genero):
    # Si No es Igual a "F", Se sale de la rutina
    if genero != "F":  #  en otros lenguajes  permite <>
        print(nombre, "Lo Siento Solo se Admiten Mujeres")
        return
    print(nombre, "Adelante, ********* ")
    

# Testeamos la aplicación 
# pasando diferentes parámetros
    
condicionNot("Maria", "F");
condicionNot("Jose", "M");
condicionNot("Jarina", "F");
condicionNot("Harrys", "M");