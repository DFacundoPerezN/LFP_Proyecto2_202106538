from prettytable import PrettyTable
from DiccionariosyListas import*

class Error:

    def __init__(self, tipo, linea, columna, token, description=None) -> None:
        if description==None:
            description=tipo
        self.tipo=tipo
        self.linea=linea
        self.columna=columna
        self.token=token
        self.description=description

    def imprimirError(self, c=0):
        print(c, self.tipo, '| fila:', self.linea, '| columna: ', self.columna, self.token, '| descripcion', self.description)

def revisarErrores(data):
    listaErrores = []
    data=ignorarComentarios(data)
    listaErrores = erroresLexicos(data,listaErrores)
    listaErrores = eroresSintacticos(data,listaErrores)

    table=PrettyTable(['Tipo de Error','Linea','Columna','Token','Descripción'])
    for error in listaErrores:
        error : Error
        table.add_row([error.tipo, error.linea, error.columna, error.token, error.description])

    print(table)
    return table

def ignorarComentarios(data):
    data:str
    
    while '---' in data:    #IGNORA LOS COMENTARIOS ENTRE: "// \n"
        comentario=data[(data.index('---')):len(data)]
        comentario=comentario[0:comentario.index('\n')]
        data=data.replace(comentario,"")
        print('Comentario ignorado: '+comentario)

    while ('/*' in data) and ('*/' in data):    #IGNORA LOS COMENTARIOS ENTRE: "/* */"
        comentario=data[(data.index('/*')):len(data)]
        comentario=comentario[0:comentario.index('*/')+2]
        data=data.replace(comentario,"")        
        print('Comentario ignorado: '+comentario)
    
    return data

def erroresLexicos(data: str, listaErrores:list):
    nFila:int
    nFila=0

    lineas = data.split("\n")
    for linea in lineas:
        nColumna=0
        nFila+=1

        for c in linea:
            nColumna+=1

            if not(c.isdigit()|c.isalpha()or c==" " or c == "{" or c=="}" or c == ":" or c=="," or c == "(" or c==")" or c == "=" or c == "."or c == '"' or c == ";" or c=="$"):
                listaErrores.append(Error('lexico', nFila, nColumna, c, "Caracter no valido"))
    return listaErrores

def eroresSintacticos(data: str, listaErrores:list):

    while ('  'in data): #aseguramos quitar espacios innecesarios
        data=data.replace('  ',' ')
    comandos=data.split(';')

    for comando in comandos[0:len(comandos)-1]:
        comando=comando.strip()
        try:
            comando1=comando.split('(')[0]
            comando2=comando.split('(')[1]
        except:
            saveError(data, listaErrores,comando[comando.index('"')], ')','Error con la apertura de parentesis')

        else:
            comando1=comando1.strip()
            #print(comando1)
            espacios=comando1.split(' ')

            if not(espacios[0] in listaFunciones):#ERROR SI LA FUNCION NO ES VALIDA                
                saveError(data, listaErrores,espacios[0], espacios[0],'La funcion ingresada no existe')    

            for c in espacios[1]:
                if not(c.isdigit()|c.isalpha()):#ERROR SI EL NOMBRE DE LA VARIABLE NO ES VALIDO
                    
                    saveError(data, listaErrores,espacios[1], c,'El nombre de la variable no es valido, solo letras y numeros') 
                
            if not(str(espacios[2])=='='): #ERROR SI SE ESPERABA EL '='
                saveError(data, listaErrores,espacios[2], espacios[2],'Se esperaba el signo =')            

            if not(espacios[3]=='nueva'):   #ERROR SE ESPERABA LA PALABRA 'nueva'
                saveError(data, listaErrores,espacios[3], espacios[3],'Se esperaba la palabra "nueva"')

            if not(espacios[4] in listaFunciones):  #ERROR SI LA FUNCION NO ES VALIDA
                print(espacios)
                saveError(data, listaErrores,espacios[4], espacios[4],'La funcion escrita al final no es valido')

            if len(comando1)<1:         #ERROR SI NO SE ABRIÓ PARENTESIS '('
                saveError(data, listaErrores,espacios[4], '(','No se abrio parentesis')

            if not(comando[-1]==')'):   #ERROR SI NO SE CERRÓ PARENTESIS '('
                saveError(data, listaErrores,comando[-1], ')','No se cerró parentesis')
                
            if not(comando2[0]==')' or comando2[0]=='"'):
                print('PA',comando2)
                saveError(data, listaErrores, comando2[0],comando2[0])

            if comando1[0]=='"':
                pila=1
                for i in comando1:
                    match i:
                        case ')':
                            break
                        case '"':
                            if not(comando1[i-1]==','):
                                if not(comando1[i+1]==')' or comando1[i+1]==','):
                                    saveError(data, listaErrores, comando1[i+1],comando[i+1],'No se cerro correctamente la comilla "')                    
                        case _:
                            i=i
    return listaErrores        

            
def saveError(data, listaErrores, infoError, lexema, des=None):
    #print(data)
    #print(infoError)
    infoFila=data[0:data.index(infoError)]
    nFila=infoFila.count('\n')

    infoColumna=infoFila.split('\n')[-1]
    nColumna=len(infoColumna[0:data.index(infoError)])
    listaErrores.append(Error('Sintactico',nFila, nColumna, lexema, des))
    
t='InsertarUnico insertadoc = nueva InsertarUnico"NombreColeccion" ,\n"\n{\n"nombre" : "Obra Literaria",\n"autor" : "Jorge Luis"\n}\n");'  
t2='InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion" ,\n"\n{\n"nombre" : "Obra Literaria",\n"autor" : "Jorge Luis"\n}\n");'    
#revisarErrores(t)
#revisarErrores(t2)