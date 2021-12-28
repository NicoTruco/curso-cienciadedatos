# Método que recibe dos parámetros  Nombre y edad
# Dependiendo de la edad, puede o no ganar un Regalo
def condicionIgual(nombre,edad):
    # Observe que para compara
    # Ocupamos dos (==) igual
    if edad == 100:
        print(nombre, "Felicidades, Ganaste un 10% de AFP ")
        return
    if edad == 70:
        print(nombre, "Felicidades,Ganaste un Viaje Miami")
        return
    if edad == 50:
        print(nombre, "Felicidades,Ganaste un Vehículo")
        return
    print(nombre, "Lo Siento No tienes Regalo")
   
# Testeamos la aplicación 
# pasando diferentes parámetros
condicionIgual("Maria", 21);
condicionIgual("Jose", 50);
condicionIgual("Jarina", 70);
condicionIgual("Harrys", 100);
