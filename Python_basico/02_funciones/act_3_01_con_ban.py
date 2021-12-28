iva = 0.19  #base de datos
aumento = 5
cn_platano = 0
cn_sandia = 0
cn_uva = 0
seguir = True

while seguir :
    opcion = int(input("1=platano/2= sandia/3=uva/ 0=salir  "))
    if (opcion == 1):
       cn_platano =    cn_platano + aumento   
    if (opcion == 2):
       cn_sandia    = cn_sandia + aumento
    if (opcion == 3):
       cn_uva =    cn_uva + aumento   
    seguir = opcion != 0

print("plantan : " , cn_platano)
print("sandia  : " , cn_sandia)
print("uva     : " , cn_uva)



for x in range(7):
  print("range:",x)
else:
  print("Finally finished!")



  for (x=0;x <10;x++){

  }
  for (x=100;x >-10;x--){
  
  }
  x=100
  for (;;){
    x = x+1
    if (x > 100) break;
  }