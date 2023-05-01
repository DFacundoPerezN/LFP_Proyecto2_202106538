# Manual de Usuario
### Descripción
El programa es una herramienta que permita el diseño y creación de sentencias de bases de datos no relacionales de una forma sencilla. La aplicación tendrá un área de edición de código y un área de visualización de la sentencia final generada.
Cuando ya se cuente con las sentencias creadas inicialmente, se procederá a realizar la compilación respectiva lo que generar las sentencias de MongoDB que serán mostradas en el espacio de resultados que posteriormente se podrán aplicar a un entorno adecuado a MongoDb.

## Funcionamiento

Al momento de abrir el programa saldra una interfaz la cual estar conformada por 10 botones, 2 entradas de texto y 3 Areas de Texto.
![imagen](https://user-images.githubusercontent.com/98927736/235376965-9085c612-91f6-4c89-8f78-799e239260ae.png)

Primeramente, se deberá llenar la entrada de texto de arriba con la ubicación y nombre del archivo que deseemos abrir, esto se puede hacer manualmente o automáticamente con el botón de “Buscar Archivo” el cual abrirá el explorador de archivos.
![imagen](https://user-images.githubusercontent.com/98927736/235376970-57903619-c9be-4424-88a6-5a39aef45e01.png)

Al darle en “Abrir” copiara la ruta del archivo en la entrada en la entrada de texto. 
![imagen](https://user-images.githubusercontent.com/98927736/235376984-d8b7872d-163b-4387-b2d3-c9ea7d2906ed.png)

## Opciones de Guardado y Edición de Archivo
Una vez con la dirección del archivo Se le da Al botón de “Abrir Archivo” y este desplegara la información del archivo en el área de texto de la izquierda. 
![imagen](https://user-images.githubusercontent.com/98927736/235376989-c285a4f9-92f0-4059-ae10-a3c6b0ee1a57.png)

Si queremos limpiar el área de texto para empezar a editar uno nosotros mismos le damos al botón “Nuevo Archivo” en el cual si el área de texto esta NO esta en blanco nos preguntara por consola si deseamos guardar los cambios de este.
![imagen](https://user-images.githubusercontent.com/98927736/235376992-a6554182-2070-4be6-8cde-9000891dff96.png)

En caso de presionar cualquier otra tecla no se guardará el archivo. 
En caso de ingresar 1 se preguntará por el nombre y la ruta del archivo antes de limpiar el área de texto. 
![imagen](https://user-images.githubusercontent.com/98927736/235377001-6694762e-42f2-4b05-935b-462b24e7ec5d.png)

Para guardar el archivo que se esta editando en el área de texto del lado izquierdo se cuentan con los botones de “Guardar Archivo” y “Guardar Entrada Archivo Como:”  
![imagen](https://user-images.githubusercontent.com/98927736/235377005-369d125f-6713-415e-9dbc-68626dcd3d3a.png)

La diferencia es que el botón de “Guardar Archivo” guarda la información reescribiendo el archivo que se abrió mientras que “Guardar Entrada Archivo Como: ” usa la barra de texto a su derecha para darle nombre al archivo que se guardara.

## Edición del Archivo
Cuando se esta editando el archivo en el área de texto de la izquierda aparece un texto el cual tiene la posición de donde se está editando. 

![imagen](https://user-images.githubusercontent.com/98927736/235377017-ec719cc3-e1fe-4f3f-9110-ca1a56c74ae7.png)

## Tabla de Tokens
Con el botón de “Ver Tokens” se generará una tabla en el área de texto de la derecha en la que se identifiquen todos los tokens del archivo, estos tomando la información del Área de texto izquierda. 
![imagen](https://user-images.githubusercontent.com/98927736/235377063-1d57a819-a8cf-4899-9f89-c6682f95e05c.png)

Cuando se tiene un json muy largo se da este problema que no cabe todo en area de texto, para eso se puede ver la tabla por consola. 
![imagen](https://user-images.githubusercontent.com/98927736/235377100-03c952e7-3635-403f-ac2a-acd6be145a4e.png)

## Mostrar Errores
Por cada error que haya en la infromacion del area de texto de la izquierda se mostrara en una tabla generarda en el area de texto de la derecha con el boton “Mostrar Errores”. 
![imagen](https://user-images.githubusercontent.com/98927736/235377147-244f95cf-09e2-42c1-8efe-852cfc510989.png)
Esta tabla también se imprime en consola. 

## Generar MongoDB
Con este botón del centro Se generan las sentencias resultado de compilar la información en el área de la izquierda. 
![imagen](https://user-images.githubusercontent.com/98927736/235377227-30d6ff31-920e-428d-9a5c-be86ed153cce.png)

En caso de que haya un error en el archivo este mostrara el mensaje de “Hay errores en el archivo.
 ![imagen](https://user-images.githubusercontent.com/98927736/235377159-1a8ec8ac-44ad-4d41-838b-446c04d787f7.png)

Para guardar la información que se muestra en el área de texto de la derecha Esta el botón de Guardar Archivo resultados el cual leerá la información y la guardara en un archivo con el mismo nombre con el que se abrió solo que con la extensión lfp en lugar de .txt
 ![imagen](https://user-images.githubusercontent.com/98927736/235377161-9a352d15-f902-481f-8732-4f98ed52a17c.png)

Y finalmente con el botón de abajo a la derecha que dice “Salir” se cierra la aplicación. 
![imagen](https://user-images.githubusercontent.com/98927736/235377164-fc7b04e8-cd87-4e0f-beca-817daa83aef5.png)

