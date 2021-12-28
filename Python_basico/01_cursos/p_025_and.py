def funAnd(num1,num2):
    if num1 >= 0 and num2 >= 0:
       return ("Ambas variables son Positivas")
    if num1 < 0 and num2 < 0:  
       return ("Ambas variables son Negativas")
    if num1 < 0 :  
       return ("N1 es Negativa")
    if num2 < 0 :  
       return ("N2 es Negativa")

# Testeamos la aplicación 
    
print ("Val -1,0",funAnd(-1,0))
print ("Val 0,-2",funAnd(0,-2))
print ("Val 0,0",funAnd(0,0))
print ("Val -20,-10",funAnd(-20,-10))