from DiccionariosyListas import *
from prettytable import PrettyTable
from Errores import ignorarComentarios

t='InsertarUnico insertadoc = nueva InsertarUnico("NombreColeccion" ,\n"\n{\n"nombre" : "Obra Literaria",\n"autor" : "Jorge Luis"\n}\n");'
listaTokens=[]

class Token:

    def __init__(self, token, lexema):
        self.token=token
        self.lexema=lexema
        try:
            self.numeroToken=numerosPorTokens[token]
            if self.numeroToken==None:
                self.numeroToken='15'
        except:
            self.numeroToken='15'

    def imprimirToken(self, c=0):
        print(c, self.tipo, '| fila:', self.linea, '| columna: ', self.columna, self.token, '| descripcion', self.description)

def buscarJson(data: str):
    data=data.replace("\n","")

    while ('"{' in data) and ('"}' in data):    #ENCUENTRA EL JSON ENTRE: "{ }"
        json=data[(data.index('"{')):data.index('}"')+2]
        data=data.replace(json[0:len(json)],'')
        listaTokens.append(Token('Json',json[1:len(json)-1]))
        #print(data)
            
    return data

def buscarEntreComillas(data: str):

    while ('"' in data):    #ENCUENTRA EL STRING ENTRE: ""
        inicio=data.index('"')        
        cadena='"'

        
        cadena=data[inicio:len(data)]
        cadena1=cadena[1:len(cadena)]
        #print('inicio',cadena1,'fin')
        final=cadena1.index('"')+2
        cadena=cadena[0:final]     

        '''
        for c in data[inicio:len(data)]:
            if c!='"':
                cadena=cadena+c
                print(cadena)
            else:
                cadena=cadena+c
                break
            print(cadena)'''
        

        data=data.replace(cadena,'')
        listaTokens.append(Token('String',cadena))

    return data

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

def encontrarTokens(data):
    data=ignorarComentarios(data)
    data=buscarJson(data)
    data=buscarEntreComillas(data)
    #print(data)
    buscarTokens(data)

    #text='------------------------------------------------------------------------------------------------\n'
    text=PrettyTable(['Correlativo','Token','Número','Lexema'])
    cToken=1
    for token in listaTokens:
        token:Token
        '''text=text+'#'+str(cToken)+' | '+ token.token +' | '+ token.numeroToken +' |'+ token.lexema+'| \n'
        text=text+"------------------------------------------------------------------------------------------------\n "'''
        text.add_row([cToken,token.token, token.numeroToken, token.lexema])
        cToken+=1

    print(text)
    return text

#encontrarTokens(t)