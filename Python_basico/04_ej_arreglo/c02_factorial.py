def factorial (nro):
	suma=1
	for x in range(1,8):
		suma = suma * x
	return suma


res = factorial(7)
print(f"resultado {res}")