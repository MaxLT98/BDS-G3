#parametros args y kargs
def sumar_infinito(*args):
    resultado = 0
    for numero in args:
        resultado = resultado + numero  
    
    return resultado

suma1 = sumar_infinito(3.3,4,5,6,7,8,9,10)
print(suma1)


def calculadra (**kwargs):
    ope = kwargs.get('ope')
    n1 = kwargs.get('n1')
    n2 = kwargs.get('n2')

    if ope == "suma":
        resultado = n1 + n2
    elif ope == "resta":
        resultado = n1- n2
    elif ope == "multiplicar":
        resultado = n1 * n2
    elif ope == "dividir":
        resultado = n1 / n2
    else:
        print ('no se encontro la funcion nombrada')

suma3 = calculadra(n1 = 5 , n2=10 , ope ='suma')
resta1 = calculadra(n1 = 5 , n2=10 , ope ='resta')
dividir1 = calculadra(n1 = 5 , n2=10 , ope ='dividir')
multiplicar1 = calculadra(n1 = 5 , n2=10 , ope ='multiplica')
print (suma3)
print (resta1)
print (multiplicar1)
print (dividir1)

