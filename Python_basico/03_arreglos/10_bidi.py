import numpy as np
import random
matriz = np.empty((5, 5)) # Matriz vacía, con valores residuales de la memoria
arr_suma_col = np.empty(5) 
arr_suma_fila = np.empty(5) 
arr_matriz = np.empty((5, 5)) # Matriz vacía, con valores residuales de la memoria

for x in range(0,5):
   for y in range(0,5):
       nro = random.randint(1,10 )
       matriz[x,y] = nro
       #arr_matriz[y,x] = nro
print(matriz)
#print(arr_matriz)
# Limpio los totales
for x in range(0,5):
    arr_suma_fila[x] = 0
for y in range(0,5):
    arr_suma_col[y] = 0


for x in range(0,5):
   for y in range(0,5):
   	   arr_suma_col[y] = arr_suma_col[y] + matriz[x,y]
   	   arr_suma_fila[x] = arr_suma_fila[x] +  matriz[x,y]

print("x" , arr_suma_col)
print("y" , arr_suma_fila)
print("****************************")

for x in range(0,5):
   for y in range(0,5):
   	  stValor = '{:>4}'.format(str(int(matriz[x,y]))) + " "
   	  print (f"{stValor}" ,end="")
   print("   =  ",end="")
   print( '{:>4}'.format(int(arr_suma_fila[x])))

print("==== ==== ==== ==== ====")

for x in range(0,5):
   print('{:>4}'.format( int(arr_suma_col[x])),end=" ")	
print("")