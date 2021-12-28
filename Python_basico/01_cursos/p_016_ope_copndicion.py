#Método que recibe dos parámetros
# Nombre y edad
def condicionMenorIgual(nombre,edad):
    if edad <= 17:
        # si es menor o igual que 17
        print(nombre, "es una persona menor de Edad :",edad)
    else:
        if edad <= 50:
            # si es Mayor de 18 pero menor igual que 50
            print(nombre, "es un persona mayor de Edad")
        else:
            if edad <= 70:
                # si es Mayor de 50 pero menor igual que 70
                print(nombre, "es un Adulto Mayor")
            else:
                if edad <= 100:
                    # si es Mayor de 70 pero menor igual que 100
                    print(nombre, "es un Abuelo")
                else:
                    print(nombre, "Felicidades pasaste los 100 años ")


# Testeamos la aplicación 
# pasando diferentes parámetros

condicionMenorIgual("Harrys", 17);
condicionMenorIgual("Maria", 21);
condicionMenorIgual("Jose", 51);
condicionMenorIgual("Jarina", 75);
condicionMenorIgual("Harrys", 120);
