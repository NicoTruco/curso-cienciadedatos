class Persona:
    # Atributo, Propiedades, Valor ,etc
    rut=None
    nombres=None
    apPaterno=None
    apMaterno=None



p1= Persona()
# Esto es un error, asignar despues de haber construido new()
p1.rut = 78
p1.nombres = "Juanito"    
p1.apPaterno = "Harrys"    
p1.apMaterno = "Marilad"    

p2= Persona()    
p2.rut = 98
p2.nombres = "Juanito   98"    
p2.apPaterno = "Harrys   98" 
p2.apMaterno = "Marilad   98" 

p3= Persona()    
p3.rut = 178
p3.nombres = "Juanito 178"    
p3.apPaterno = "Harrys 178"    
p3.apMaterno = "Marilad 178"    

p4= Persona()    
p4.rut = 378
p4.nombres = "Juanito 378"    
p4.apPaterno = "Harrys 378"    
p4.apMaterno = "Marilad 378"    


print(p1.rut,p1.nombres,p1.apPaterno,p1.apMaterno)
print(p2.rut,p2.nombres,p2.apPaterno,p2.apMaterno)
print(p3.rut,p3.nombres,p3.apPaterno,p3.apMaterno)
print(p4.rut,p4.nombres,p4.apPaterno,p4.apMaterno)
