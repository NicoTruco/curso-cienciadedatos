def comprar(cigarro,bebida):
    #Si Cualquiera es Verdadero
    if cigarro or bebida:
       return ("Compre Cigarros o Bebida")
    return ("Nada")


# Testeamos la aplicación 
print ("Comprar False True  ==>",comprar(False,True))   
print ("Comprar True  False ==>",comprar(True,False))
print ("Comprar True  True  ==>",comprar(True,True))
print ("Comprar False False ==>",comprar(False,False))
