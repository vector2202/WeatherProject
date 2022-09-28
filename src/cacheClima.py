import json
import urllib
import urllib.request
from datetime import datetime, timedelta
from aeropuerto import Aeropuerto
from urllib.request import urlopen

from datosClima import DatosClima
class CacheClima:
    def __init__(self, tamañoDiccionario) -> None:
        self.cache = [list()]
        self.tamaño = tamañoDiccionario
        for i in range(self.tamaño):
            self.cache.append(list())
            
    def buscarAeropuerto(self, aeropuerto):
        for i in range(self.tamaño):
            if(len(self.cache[(aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño]) == 0):
                return -1
            if(self.cache[(aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño][0] == aeropuerto.nombre):
                return i + aeropuerto.funcionHash(self.tamaño)
        return -1
    """Funcion que busca con una ciudad clima donde esta ubicada en la cache"""
    def refrescar(self, aeropuerto, api):
        indice = self.buscarAeropuerto(aeropuerto)
        if(indice != -1):#Si el clima ya se registro previamente
            if((datetime.now() - self.cache[indice][2]) >= timedelta(minutes=30)):
                #Si ya paso tiempo desde la ultima consulta
                datosJson = self.realizarPeticion(aeropuerto, api)
                self.cache[indice][1] = datosJson
                self.cache[indice][2] = datetime.now()
        else:#Registramos el clima
            for i in range(self.tamaño):
                indice = (aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño
                if(len(self.cache[indice]) == 0): 
                    datosJson = self.realizarPeticion(aeropuerto, api)
                    self.cache[indice] = [aeropuerto.nombre, datosJson, datetime.now()]
                    return
        """Funcion que registra si tenemos que realizar la peticion """
    
    def obtenerClima(self, aeropuerto):
        return DatosClima(self.cache[self.buscarAeropuerto(aeropuerto)][1])
    
    def realizarPeticion(self, aeropuerto, api):
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?lat="\
                + str(aeropuerto.latitud) + "&lon=" + str(aeropuerto.longitud)\
                + "&appid=" + api + "&lang=es"
            f = urllib.request.urlopen(url,timeout=30)
            return json.loads(f.read())
        except urllib.request.HTTPError as error:
            print(error)
            return None
    """Funcion que realiza dada una ciudad y la api su clima en datos json"""
