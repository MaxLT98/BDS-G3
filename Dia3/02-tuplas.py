#TUPLAS : IGUAL A LISTAS PERO NO CAMBIAN DE VALOR
dias = ("lunes" , "martes" , "miercoles")
print (dias)

#AGREGAR VALOR A LA TUPLA , SE CONVIERTE LA TUPLA EN LISTA
print (type(dias))
dias = list(dias)
print (type(dias))
dias.append("jueves")
dias.append("viernes")

print (dias)

dias = tuple(dias)
print (type(dias))

for dias in dias:
    print (dias)
    