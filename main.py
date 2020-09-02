import re
import os.path as path
from ControladorJson import *

opcion = input("Ingrese el comando\n")
#opcion=opcion.upper()
while True:
    separado = opcion.split(maxsplit=1)
    #print(len(separado))
    #print(separado[0])
    # print(separado[1])
    if separado[0].upper() == 'CARGAR':   #quitar el .upper
        listaDeArchivos = separado[1].split(sep=',')
        for archivos in listaDeArchivos:
            #print(archivos.strip())
            if path.exists(f'entradas/{archivos.strip()}.json'):
                controladorJson = ControladorJson()
                controladorJson.cargarJson(f'entradas/{archivos.strip()}.json')
                print(f"{archivos.strip()} cargado correctamente!")
                print("////////////////////////////////////////////////////////////")
            elif path.exists(f'entradas/{archivos.strip().upper()}.json'): #cambiar por .lower
                controladorJson = ControladorJson()
                controladorJson.cargarJson(f'entradas/{archivos.strip().lower()}.json') #cambiar por .lower
                print(f"{archivos.strip()} cargado correctamente!")
                print("////////////////////////////////////////////////////////////")
            else:
                print("No existe el archivo ", archivos.strip())
                print("////////////////////////////////////////////////////////////")
    elif separado[0].upper() == 'SELECCIONAR':
        listaDeAtributos = re.split('donde',str(separado[1]),flags=re.IGNORECASE)
        if listaDeAtributos[0].strip() == '*':
            controladorJson = ControladorJson()
            controladorJson.seleccionar(listaDeAtributos[0].strip(), listaDeAtributos[1].strip())
        else:
            try:
                controladorJson = ControladorJson()
                controladorJson.seleccionar(listaDeAtributos[0].strip(), listaDeAtributos[1].strip())
            except IndexError as e:
                print("Formato de entrada no valido")
    elif separado[0].upper() =='MAXIMO':
        if re.search("edad", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.maximo(separado[1].lower().strip())
        elif re.search("promedio", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.maximo(separado[1].lower().strip())
    elif separado[0].upper() == 'MINIMO':
        if re.search("edad", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.minimo(separado[1].lower().strip())
        elif re.search("promedio", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.minimo(separado[1].lower().strip())
    elif separado[0].upper() == 'SUMA':
        if re.search("edad", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.suma(separado[1].lower().strip())
        elif re.search("promedio", separado[1], flags=re.IGNORECASE):
            controladorJson = ControladorJson()
            controladorJson.suma(separado[1].lower().strip())
    elif separado[0].upper() == 'CUENTA':
        controladorJson = ControladorJson()
        controladorJson.cuenta()
    else:
        print('El comando no existe')

    opcion = input("Ingrese el comando\n")