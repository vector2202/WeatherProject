import csv
import json

from src.listaDeAeropuertos import ListaDeAeropuertos


def revisarFormatoVuelo(vuelo):
    if(type(vuelo[0]) != str or type(vuelo[1]) != str or \
       type(vuelo[2]) != float or type(vuelo[3]) != float or\
       type(vuelo[4]) != float or type(vuelo[5]) != float):
        return False
    return True

def revisarCsv(nombreArchivo):
    with open('datos/' + nombreArchivo, 'r') as archivo:
        next(archivo)
        vuelos = csv.reader(archivo)
        for vuelo in vuelos:
            if(len(vuelo) != 6 or revisarFormatoVuelo(vuelo)):
                return False
        return True
"""Funcion que verifica que el formato del csv sea correcto"""

def escribirDestinos(nombreArchivo, tamañoDiccionario):
    with open('datos/' + nombreArchivo, 'r') as archivo:
        next(archivo)
        vuelos = csv.reader(archivo)
        lista = ListaDeAeropuertos(tamañoDiccionario)
        for vuelo in vuelos:
            lista.procesarVuelo(vuelo)
        
        lista.escribirAeropuertosJson()
        return lista
"""Funcion que escribe en un 'Nombre'.json para cada ciudad de origen, escribe los destinos disponibles, recibe un n que es el tamño de la tabla hash """

def leerDestinos(nombreAeropuertoOrigen):
    try:
        destinos = []
        with open("datos/" + nombreAeropuertoOrigen + ".json") as archivo:
            datos = json.load(archivo)
            for dato in datos:
                destinos.append(dato)
            return destinos
    except OSError as error:
        return None
""" Leemos con la ciudad de origen todos sus destinos posibles"""
