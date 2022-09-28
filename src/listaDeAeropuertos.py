import json
from aeropuerto import Aeropuerto
from codificadorJsonAeropuerto import CodificadorAeropuerto

class ListaDeAeropuertos():
    def __init__(self, tamañoDiccionario) -> None:
        self.tamaño = tamañoDiccionario
        self.lista = [list()]
        for i in range(self.tamaño):
            self.lista.append(list())
            
    def procesarVuelo(self, vuelo):
        #Inicializamos todas las casillas con listas vacias
        aeropuertoOrigen = Aeropuerto(vuelo[0], float(vuelo[2]), float(vuelo[3]))
        aeropuertoDestino = Aeropuerto(vuelo[1], float(vuelo[4]), float(vuelo[5]))
        indice = self.buscarAeropuertoOrigen(aeropuertoOrigen)
        if(indice == -1):#Si la ciudad no existe, la registramos
            self.insertarAeropuerto(aeropuertoOrigen)
        if(not self.buscarAeropuertoDestino(self.lista[indice],\
                                            aeropuertoDestino.nombre)):
            self.lista[indice].append(aeropuertoDestino)
    
    def buscarAeropuertoOrigen(self, aeropuertoOrigen):
        for i in range(self.tamaño):
            if(len(self.lista[(aeropuertoOrigen.funcionHash(self.tamaño) + i)\
                              % self.tamaño]) == 0):
                return -1
            if(self.lista[(aeropuertoOrigen.funcionHash(self.tamaño) + i)\
                          % self.tamaño][0].nombre == aeropuertoOrigen.nombre):
                return i + aeropuertoOrigen.funcionHash(self.tamaño)
        return -1
    """ Funcion que busca en el arreglo de ciudades, una ciudad dado su nombre, si no la encuentra devuelve -1"""

    def insertarAeropuerto(self, aeropuerto):
        for j in range(self.tamaño):#En la primera posicion disponible a partir de su HK
            if(len(self.lista[(aeropuerto.funcionHash(self.tamaño) + j) % self.tamaño]) == 0):
                self.lista[(aeropuerto.funcionHash(self.tamaño) + j) % self.tamaño].append(aeropuerto)
                return (aeropuerto.funcionHash(self.tamaño) + j) % self.tamaño
            
    def buscarAeropuertoDestino(self, listaAeropuerto, nombreAeropuerto):
        for aeropuerto in listaAeropuerto:
            if(aeropuerto.nombre == nombreAeropuerto):
                return True
        return False
    """ Funcion que busca si la ciudad destino ya esta considerada en en arreglo de los destinos de la ciudad"""
    def escribirAeropuertosJson(self):
        for i in range(self.tamaño):
            if(len(self.lista[i]) > 0):#Para cada ciudad que fue registrada
                #Abrimos el json de la ciudad correspondiente y escribimos la ciudad y todos sus destinos
                with open("data/" + self.lista[i][0].nombre + '.json', 'w') as archivo:
                    json.dump(self.lista[i], archivo, indent=4, cls=CodificadorAeropuerto)
    
    def obtenerNombres(self):
        nombresAeropuertosDestinos = []
        for aeropuertoOrigen in self.lista:
            if(len(aeropuertoOrigen) > 0):
               nombresAeropuertosDestinos.append(aeropuertoOrigen[0].nombre)
        return nombresAeropuertosDestinos
        
