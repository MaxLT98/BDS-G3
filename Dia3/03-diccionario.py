capitales = {
              'Peru' : 'Lima',
              'Ecuador' : 'Quito',
              'Chile' : 'Santiago',
              'Colombia' : 'Bogota'
            }

pais = input ("ingrese el pais ")
capital = capitales.get (pais)
print (f"La capital de {pais} es {capital}")