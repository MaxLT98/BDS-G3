import os

#razon de cambio de dolar a sol
razon = 3.73

bandera = "si"
while (bandera =="si"):
    os.system ("clear")
    print ("===============CONVERSOR DE MONEDA=============")
    
    operacion = int (input (""" Ingrese el tipo de operacion 
                     1) De Soles a Dolares
                     2) de Dolares a Soles
                     """))
    if (operacion == 1):
        os.system ("clear")
        print ("===============CONVERSOR DE SOLES A DOLARES=============")
        soles = float ( input("Ingrese el monto en Soles : "))
        cambio = soles / razon
        print(f" El monto en dolares es de {cambio} ")
    elif (operacion ==2):
        print ("===============CONVERSOR DE DOLARES A SOLES=============")
        dolares = float (input("Ingrese el monto en dolares : "))
        cambio = dolares * razon
        print(f" El monto en soles es de {cambio} ")
    else:
        print (" Esta operacion no existe!!!")
    
    bandera = input ("¿Desea continuar...? (si/no) : ")
