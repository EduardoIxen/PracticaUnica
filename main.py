import os.path as path
from ControladorJson import *

opcion = input("Ingrese el comando\n")
opcion=opcion.upper()
while True:
    print(opcion)
    separado = opcion.split(maxsplit=1)
    print(len(separado))
    print(separado[0])
    # print(separado[1])
    if separado[0] == 'CARGAR':
        listaDeArchivos = separado[1].split(sep=',')
        for archivos in listaDeArchivos:
            print(archivos.strip())
            if path.exists(f'entradas/{archivos.strip()}.json'):
                print("Si existe")
                controladorJson = ControladorJson()
                controladorJson.cargarJson(f'entradas/{archivos.strip()}.json')
            elif path.exists(f'entradas/{archivos.strip().lower()}.json'):
                print("Si existe2")
                controladorJson = ControladorJson()
                controladorJson.cargarJson(f'entradas/{archivos.strip().lower()}.json')
            else:
                print("No existe el archivo")
    elif separado[0] == 'SELECCIONAR':
        listaDeAtributos = separado[1].split(sep='DONDE', maxsplit=1)  # crea dos arreglos (atributos y valor ="
        if listaDeAtributos[0].strip() == '*':
            print("Listar todos los atributos")
            controladorJson = ControladorJson()
            controladorJson.seleccionar(listaDeAtributos[0].strip(), listaDeAtributos[1].strip())
        else:
            print("Separar atributos")
            controladorJson = ControladorJson()
            controladorJson.seleccionar(listaDeAtributos[0].strip(), listaDeAtributos[1].strip())
    else:
        print('El comando no existe')

    opcion = input("Ingrese el comando\n")
    opcion = opcion.upper()

'''print("Imprimiendo todos los datos:")
for data in Registro.registros:
    print(data)
print(f'Tipo de archivo cargado: {type(data)}')'''