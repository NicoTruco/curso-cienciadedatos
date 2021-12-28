def forRanoInicioFinal(msg,num1,num2):
    # Range parámetros inicio y Final
    for x in range(num1,num2+1):
        print("Número", x, msg)

# Testeamos la aplicación 
forRanoInicioFinal("1,10 Veces",1,10)
print("******************")
forRanoInicioFinal("5,10 Veces",1,5)
