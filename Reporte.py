import webbrowser
from Registro import *
import  os.path
from os import remove
from tabulate import *
class Reporte:
    def crearHtml(self, numero):
        contador = 0
        arregloPrincipal = []
        if len(Registro.registros) < numero:
            print(f"Solo se cuenta con {len(Registro.registros)} registros")
        for registro in Registro.registros:
            contador = contador + 1
            if contador <= numero:
                #agregar los registros a una lista auxiliar saber cuantos reportar
                aux=[]
                aux.append(contador)
                aux.append(registro.get('nombre'))
                aux.append(registro.get('edad'))
                aux.append(registro.get('activo'))
                aux.append(registro.get('promedio'))
                #llenar el arreglo del reporte de listas auxiliares
                arregloPrincipal.append(aux)
        #usar tabulate para crear una tabla html en base a la lista que se le pasa como parametro
        content = tabulate(arregloPrincipal, headers=["No.","Nombre","Edad","Activo","Promedio"],tablefmt='html')
        contenidoTabla = str(content)
        contenidoTabla = contenidoTabla.replace('<table>','<table class="table table-striped table-bordered" style="margin: 2%  auto; width:80%" >',1)
        contenidoTabla = contenidoTabla.replace('<thead>','<thead class="thead-dark">',1)
        contenidoTabla = contenidoTabla.replace('right','center')
        contenidoTabla = contenidoTabla.replace('<th>Nombre','<th style="text-align: center;">Nombre' )
        contenidoTabla = contenidoTabla.replace('<th>Activo','<th style="text-align: center;">Activo')
        contenidoTabla = contenidoTabla.replace('<td>', '<td style="text-align: center;">')

        if os.path.exists("entradas/repo.html"):
            remove("entradas/repo.html")

        file = open("entradas/repo.html", "w")

        file.write('<!DOCTYPE html>')
        file.write('<html>')
        file.write('<head>')
        file.write('<title>Reporte</title>')
        file.write('<meta charset="utf-8">')
        file.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
        file.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
        file.write('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')
        file.write('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>')
        file.write('<link rel="stylesheet" href="css/estilo.css">')
        file.write("<style>body{background: rgba(242,246,248,1);background: -moz-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -webkit-gradient(left bottom, right top, color-stop(0%, rgba(242,246,248,1)), color-stop(28%, rgba(216,225,231,1)), color-stop(100%, rgba(104,149,179,1)));background: -webkit-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -o-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: -ms-linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);background: linear-gradient(45deg, rgba(242,246,248,1) 0%, rgba(216,225,231,1) 28%, rgba(104,149,179,1) 100%);filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f2f6f8', endColorstr='#6895b3', GradientType=1 );}"
                   "table{-webkit-box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);-moz-box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);box-shadow: 6px 11px 14px 1px rgba(0,0,0,0.75);}</style>")
        file.write('</head>')
        file.write('<body>')
        file.write('<center>')
        file.write('<h1>Registros</h1>')
        file.write(contenidoTabla)
        file.write('</center>')
        file.write('</body>')
        file.write('</html>')
        file.close()
        #obtiene la ruta absoluta del archivo
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../entradas/repo.html")
        path = path.replace("\\","/")
        path = path.replace("../","")
        webbrowser.open_new_tab(path)
