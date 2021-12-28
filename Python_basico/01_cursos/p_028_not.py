#Rutina que devuelve True o False
def funAnd(num1,num2):
    if (num1 and num2):
       return True
    else:
       return False

# Testeamos la aplicación 
# La rutina para 1,1 deviera devolver True    
print ("Val 1,1 Sin Not",funAnd(1,1))
print ("Val 1,1 Con Not",not funAnd(1,1))


