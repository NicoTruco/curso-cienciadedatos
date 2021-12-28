n1 = int(input("Ingrese Nro 1 : "))
n2 = int(input("Ingreso nro 2 : "))
print(f"   nro1 = {n1}    nro2= {n2}")

#  5  > 3
"""
if n1 == n2:
    print(f" Los números son iguales")
else:    
    if n1 > n2:
        print(f"El Nro Mayor es nro1  ={n1} ")
    else:
        print(f"El Nro Mayor es nro2  ={n2} ")    

print("Termino el programa")    
"""

print("Versión 2")
if n1 > n2:
    print(f"El Nro Mayor es nro1  ={n1} ")
else:
    if n1 < n2:
        print(f"El Nro Mayor es nro2  ={n2} ")    
    else:    
        if n1 == n2:  # pregunta demas
            print(f" Los números son iguales")
        else:
            print ("Error")

print("Termino el programa")    