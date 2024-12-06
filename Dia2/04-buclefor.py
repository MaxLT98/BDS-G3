#BUCLE FOR
# for contador in range (1,11,2):
#   print (contador)
numero1 = input ("tabla del numero : ")

for contador in range(1,13):
    tabla = int(numero1) * contador
    print (f" {numero1} x {contador} = {tabla}")
