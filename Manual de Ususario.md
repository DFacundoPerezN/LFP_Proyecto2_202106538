# Manual de Usuario
### Descripción
El programa es una herramienta que permita el diseño y creación de sentencias de bases de datos no relacionales de una forma sencilla. La aplicación tendrá un área de edición de código y un área de visualización de la sentencia final generada.
Cuando ya se cuente con las sentencias creadas inicialmente, se procederá a realizar la compilación respectiva lo que generar las sentencias de MongoDB que serán mostradas en el espacio de resultados que posteriormente se podrán aplicar a un entorno adecuado a MongoDb.

## Funcionamiento

Al momento de abrir el programa saldra una interfaz la cual estar conformada por 10 botones, 2 entradas de texto y 3 Areas de Texto.
```
imagen
```
Primeramente, se deberá llenar la entrada de texto de arriba con la ubicación y nombre del archivo que deseemos abrir, esto se puede hacer manualmente o automáticamente con el botón de “Buscar Archivo” el cual abrirá el explorador de archivos.
```
imagen
```
Al darle en “Abrir” copiara la ruta del archivo en la entrada en la entrada de texto. 
```
imagen
```
## Opciones de Guardado y Edición de Archivo
Una vez con la dirección del archivo Se le da Al botón de “Abrir Archivo” y este desplegara la información del archivo en el área de texto de la izquierda. 
```
imagen
```
Si queremos limpiar el área de texto para empezar a editar uno nosotros mismos le damos al botón “Nuevo Archivo” en el cual si el área de texto esta NO esta en blanco nos preguntara por consola si deseamos guardar los cambios de este.
```
imagen
```
En caso de presionar cualquier otra tecla no se guardará el archivo. 
En caso de ingresar 1 se preguntará por el nombre y la ruta del archivo antes de limpiar el área de texto. 
```
imagen
```
Para guardar el archivo que se esta editando en el área de texto del lado izquierdo se cuentan con los botones de “Guardar Archivo” y “Guardar Entrada Archivo Como:”  
```
imagen
```

La diferencia es que el botón de “Guardar Archivo” guarda la información reescribiendo el archivo que se abrió mientras que “Guardar Entrada Archivo Como: ” usa la barra de texto a su derecha para darle nombre al archivo que se guardara.

## Edición del Archivo
Cuando se esta editando el archivo en el área de texto de la izquierda aparece un texto el cual tiene la posición de donde se está editando. 
```
imagen
```
## Tabla de Tokens
Con el botón de “Ver Tokens” se generará una tabla en el área de texto de la derecha en la que se identifiquen todos los tokens del archivo, estos tomando la información del Área de texto izquierda. 
```
imagen
```
Cuando se tiene un json muy largo se da este problema que no cabe todo en area de texto, para eso se puede ver la tabla por consola. 
```
imagen
```
## Mostrar Errores
Por cada error que haya en la infromacion del area de texto de la izquierda se mostrara en una tabla generarda en el area de texto de la derecha con el boton “Mostrar Errores”. 
 ```
imagen
```
Esta tabla también se imprime en consola. 
## Generar MongoDB
Con este botón del centro Se generan las sentencias resultado de compilar la información en el área de la izquierda. 
```
imagen
```
En caso de que haya un error en el archivo este mostrara el mensaje de “Hay errores en el archivo.
 
Para guardar la información que se muestra en el área de texto de la derecha Esta el botón de Guardar Archivo resultados el cual leerá la información y la guardara en un archivo con el mismo nombre con el que se abrió solo que con la extensión lfp en lugar de .txt
 
Y finalmente con el botón de abajo a la derecha que dice “Salir” se cierra la aplicación. 

