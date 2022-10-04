import csv
import json
from src.listaDeAeropuertos import ListaDeAeropuertos

def revisarFormatoVuelo(vuelo):
    '''
    Funcion para revisar formato de los vuelos para que sea compratible
    '''
    if(type(vuelo[0]) != str or type(vuelo[1]) != str or \
       type(vuelo[2]) != float or type(vuelo[3]) != float or\
       type(vuelo[4]) != float or type(vuelo[5]) != float):
        return False
    return True


def revisarCSV(nombreArchivo):
    '''
    Funcion que verifica que el formato del csv sea correcto
    '''
    if(type(nombreArchivo) != str or len(nombreArchivo) < 1):
        return False
    with open('datos/' + nombreArchivo, 'r') as archivo:
        next(archivo)
        vuelos = csv.reader(archivo)
        for vuelo in vuelos:
            if(len(vuelo) != 6 or revisarFormatoVuelo(vuelo)):
                return False
        return True


def escribirDestinos(nombreArchivo, tamañoDiccionario):
    '''
    Funcion que escribe en un 'Nombre'.json para cada aeropuerto de origen, escribe los destinos disponibles, recibe un n que es el tamño de la tabla hash
    '''
    if(type(nombreArchivo) != str or len(nombreArchivo) < 1):
        return ListaDeAeropuertos(tamañoDiccionario)
    with open('datos/' + nombreArchivo, 'r') as archivo:
        next(archivo)
        vuelos = csv.reader(archivo)
        lista = ListaDeAeropuertos(tamañoDiccionario)
        for vuelo in vuelos:
            lista.procesarVuelo(vuelo)
        
        lista.escribirAeropuertosJson()
        return lista


def leerDestinos(nombreAeropuertoOrigen):
    '''
    Leemos con el aeropuerto de origen todos sus destinos posibles
    '''
    if(type(nombreAeropuertoOrigen) != str or len(nombreAeropuertoOrigen) < 1):
        return None
    try:
        destinos = []
        with open("datos/" + nombreAeropuertoOrigen + ".json") as archivo:
            datos = json.load(archivo)
            for dato in datos:
                destinos.append(dato)
            return destinos
    except OSError as error:
        return None
