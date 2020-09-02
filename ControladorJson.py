import json
import re
import  operator
from Registro import *

class ControladorJson:
    def cargarJson(self,ruta):
        with open(ruta) as contenido:
            productos = json.load(contenido)
            for producto in productos:
                Registro.registros.append(producto)
            #print(f'Tipo de archivos cargados: {type(producto)}')

    def seleccionar(self, atributos, llave):
        if str(atributos) == "*":
            separarLlave = llave.split(sep='=', maxsplit=1)
            #print(separarLlave[0])
            #print(separarLlave[1])
            if str(re.search("nombre", str(separarLlave[0]))) != "None":
                nombreBuscar2 = str(separarLlave[1].replace("\"", ""))
                nombreBuscar = str(separarLlave[1].replace("\"", "\'"))
                if re.search('^\'.*\'$', nombreBuscar):
                    for registro in Registro.registros:
                        comp = str(registro.get(separarLlave[0].strip()))
                        if comp == nombreBuscar2:
                            print(registro)
                    print("////////////////////////////////////////////////////////////")
                else:
                    print("El nombre no esta entre comillas")
            else:
                for registro in Registro.registros:
                    comp = str(registro.get(separarLlave[0].lower().strip()))
                    if comp == str(separarLlave[1].strip()):
                        print(registro)
                print("////////////////////////////////////////////////////////////")
        else:
            atributosSep = atributos.split(sep=',')
            separarLlave = llave.split(sep='=', maxsplit=1)
            #print(separarLlave[0])
            #print(separarLlave[1])
            #print(re.search("nombre", str(separarLlave[0])))
            #print(type(re.search("nombre", str(separarLlave[0]))))
            if str(re.search("nombre", str(separarLlave[0]))) != "None":
                nombreBuscar = str(separarLlave[1].replace("\"","\'"))
                if re.search('^\'.*\'$',nombreBuscar):
                    nombreBuscar2 =str(separarLlave[1].replace("\"",""))
                    for registro in Registro.registros:
                        comp = str(registro.get(separarLlave[0].strip()))
                        #print("lo que vamos a comp",comp)
                        if comp == nombreBuscar2:
                            for atributo in atributosSep:
                                try:
                                    print(f"{atributo.lower().strip()}: ", registro[f'{atributo.lower().strip()}'])
                                except KeyError as e:
                                    print(f"El atributo {atributo.lower().strip()} no exixte")
                            print("////////////////////////////////////////////////////////////")
                else:
                    print("El nombre no esta entre comillas.")
            else:
                for registro in Registro.registros:
                    comp = str(registro.get(separarLlave[0].lower().strip()))
                    if comp == str(separarLlave[1].strip()):
                        for atributo in atributosSep:
                            try:
                                print(f"{atributo.lower().strip()}: ", registro[f'{atributo.lower().strip()}'])
                            except KeyError as e:
                                print(f"El atributo {atributo.lower().strip()} no exixte")
                            #print(atributo)
                        print("////////////////////////////////////////////////////////////")

    def maximo(self,atributo):
        listaEdad = []
        listaPromedio = []
        if atributo == 'edad':
            for registro in Registro.registros:
                edad = registro.get('edad')
                listaEdad.append(edad)
            print("La edad maxima es de", max(listaEdad))
        elif atributo == 'promedio':
            for registro in Registro.registros:
                promedio = registro.get('promedio')
                listaPromedio.append(promedio)
            print("El promedio maximo es de",max(listaPromedio))

    def minimo(self,atributo):
        listaEdad = []
        listaPromedio = []
        if atributo == 'edad':
            for registro in Registro.registros:
                edad = registro.get('edad')
                listaEdad.append(edad)
            print("La edad minima es de", min(listaEdad))
        elif atributo == 'promedio':
            for registro in Registro.registros:
                promedio = registro.get('promedio')
                listaPromedio.append(promedio)
            print("El promedio minimo es de", min(listaPromedio))

    def suma(self,atributo):
        listaEdad = []
        listaPromedio = []
        if atributo == 'edad':
            for registro in Registro.registros:
                edad = registro.get('edad')
                listaEdad.append(edad)
            print("La suma de edades es:", sum(listaEdad))
        elif atributo == 'promedio':
            for registro in Registro.registros:
                promedio = registro.get('promedio')
                listaPromedio.append(promedio)
            print("La suma de promedios es:", sum(listaPromedio))

    def cuenta(self):
        total = 0
        for numRegistro in Registro.registros:
            total = total+1
        print("El numero total de cuentas registradas es: ",total)