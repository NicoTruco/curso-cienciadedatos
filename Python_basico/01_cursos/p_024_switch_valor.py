def zero():
    return "zero"
def one():
    return "one"
def two():
    return "two"
switcher = {
        0: zero,
        1: one,
        2: two
    }
def numeroToString(numero):
    func = switcher.get(numero, "nothing")
    return func()
print("Valor 1",numeroToString(1))      #Salida: One
switcher[1]=two #Cambio el valor de la matriz
print("Valor 1",numeroToString(1)) #Salida: Two