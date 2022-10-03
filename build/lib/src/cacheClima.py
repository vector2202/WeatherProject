import json
from types import NoneType
import urllib
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from src.datosClima import DatosClima

class CacheClima:
    def __init__(self, tamañoDiccionario) -> None:
        self.cache = [list()]
        self.tamaño = tamañoDiccionario
        self.api = ''
        for i in range(self.tamaño):
            self.cache.append(list())


    def actualizarAPI(self, api):
        self.api = api
        

    def buscarAeropuerto(self, aeropuerto):
        '''
        Funcion que busca con una ciudad clima donde esta ubicada en la cache
        '''
        if(aeropuerto == None):
            return -1
        for i in range(self.tamaño):
            if(len(self.cache[(aeropuerto.funcionHash(self.tamaño)\
                               + i) % self.tamaño]) == 0):
                return -1
            if(self.cache[(aeropuerto.funcionHash(self.tamaño) + i)\
                          % self.tamaño][0] == aeropuerto.nombre):
                return i + aeropuerto.funcionHash(self.tamaño)
        return -1


    def refrescarClima(self, aeropuerto):
        '''
        Funcion que registra si tenemos que realizar la peticion
        '''
        if(aeropuerto == None):
            return False
        indice = self.buscarAeropuerto(aeropuerto)
        if(indice != -1):
            if((datetime.now() - self.cache[indice][2]) >= timedelta(minutes=30) or self.cache[indice][1] == None):
                datosJson = self.realizarPeticion(aeropuerto)
                self.cache[indice][1] = datosJson
                self.cache[indice][2] = datetime.now()
            return False if self.cache[indice][1] == None else True
        else:#Registramos el clima
            for i in range(self.tamaño):
                indice = (aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño
                if(len(self.cache[indice]) == 0): 
                    datosJson = self.realizarPeticion(aeropuerto)
                    self.cache[indice] = [aeropuerto.nombre, datosJson, datetime.now()]
                    return False if datosJson == None else True
        return False
    

    def obtenerClima(self, aeropuerto):
        if(self.buscarAeropuerto(aeropuerto) == -1):
            return None
        return DatosClima(self.cache[self.buscarAeropuerto(aeropuerto)][1])
    

    def realizarPeticion(self, aeropuerto):
        '''
        Funcion que realiza dada una ciudad y la api su clima en datos json
        '''
        if(aeropuerto == None):
            return None
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?lat="\
                + str(aeropuerto.latitud) + "&lon=" + str(aeropuerto.longitud)\
                + "&appid=" + self.api + "&lang=es"
            f = urllib.request.urlopen(url,timeout=30)
            return json.loads(f.read())
        except urllib.request.HTTPError as error:
            print(error)
            return None
