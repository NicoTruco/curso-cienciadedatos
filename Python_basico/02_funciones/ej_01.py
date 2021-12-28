v_pla = 1000
v_san = 2000
c_pla = 0    #total de unidad plata
c_san = 0
c_uva = 0
c_tot_pla = 0
c_tot_san = 0
c_tot_uva = 0
c_tot_fruta = 0
c_fruta = 0
seguir= True
while seguir:
    opcion = input ("Hay clientes S=Si/N=No : ")
    seguir = opcion.upper() == "S"
    if(seguir):
        seguir_compra = True
        while seguir_compra:
            print(" 1.- Platano")
            print(" 2.- Sandia")
            print(" S.- Salir")
            opcion = input (" Ingrese opcion  ")
            seguir_compra = opcion != "S"
            print(" paso  11111")
            if (seguir_compra):
                print(" paso  si compra 2222")
                if opcion == "1":
                    print(" paso  si compra 33333")
                    c_pla = c_pla + 1
                    c_tot_pla = c_tot_pla + v_pla
                if opcion == "2":
                    print(" paso  si compra 4444")
                    c_san = c_san + 1
                    c_tot_san = c_tot_san + v_san
        print("Total platano Vendido Cliente  :  " ,c_pla)
        print("Total platano Vendido Cliente  : $" ,c_tot_pla)



print("Total platano Vendido Dia" ,c_pla)