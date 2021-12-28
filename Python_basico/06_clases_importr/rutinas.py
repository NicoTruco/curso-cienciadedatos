#método
def sumar_i2(n1,n2):
	#print("ini 3")
	total=n1+n2 #+ 1000
	#print("fin 3")
	return total


def sumar_i1(n1,n2):
	#print("ini 2")
	total=  sumar_i2(n1,n2)
	#print("fin 2")
	return total

def sumar(n1,n2):
	#print("ini 1")
	total= sumar_i1(n1,n2)
	#print("fin 1")
	return total


