class Persona:
    
    def __init__(self,run,nombres,apPaterno,apMaterno="***"):
        self.run = run
        self.nombres = nombres
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.direccion = ""
        self.dv = "*"

    def calculaDv(self):
        self.edad = 18
        self.dv = "9"
    # Get Set
    def getRun(self):
        return self.run

    def camina():
        print("Caminando")

p1 = Persona(788111,"Juanquin Andres","Baeza")    
p2 = Persona(788111,"Juanquin Andres","Baeza","Garcia")    

p1.calculaDv()
p2.calculaDv()
print("Ape",p1.apMaterno,p2.apMaterno)
print("edad1",p1.edad)
print("edad2",p2.edad)