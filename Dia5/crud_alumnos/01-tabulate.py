from tabulate import tabulate

data = [
    ["100", "max laura ", "max@gmail.com"],
    ["200", "rodrigo manuel", "rodrigo@gmail.com"],
    ["300", "manuel hinojoza ", "manuel@gmail.com"],
]

columnas = [ "DNI" , "NOMBRE" , "EMAIL" ]

tabla = tabulate (data,headers = columnas,tablefmt ="simple_grid" )

print (tabla)
