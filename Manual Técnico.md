# Manual Técnico
### Descripción
El programa es una herramienta que permita el diseño y creación de sentencias de bases de datos no relacionales de una forma sencilla. La aplicación tendrá un área de edición de código y un área de visualización de la sentencia final generada.
Cuando ya se cuente con las sentencias creadas inicialmente, se procederá a realizar la compilación respectiva lo que generar las sentencias de MongoDB que serán mostradas en el espacio de resultados que posteriormente se podrán aplicar a un entorno adecuado a MongoDb.

## Tkinter

- Asi es como se inicializó la ventana en Tkinter, Recordemos que Tkinter es una libreria de python la cual ayuda a la creacion de una interfaz grafica la cual provee de entre muchas cosas de botones, entradas de texto, areas de texto y de etiquetas de exitos.
```
def abrirWindowMA():
    windowP = tk.Tk()
    windowP.title("Menu Archivos")
    windowP.columnconfigure([0,16], minsize=100)
    windowP.rowconfigure([0,8], minsize=100)
    windowP.configure(background="#9980FA")
```
## Guardar Archivo
- Con la funciones que tiene python de leer y abrir archivos es qeu guardamos la informacion en archivos con la siguiente función
```
def guardar(datos, nombreYRutaArchivo):

        newFile = open (nombreYRutaArchivo, "w")
        newFile.write(datos)
        newFile.close

```

La diferencia es que el botón de “Guardar Archivo” guarda la información reescribiendo el archivo que se abrió mientras que “Guardar Entrada Archivo Como: ” usa la barra de texto a su derecha para darle nombre al archivo que se guardara.


## Tabla de Tokens

- La tabla de tokens se genera primero guardando los lexemas leidos y comparandolos en la siguiente funcion se reconocen los token según un diccionario o si este es una palabra reservada. Se hace append en una lista de onjetos abstractos 'Token'.
```
def buscarTokens(data):
    cadena=''
    for c in data:
        if c.isdigit()|c.isalpha():
            cadena=cadena+c

        else:
            if cadena!='':
                print(cadena)
                if cadena in listaFunciones:
                    listaTokens.append(Token('Funcion',cadena)) 

                elif cadena=='nueva':
                    listaTokens.append(Token('Palabra Reservada',cadena))

                else:
                    listaTokens.append(Token('ID',cadena))
                    
                cadena=''

            if c!=' ':
                listaTokens.append(Token(tokensPorLexema[c],c))
```
##  Errores
- Para los Errores lexicos se uso una funcion que revisara caracter por caracter para verificar que fuera válido. 
 ```
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
```

## Compilar
- Se tiene la clase de Comando para guardar la informacion de cada uno 
```
class Comando:
    def __init__(self, funcion, nombre=None , json=None) -> None:
        self.funcion=funcion
        self.nombre=nombre
        self.json=json
```
- Tenemos la funcion de compilar la que lee la informacion y segun el tipo de funcion guarda sus datos en una lista
 ```
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
```
- Con la funcion de salida es que por cada comando en la lista se genera una salida en el lenguaje de mongoDB.
 ```
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
```

## Tabla de Tokens
| Token | Lexema | Patrón|
| ------ | ------ | ------ |
|String| "a-Z"|conjunto de caracteres entre comillas|  
|Funcion| CrearBD |palabras reservadas|
|ID|[a-Z][0-9]|conjunto de letras a veces con números|
|Op Asignacion|=|=|
|Palabra Reservada| nueva| palabra reservada|
|Abrir parentesis| (|(|
|Cerrar parentesis| )|)|
|Separa Comando |;|;|
|Asignación en JSon|:|:|
|Json| formato Json|{id: valor, ...}|
## Metodo del árbol
![imagen](https://user-images.githubusercontent.com/98927736/235448944-8586aa18-a55e-4568-8a46-805b13c4c45d.png)

## AFD del scanner léxico
![imagen](https://user-images.githubusercontent.com/98927736/235448974-957d6ee8-6634-4ebf-bf6d-c06ebce347a1.png)

## Gramática libre de contexto del scanner sintático
![imagen](https://user-images.githubusercontent.com/98927736/235448995-9274f743-53b6-43cc-b27c-69e080bf98f5.png)
