def forBreak():
    for x in range(1,4):
        for y in range(5,10):
            print("X,Y", x, "Valor y",y)
# Break corta solo el For más cercano
            if x == 2 and y == 6: 
                break

# Testeamos la aplicación 
forBreak()
