
listaFunciones=['CrearBD','EliminarBD','CrearColeccion','EliminarColeccion','InsertarUnico','ActualizarUnico','EliminarUnico','BuscarTodo','BuscarUnico']

numerosPorTokens={'ID':'1', 'Funcion':'2','Palabra Reservada':'3', 
               'Op Asignacion':'4','Abre Llave':'5', 'Cierra Llave':'6',
               'Definicion DosPuntos':'7','Separa datos':'8', 'Punto':'9',
               'Abre Parentesis':'10','Cierra Parentesis':'11', 'Separa Comando':'12'
               , 'Json':'13', 'String':'14'}

tokensPorLexema={'=':'Op Asignacion','{':'Abre Llave','}':'Cierra Llave',
                 '(':'Abre Parentesis',')':'Cierra Parentesis',';':'Separa Comando',
                 ',':'Separa datos','.':'Punto',':':'Definicion DosPuntos'}

salidasFunciones={}