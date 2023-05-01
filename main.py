import tkinter as tk
import Guardar
import tkinter.filedialog
import Errores
import Tokens
import Compilar

def buscarArchivo(textBox1):    
    textBox1.delete("0","end")
    ruta=tk.filedialog.askopenfilename()
    textBox1.insert(0,ruta)

def nuevoArchivo(espacio, nombreArchivo='Archivo.lfp'):
    info=espacio.get("1.0", "end")
    #print(espacio)
    if(info.replace('\n','')!=""):
        option=input('¿Desea guardar el archivo que estaba editando? \n1. Para si, cualquier otra para no>>')

        if(option=='1'):
            nombreArchivo=input('Ingrese nombre y direccion para guardar el archivo>>')
            Guardar.guardar(info, nombreArchivo)  
            
    espacio.delete("1.0", "end")

def abrirArchivo(espacio, ruta):
    espacio.delete("1.0", "end")
    File = open (ruta, "r")
    info = File.read()
    espacio.insert("insert", info)

def guardarArchivo(datos,nombreArchivo='Archivo.lfp'):
    print('Guardando Archivo...')
    Guardar.guardar(datos, nombreArchivo)

def revisionErrores(data, espacio):    
    data=data.replace('\t','')   
    espacio.delete("1.0", "end")
    print('revisando los errores')
    tabla=Errores.revisarErrores(data)
    espacio.insert("insert", tabla)

def verTokens(data, espacio):       
    data=data.replace('\t','')   
    espacio.delete("1.0", "end")
    print('revisando los errores')
    tabla=Tokens.encontrarTokens(data)
    espacio.insert("insert", tabla)

def generarMongoDB(data,espacio):       
    data=data.replace('\t','')   
    espacio.delete("1.0", "end")
    tablaErrores=Errores.revisarErrores(data)
    lineas=str(tablaErrores)
    #print('Lineas: ',len(lineas))
    if len(lineas)>231:
        salida=('Hay errores en el archivo')
        try:
            Compilar.compilar(data)
        except:
            print('Hay errores en el archivo')
    else:        
        salida=Compilar.compilar(data)
    espacio.insert("insert", salida)


def abrirWindowMA():
    windowP = tk.Tk()
    windowP.title("Menu Archivos MongoDB")
    windowP.columnconfigure([0,16], minsize=100)
    windowP.rowconfigure([0,8], minsize=100)
    windowP.configure(background="#9980FA")
    posicion="Linea X, Columna Y"

    label1 = tk.Label(windowP, text="Ruta del Archivo Con Nombre:" , bg="#9980FA")
    label1.grid(row=0,column=1)

    textBox1 = tk.Entry(windowP, text="")
    textBox1.grid(row=0,column=2)

    textArea1= tk.Text(windowP, height=40, width=60)
    textArea1.grid(row=4,column=1, padx=5,pady=5)

    label2 = tk.Label(windowP, text=posicion , bg="#9980FA")
    label2.grid(row=4,column=2)

    textArea2= tk.Text(windowP, height=40, width=75)
    textArea2.grid(row=4,column=4, padx=5,pady=5)

    def llamado(event):
        x,y=textArea1.index(tk.INSERT).split(".") 
        posicion=(f"Linea: {x}, Columna: {y}")
        label2 = tk.Label(windowP, text=posicion , bg="#9980FA")
        label2.grid(row=4,column=2)

    textArea1.bind("<Key>",llamado)
    textArea1.bind("<Button-1>",llamado)

    button0= tk.Button(windowP, text ="Buscar Archivo" ,  command=lambda: buscarArchivo(textBox1) , bg="#f9ca24") #Boton de Buscar Archivo
    button0.grid(row=0,column=4)

    button1= tk.Button(windowP, text ="Nuevo Archivo", command=lambda: nuevoArchivo(textArea1, textBox1.get()), bg="#686de0") 
    button1.grid(row=1,column=1, padx=5,pady=5)

    button2= tk.Button(windowP, text ="Abrir Archivo", command=lambda: abrirArchivo(textArea1, textBox1.get()), bg="#686de0") #Abre el Archivo para poder editarlo
    button2.grid(row=1,column=2, padx=5,pady=5)

    button3= tk.Button(windowP, text ="Guardar Archivo", command=lambda: guardarArchivo(textArea1.get("1.0", "end"),textBox1.get()), bg="#686de0") #Guarda el archivo
    button3.grid(row=1,column=4, padx=5,pady=5)

    textBox2 = tk.Entry(windowP)  
    textBox2.grid(row=1,column=6)

    button5= tk.Button(windowP, text ="Guardar Entrada Archivo Como: ", command=lambda: guardarArchivo(textArea1.get("1.0", "end"), textBox2.get()) , bg="#686de0") #Guarda el Archivo con el nombre especificado
    button5.grid(row=1,column=5, padx=5,pady=5)

    button6= tk.Button(windowP, text ="Generar MongoDB",command=lambda: generarMongoDB(textArea1.get("1.0", "end"),textArea2), bg="#7ed6df") #Imprime la informacion presente en el archivo
    button6.grid(row=2,column=2, padx=10,pady=10)

    button7= tk.Button(windowP, text ="Ver Tokens",command=lambda: verTokens(textArea1.get("1.0", "end"),textArea2), bg="#7ed6df")   #Revisa los Errores del Archivo
    button7.grid(row=2,column=4, padx=10,pady=10)

    button8= tk.Button(windowP, text ="Mostrar Errores",command=lambda: revisionErrores(textArea1.get("1.0", "end"),textArea2), bg="#7ed6df")   #Revisa los Errores del Archivo
    button8.grid(row=2,column=5, padx=10,pady=10)

    button9= tk.Button(windowP, text ="Guardar Archivo Resultados", command=lambda: guardarArchivo(textArea2.get("1.0", "end"), textBox2.get().replace(".txt",".lfp")) , bg="#FDA7DF")
    button9.grid(row=3,column=5, padx=5,pady=5)

    button10= tk.Button(windowP, text ="Salir",command=windowP.destroy, bg="#ff6b6b")   #Botón de regresar
    button10.grid(row=7,column=5)

    windowP.mainloop()
abrirWindowMA()