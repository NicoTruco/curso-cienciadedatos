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
    def moverIzq(self):
        print("Mover Izquiersa",self.nombres)
    def moverDerecha(self):
        print("Mover moverDerecha",self.nombres)
    def moverUp(self,cuantos=1):
        print("Mover moverUp",self.nombres, "se mueve :", cuantos)

    def __str__(self):
        return self.nombres + " > " + self.apPaterno + " > " + self.apMaterno

p1= Persona(78,"Harrys","Harrys","El simpatico",50)
p2= Persona(1278,"Pdero","Harrys222","El simpatico222")
p3= Persona(324378,"mario","Harrys3333","El simpatico333",15)
p4= Persona(32478,"Tati","Harrys 444","El simpatico444")

# Casting print, Imprime, no puede imprimir objetos
# casting implicito del To String
print(p1)
print(p2)
print(p3)
print(p4)
