def sumar(n1,n2):
    resultado = n1 + n2 
    return resultado

def sumar_con_mensaje(n1,n2):
    resultado = int(n1) + int(n2)
    print (f'la suma de {n1} + {n2} es {suma}')


n1 = input ("ingrese el nro 1 : ")
n2 = input ("ingrese el nro  2: ")

suma = sumar(int(n1) , int(n2))

print (f'la suma de {n1} + {n2} es {suma}')

sumar_con_mensaje (n1,n2)




