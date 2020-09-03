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

![cargar](https://user-images.githubusercontent.com/18478169/92063708-07fb3f80-ed59-11ea-8463-8f5cb16eeef6.png)


### Notas
- Los archivos que se desean cargar deben estar dentro de la carpeta **entradas** del proyecto.

- Los archivos deben ser **.json** y deben tener el siguiente formato.

![formatoJson](https://user-images.githubusercontent.com/18478169/92063538-9622f600-ed58-11ea-8af8-ee03618cbc2b.png)

- **SELECCIONAR:** Permite seleccionar uno o más registros o atributos condicionando por medio de los mismos atributos. Los atributos que deseamos obtener deben ir antes despues de la palabra reservada **SELECCIONAR** y antes de la palabra reservada **DONDE**. Para condicionar la seleccion se debe agregar un atributo despues de la palabra reservada **DONDE**.
  - Si se utiliza * en lugar de atributos, automaticamente se seleccionan todos los atributos.
  - Si el atributo que condicionara la seleccion es el nombre, deberá ir dentro de comillas.
 
![seleccionar](https://user-images.githubusercontent.com/18478169/92064529-e13e0880-ed5a-11ea-92be-f386db60f3fa.png)

- **MAXIMO:** Este comando encontrara el valor maximo de alguno de los dos atributos que se cargaron a memoria. Los atributos pueden ser **edad** o **promedio**.

![maximo](https://user-images.githubusercontent.com/18478169/92064755-688b7c00-ed5b-11ea-8cae-87324be2a8a6.png)

- **MINIMO:** Este comando encontrará el valor minimo de las dos variables (**edad** o **promedio**) de los registros que fueron cargados a memoria.

![minimo](https://user-images.githubusercontent.com/18478169/92064918-d0da5d80-ed5b-11ea-9198-07cb11d33590.png)

- **SUMA:** Este comando sumara los atributos permitidos (**edad** o **promedio**) de todos los registros cargados a la memoria.

![suma](https://user-images.githubusercontent.com/18478169/92065184-6aa20a80-ed5c-11ea-84cd-9fd8e1f7f4e2.png)

- **CUENTA:** Permite encontrar el numero de registros cargados a la memoria.

![CUENTA](https://user-images.githubusercontent.com/18478169/92065273-a2a94d80-ed5c-11ea-942a-fb3900d98eca.png)

-**REPORTAR:** Este comando permite crear un reporte en un archivo HTML donde se muestren la **N** cantidad de registros que se desean visualizar.

![reportar](https://user-images.githubusercontent.com/18478169/92069238-1bf96e00-ed66-11ea-981e-81d8c907ce06.png)

![html](https://user-images.githubusercontent.com/18478169/92069328-48ad8580-ed66-11ea-9239-e4ba226b7467.png)
