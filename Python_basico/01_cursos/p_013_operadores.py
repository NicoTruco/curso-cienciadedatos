
# retorna la suma dos números pasados por parámetros
def suma(num1, num2):    
    return num1+num2    

# retorna la resta dos números pasados por parámetros    
def resta(num1, num2):    
    return num1-num2    
    
# retorna la multiplicación dos números 
# pasados por parámetros    
def multiplicacion(num1, num2):    
    return num1*num2

# retorna la división dos números 
# pasados por parámetros    
def division(num1, num2):    
    return num1/num2 

# retorna la división entera dos números 
# pasados por parámetros    
def divisionEntera(num1, num2):    
    return num1//num2       

# retorna la módulo (resto) de dos números
# pasados por parámetros    
def modulo(num1, num2):    
    return num1%num2 #    15 mod 10 = 5

# retorna la negación  de un número
# pasados por parámetros    
def negacion(num1):    
    return -num1 


# LLamada del Método, con dos parámetros
# El cual retorna un valor
resultado = suma(3,12)
print ("El Resultado de la suma es :", resultado)


# En vez de utilizar una variable de retorno
# imprimimos de inmediato el resultado
print ("Suma", suma(3,3),suma(4,5))    
print ("Resta", resta(3,3),resta(4,5))    
print ("Multiplicacion", multiplicacion(3,3),multiplicacion(4,5))    
print ("division", division(3,3),division(4,5))    
print ("division Entera", divisionEntera(6,3),divisionEntera(4,5))    
print ("Modulo", modulo(13,3),modulo(4,5))    
print ("Negación", negacion(13)) 


#resto 25 % 7 = 3 = 3*7  =21 == 25 -21 = 4