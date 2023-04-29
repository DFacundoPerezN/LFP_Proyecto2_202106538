def guardar(datos, nombreYRutaArchivo):

        newFile = open (nombreYRutaArchivo, "w")
        newFile.write(datos)
        newFile.close

        print(datos)
    
