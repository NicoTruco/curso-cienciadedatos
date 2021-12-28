#JuanDiegoVargas  
#juanDiegoVargas  ==>Todas las variables inician con minúsculas
       # cada vez que cambia de palabra mayuscula o _
       #juan_diego_vargas
       #juanDiegoVargas


class Persona:
    run = 0
    dv=""
    nombres=""
    apPaterno=""
    apMaterno="" 
    direccion=""
    # self == this
    def __init__(self,run,nombres,apPaterno):
        self.run = run
        self.nombres = nombres
        self.apPaterno = apPaterno
        self.apMaterno = ""
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
print("uno",p1.nombres,p1.apPaterno,p1.direccion,p1.dv)

p1.run = 87 
p1.nombres = "**"
p1.calculaDv()

print("dos",p1.nombres,p1.apPaterno,p1.direccion,p1.dv)

p2 = Persona(15,"----","***") 

print("run1 ",p1.getRun())
print("run2 ",p2.getRun())

#p1.camina()    # Errorrrrrr


Persona.camina()