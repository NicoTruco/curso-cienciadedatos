invertido = []
palabra = []
palabra_input="car"
def leer_palabra_input():
	#palabra_input = input("Ingrese una palabra_input :")
	palabra_input =  "carlos hola como estas"
	print(len(palabra_input))
	for x  in range (0,len(palabra_input)):
		print(x)
		palabra.append(palabra_input[x])
def alt_1():
	print(f"palabra_input :" ,palabra_input)
	for x  in range (0,len(palabra_input)):
	    #print(palabra_input[x],end='')
	    print(palabra_input[14-x],end='')
	    invertido.append(palabra_input[14-x])

def alt_2():
	print(f"palabra_input :" ,palabra_input)
	for x  in range (0,len(palabra_input)):
	    #print(palabra_input[x],end='')
	    print(palabra_input[(len(palabra_input)-1)-x],end='')
	    invertido.append(palabra_input[(len(palabra_input)-1)-x])

def alt_3():
	print(f"palabra_input :" ,palabra)
	for x  in range (0,len(palabra)):
	    print(palabra[(len(palabra)-1)-x],end='')
	    invertido.append(palabra[(len(palabra)-1)-x])

#alt_1() # debe tener 14 caracteres 
#alt_2()
leer_palabra_input()	    
alt_3()
print(palabra)

print(invertido)