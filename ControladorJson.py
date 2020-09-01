import json
from Registro import *

class ControladorJson:
    def cargarJson(self,ruta):
        print('///////////////////////CARGANDO ARCHIVO JSON///////////////////////')
        with open(ruta) as contenido:
            productos = json.load(contenido)
            for producto in productos:
                #print(producto)
                Registro.registros.append(producto)
            #print(f'Tipo de archivos cargados: {type(producto)}')

    def seleccionar(self, atributos, llave):
        print(atributos)
        if str(atributos) == "*":
            separarLlave = llave.split(sep='=', maxsplit=1)
            print(separarLlave[0])
            print(separarLlave[1])
            for registro in Registro.registros:
                comp = str(registro.get(separarLlave[0].lower().strip()))
                if comp == str(separarLlave[1].strip()):
                    print(registro)
        else:
            atributosSep = atributos.split(sep=',')
            print("entro",atributos)
            separarLlave = llave.split(sep='=', maxsplit=1)
            print(separarLlave[0])
            print(separarLlave[1])
            for registro in Registro.registros:
                comp = str(registro.get(separarLlave[0].lower().strip()))
                if comp == str(separarLlave[1].strip()):
                    for atributo in atributosSep:
                        try:
                            print(f"{atributo.lower()}: ", registro[f'{atributo.lower()}'])
                            print(f"{atributo.lower()}: ", registro['pppp'])
                        except KeyError as e:
                            print(f"El atributo {atributo.lower()} no exixte")
                            break
                        #print(atributo)