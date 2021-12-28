#JuanDiegoVargas  
#juanDiegoVargas  ==>Todas las variables inician con minúsculas
       # cada vez que cambia de palabra mayuscula o _
       #juan_diego_vargas
       #juanDiegoVargas


class Persona:
    run = 0
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


p1 = Persona(788111,"Juanquin Andres","Baeza")    
print("uno",p1.nombres,p1.apPaterno,p1.direccion)

p1.run = 87 
p1.nombres = "**"

print("dos",p1.nombres,p1.apPaterno,p1.direccion)

