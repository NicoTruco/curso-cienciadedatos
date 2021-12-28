def calculaDvNro(run):
    stRun =  "" + str(run)
    print("Entro a calculaDv",stRun)
    """
    n1 = stRun[0:1]
    n2 = stRun[1:2]
    n3 = stRun[2:3]    #== 2 ,1
    print("Dv1",n1)
    print("Dv2",n2)
    print("Dv3",n3)
    """
    suma = 0
    nMul = 2
    for x in range (len(stRun)-1,-1,-1):
        nx= stRun[x:x+1]

        resMul = int(nx) * nMul
        suma = suma + resMul

        #print(f"x:{x} dig:{nx}  nMul:{nMul} resMul:{resMul} suma:{suma}")

        nMul = nMul + 1
        if nMul >= 8:
        	nMul = 2
    #print (f"Total {suma}")
    divTruncado = int(suma / 11)
    #print(f"divTruncado {divTruncado}")
    nroNuevo = divTruncado * 11
    diferencia = suma  - nroNuevo
    #print(f"diferencia {diferencia}")
    dv1 = 11 - diferencia
    #print(f"dv1 {dv1}") 
    if (dv1== 11):
    	return 0
    if (dv1== 10):
    	return 'K'
    return dv1




digito = calculaDvNro(20419227)
print(f"digito1 : {digito}")
#            01234567            
digito = calculaDvNro(20901792)    
print(f"digito2 : {digito}")
#calculaDvNro(1)    



20901792
01234567

7-0 = 7
7-1  =6
7-2 = 5 


0