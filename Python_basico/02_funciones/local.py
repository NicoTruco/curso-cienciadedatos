import os
def clear(): 
    os.system('cls') #on Windows System
def espacios(cuantos):
	stLinea = ""
	for x in range(0,cuantos):
		stLinea = stLinea + " "
	return stLinea
def menu():
	clear()
	for x in range(1,10):
	    print("")
	spa=40
	print(espacios(spa),"    Menu")
	print(espacios(spa),"    ====")
	print("")
	print(espacios(spa),"0.- Salir")
	print(espacios(spa),"1.- Abrir Caja")
	print(espacios(spa),"2.- Cerrar Caja")
	print(espacios(spa),"3.- Comprar")
	print(espacios(spa),"4.- Vender")
	

menu()	
#uno = input("Detiene")