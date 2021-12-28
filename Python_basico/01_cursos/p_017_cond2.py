def condicionMayorIgual(nombre,edad):
    if edad >= 100:
        print(nombre, "Felicidades pasaste los 100 años ")
    else:
        if edad >= 70:
            # si es Mayor de 70 pero menor igual que 100
            print(nombre, "es un Abuelo")
        else:
            if edad >= 50:
                # si es Mayor de 50 pero menor igual que 70
                print(nombre, "es un Adulto Mayor")
            else:
                if edad >= 17:
                    # si es Mayor de 18 pero menor igual que 50
                    print(nombre, "es un persona mayor de Edad")
                else:
                    # si es menor de 18
                    print(nombre, "es una persona menor de Edad")

# Testeamos la aplicación 
# pasando diferentes parámetros

condicionMayorIgual("Harrys", 17);
condicionMayorIgual("Maria", 21);
condicionMayorIgual("Jose", 51);
condicionMayorIgual("Jarina", 75);
condicionMayorIgual("Harrys", 120);
