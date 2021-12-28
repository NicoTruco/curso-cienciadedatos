def comprar(cigarro,pan,bebida):
    # Se aconseja a utilizar ()
    #if cigarro or pan and bebida:
    if cigarro or (pan and bebida):
       return ("Compre el mandado")
    return ("Nada")

# Testeamos la aplicación 
print ("Comprar Nada         ==>",comprar(False,False,False))    
print ("Comprar Cigarro      ==>",comprar(True,False,False))
print ("Comprar Pan y Bebida ==>",comprar(False,True,True))
print ("Comprar Pan y Bebida(false) ==>",comprar(False,True,False))
