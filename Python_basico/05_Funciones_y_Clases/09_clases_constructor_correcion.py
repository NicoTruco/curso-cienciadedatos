class Persona:
    # Atributo, Propiedades, Valor ,etc
    rut=None
    nombres=None
    apPaterno=None
    apMaterno=None
    edad=None
    # Constructor, el cual obliga que cada vez que se realice un new XX()
    # Obliga a pasa los parámetros obligatorios
    def __init__(self,run,nombres,apPaterno,apMaterno,edad=90):
        print("hola")
        # self es lo mismo que this, en otros lenguajes
        self.rut = run
        self.nombres = nombres
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.edad = edad



p1= Persona(78,"nombre 78","Harrys","El simpatico",50)
p2= Persona(1278,"nombre 1278","Harrys222","El simpatico222")
p3= Persona(324378,"nombre 3278","Harrys3333","El simpatico333",15)
p4= Persona(32478,"nombre 34478","Harrys 444","El simpatico444")

print(p1.rut,p1.nombres,p1.apPaterno,p1.apMaterno,p1.edad)
print(p2.rut,p2.nombres,p2.apPaterno,p2.apMaterno,p2.edad)
print(p3.rut,p3.nombres,p3.apPaterno,p3.apMaterno,p3.edad)
print(p4.rut,p4.nombres,p4.apPaterno,p4.apMaterno,p4.edad)
