import random
vector_numeros = []
for  x in range(0,20):
    #print(x)
    #vector_numeros[x] = random.randint(1,10 )
    vector_numeros.append(random.randint(1,10 ))
    #print(f"posicion {x} =  {vector_numeros[x]}")




for  x in range(0,len(vector_numeros)):
    print(f"posicion {x} =  {vector_numeros[x]}")
print("Finalice",len(vector_numeros),vector_numeros)    
print()    