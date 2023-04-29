from Errores import ignorarComentarios
from DiccionariosyListas import *

class Comando:
    def __init__(self, funcion, nombre=None , json=None) -> None:
        self.funcion=funcion
        self.nombre=nombre
        self.json=json

def buscarJson(data: str):
    data=data.replace("\n","")
    json='{}'
    if ('"{' in data) and ('"}' in data):    #ENCUENTRA EL JSON ENTRE: "{ }"
        json=data[(data.index('"{'))+1:data.index('}"')+1]
        print(json)
            
    return json

def compilar(data):
    listaComandos=[]
    data=ignorarComentarios(data)
    data=data.replace('\n','')
    
    comandos=data.split(';',-1)
    for comand in comandos[0:len(comandos)-1]:
        primera=comand.split('=')[0]
        segunda=comand.split('=')[1]

        funcion=segunda[segunda.index('nueva')+5:segunda.index('(')]
        funcion=funcion.strip()

        entreParentesis=segunda[segunda.index('('):segunda.index(')')+1]

        if entreParentesis == '()':     #SI EL COMANDO NO TIENE DATOS ENTRE EL PARENTESIS
            nombre=primera.split(' ')[1]
            listaComandos.append(Comando(funcion,nombre))
        
        else:
            if ',' in segunda:      #SI TIENE LA COMA ES POR QUE TIENE 2 ATRIBUTOS

                atributos=segunda.split(',')
                nombre=atributos[0].strip().replace('"','')

                json=buscarJson(segunda)

                listaComandos.append(Comando(funcion,nombre,json))

            else:   #SOLO TIENE UN ATRIBUTO ENTRE LOS PARENTESIS
                nombre=entreParentesis.replace('"','')   

                listaComandos.append(Comando(funcion,nombre))   

    info=salida(listaComandos)
    return info

def salida(listaComandos):
    info=''
    print('Cargamdo comandos...')

    for comando in listaComandos:
        comando: Comando
        print('funcion: ',comando.funcion,'.')
        match comando.funcion:

            case 'CrearBD':
                info=info+"use('"+comando.nombre+"');\n"

            case 'EliminarBD':
                info=info+"db.dropDatabase();\n"

            case 'CrearColeccion':
                info=info+"db.createCollection('"+comando.nombre+"');\n"    

            case 'EliminarColeccion':
                info=info+"db."+comando.nombre+".drop();\n"

            case 'InsertarUnico':
                info=info+"db."+comando.nombre+".insertOne("+comando.json+");\n"

            case 'ActualizarUnico':
                info=info+"db."+comando.nombre+".updateOne("+comando.json+");\n"   

            case 'EliminarUnico':
                info=info+"db."+comando.nombre+".deleteOne("+comando.json+");\n"

    print(info)    
    return info

t='InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion" ,\n"\n{\n"nombre" : "Obra Literaria",\n"autor" : "Jorge Luis"\n}\n");'    
#compilar(t)
