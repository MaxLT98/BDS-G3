capitales = {
             'Peru' : 'Lima',
             'Ecuador' : 'Quito',
             'Chile' : 'Santiago',              
             'Colombia' : 'Bogota'
           }

print ('-'*50 + "RECORRIDO POR CLAVES")

#recorrido por claves

for clave in capitales.keys():
    print(clave)

    print ('='*50)

print ('-'*50 + "RECORRIDO POR VALORES")

#recorrido por valores 
for valor in capitales.values():

    print(valor)

print ('-'*50 + "RECORRIDO POR CLAVES Y VALORES")
#recorrido por clabe y valor 

for clave,valor in capitales.items():
    print(f'la capital de {clave} es {valor} ')