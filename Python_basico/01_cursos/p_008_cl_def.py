class Persona:
    run = 0
    dv=""
    nombres=""
    apPaterno=""
    apMaterno="" 
    direccion=""
    # self == this
    def __init__(self,run,nombres,apPaterno,apMaterno="***"):
        self.run = run
        self.nombres = nombres
        self.apPaterno = apPaterno
        self.apMaterno = apMaterno
        self.direccion = ""
        self.dv = "*"

    def calculaDv(self):
        self.dv = "9"
    # Get Set
    def getRun(self):
        return self.run

    def camina():
        print("Caminando")

p1 = Persona(788111,"Juanquin Andres","Baeza")    
p2 = Persona(788111,"Juanquin Andres","Baeza","Garcia")    

print("Ape",p1.apMaterno,p2.apMaterno)