import os
import json
from src.aeropuerto import Aeropuerto
from src.codificadorJsonAeropuerto import CodificadorAeropuerto

class ListaDeAeropuertos():
    '''
    Clase con contiene las listas de aeropuertos
    '''
    def __init__(self, tamañoDiccionario) -> None:
        '''
        Atributos de la lista
        '''
        self.tamaño = tamañoDiccionario
        self.lista = [list()]
        for i in range(self.tamaño):
            self.lista.append(list())
            

    def procesarVuelo(self, vuelo):
        '''
        Funcion que nos regresa 
        '''
        if(vuelo == None):
            return -1
        aeropuertoOrigen = Aeropuerto(vuelo[0], float(vuelo[2]), float(vuelo[3]))
        aeropuertoDestino = Aeropuerto(vuelo[1], float(vuelo[4]), float(vuelo[5]))
        indice = self.buscarAeropuertoOrigen(aeropuertoOrigen)
        if(indice == -1):
            indice = self.insertarAeropuertoOrigen(aeropuertoOrigen)
        if(not self.buscarAeropuertoDestino(self.lista[indice],\
                                            aeropuertoDestino.nombre)):
            self.lista[indice].append(aeropuertoDestino)
        return indice


    def buscarAeropuertoOrigen(self, aeropuertoOrigen):
        '''Funcion que busca en el arreglo de aeropuertos, un aeropuerto dado su nombre, si no la encuentra devuelve -1'''
        if(aeropuertoOrigen == None):
            return -1
        for i in range(self.tamaño):
            if(len(self.lista[(aeropuertoOrigen.funcionHash(self.tamaño) + i)\
                              % self.tamaño]) == 0):
                return -1
            if(self.lista[(aeropuertoOrigen.funcionHash(self.tamaño) + i) %\
                          self.tamaño][0].nombre == aeropuertoOrigen.nombre):
                return i + aeropuertoOrigen.funcionHash(self.tamaño)
        return -1


    def insertarAeropuertoOrigen(self, aeropuerto):
        if(aeropuerto == None):
            return -1
        for j in range(self.tamaño):
            if(len(self.lista[(aeropuerto.funcionHash(self.tamaño) + j)\
                              % self.tamaño]) == 0):
                self.lista[(aeropuerto.funcionHash(self.tamaño) + j)\
                           % self.tamaño].append(aeropuerto)
                return (aeropuerto.funcionHash(self.tamaño) + j)\
                    % self.tamaño
        return -1
            
    def buscarAeropuertoDestino(self, listaAeropuerto, nombreAeropuerto):
        '''
        Funcion para poder buscar los aeropuertos destino de la lista
        '''
        for aeropuerto in listaAeropuerto:
            if(aeropuerto.nombre == nombreAeropuerto):
                return True
        return False


    """ Funcion que busca si el aeropuerto de destino ya esta considerada en en arreglo de los destinos del aeropuerto"""
    def escribirAeropuertosJson(self):
        for i in range(self.tamaño):
            if(len(self.lista[i]) > 0):
                with open("datos/" + self.lista[i][0].nombre + '.json', 'w') as archivo:
                    json.dump(self.lista[i], archivo, indent=4, cls=CodificadorAeropuerto)
        return self.revisarArchivosJSON()
    

    def revisarArchivosJSON(self):
        '''
        Funcion que revisa los datos en la lista de los datos en los archivos json
        '''
        for i in range(self.tamaño):
            if(len(self.lista[i]) > 0):
                if(os.path.isfile(r'datos/' + self.lista[i][0].nombre + '.json') == False):
                    return False
        return True


    def obtenerNombres(self):
        '''
        Funcion que nos da una lista con los nombres de los aeropuertos
        '''
        nombresAeropuertos = []
        for aeropuertoOrigen in self.lista:
            if(len(aeropuertoOrigen) > 0):
               nombresAeropuertos.append(aeropuertoOrigen[0].nombre)
        return nombresAeropuertos
