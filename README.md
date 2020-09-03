# PracticaUnica
Practica única del laboratorio de lenguajes formales.

# Manual de usuario
## Requerimientos
- Tener instalado python en su version 3
- PyCharm

Para usar SimpleQL primero deberá clonar el repositorio en su computadora para eso debera abrir su consola en la direccion donde quiera almacenar el repositorio y digitar el siguiente comando.

```sh
git clone https://github.com/EduardoIxen/PracticaUnica
```
Despues de haber ejecutado el comando, los archivos apareceran en la direccion seleccionada.

![archivosClonados](https://user-images.githubusercontent.com/18478169/92061229-fadb5200-ed52-11ea-81f4-ea321a1596de.png)

## Ejecutar el programa
Una vez clonado el repositorio se procede a cargarlo en pycharm donde se seleccionara el archivo principal que en este caso es el **main.py** y presionando click izquierdo sobre el archivo, se mosotrará una lista donde se seleccionará **Run 'main'** para ejecutarlo.
Del lado derecho de la imagen se observa que el programa ya se esta ejecutando en la consola de Pycharm.

![main](https://user-images.githubusercontent.com/18478169/92062684-860a1700-ed56-11ea-8b6e-0b4160d7f00e.png)

## Funcionalidad
El programa cuenta con varios comandos que tienen diferentes funciones, a continuacion se describen:
- **CARGAR:** Este comando permite cargar diferentes archivos a memoria añadiendole como parametro el nombre de los archivos a cargar.

```sh
CARGAR archivo1,archivo2,...,archivoN
```

### Notas
- Los archivos que se desean cargar deben estar dentro de la carpeta **entradas** del proyecto.

![entrada](https://user-images.githubusercontent.com/18478169/92063384-42b0a800-ed58-11ea-9283-8c2109dcc462.png)

- Los archivos deben ser **.json** y deben tener el siguiente formato.

![formatoJson](https://user-images.githubusercontent.com/18478169/92063538-9622f600-ed58-11ea-8af8-ee03618cbc2b.png)


