arr_notas = [1,2,3,4,5]
def leer_notas():
	arr_notas = [6,3,3,3,8] 
	return arr_notas



arr_notas = leer_notas()
nota_contar = 0
nota_media = 0
nota_menor = 99999
nota_mayor = 0
for x in range(0,len(arr_notas)):
	if(arr_notas[x] > nota_mayor):
		nota_mayor = arr_notas[x]
	if(arr_notas[x] < nota_menor):
		nota_menor = arr_notas[x]
	if (arr_notas[x] >= 4):
		nota_media = nota_media + arr_notas[x]
		nota_contar = nota_contar + 1

#nota_media = nota_media / len(arr_notas)
nota_media = nota_media / nota_contar

for x in range(0,len(arr_notas)):
    print(f"Nota Nro {x + 1} : {arr_notas[x]}")


print(f"Nota Menor  : {nota_menor}")    
print(f"Nota Mayor  : {nota_mayor}")    
print(f"Nota Meida  : {nota_media}")  



#print ("Notas :",arr_notas)