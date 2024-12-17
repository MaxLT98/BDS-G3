dic_empresas = {}
def cargar_empresas(nombre_archivo):
    archivo = open(nombre_archivo,'r')
    str_empresas = archivo.read()
    archivo.close()

    lista_empresas = str_empresas.splitlines()
    for str_fila in lista_empresas:
        lista_fila = str_fila.split(',')
        dic_registro = {
           'razon_social':lista_fila[1],
           'direccion' :lista_fila[2]
        }
        dic_nueva_empresa = {
            lista_fila[0] : dic_registro
        }
        dic_empresas.update(dic_nueva_empresa)


cargar_empresas('empresas.txt')
print(dic_empresas)

def grabar_alumnos(file_name):
    str_empresas = ""
    for empresa_ruc,empresa_valor in dic_empresas.items():
        str_empresas += empresa_ruc
        for registro_clave,registro_valor in empresa_valor.items():
            str_empresas += registro_valor
            if registro_clave != 'direccion':
                str_empresas += ','
            else:
                str_empresas += '\n'
    
    fsalida = open(file_name,'w')
    fsalida.write(str_empresas)
    fsalida.close()