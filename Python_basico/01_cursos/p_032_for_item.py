def forRanoInicioFinal(msg,arregloValor):
    # Recorre el arreglo, por cada item
    pos=0
    for elemento in arregloValor: #foreach
        print("Número", elemento, msg,arregloValor[pos])
        pos = pos + 1

# Testeamos la aplicación 
# Creamos una variable data con 6 posiciones
data = [100, 400, 5672, 30, 40, 15]
forRanoInicioFinal("1,10 Veces",data)
