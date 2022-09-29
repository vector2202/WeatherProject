import json
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
        for i in range(self.tamaño):
            if(len(self.cache[(aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño]) == 0):
                return -1#La casilla esta vacia
            if(self.cache[(aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño][0] == aeropuerto.nombre):
                return i + aeropuerto.funcionHash(self.tamaño)#Encontramos donde esta
        return -1#Nunca estuvo
    """Funcion que busca con una ciudad clima donde esta ubicada en la cache"""
    def refrescar(self, aeropuerto):
        indice = self.buscarAeropuerto(aeropuerto)
        if(indice != -1):#Si el clima ya se registro previamente
            if((datetime.now() - self.cache[indice][2]) >= timedelta(minutes=30)):
                #Si ya paso tiempo desde la ultima consulta
                datosJson = self.realizarPeticion(aeropuerto)
                self.cache[indice][1] = datosJson
                self.cache[indice][2] = datetime.now()
                return False if datosJson == None else True
        else:#Registramos el clima
            for i in range(self.tamaño):
                indice = (aeropuerto.funcionHash(self.tamaño) + i) % self.tamaño
                if(len(self.cache[indice]) == 0): 
                    datosJson = self.realizarPeticion(aeropuerto)
                    self.cache[indice] = [aeropuerto.nombre, datosJson, datetime.now()]
                    return False if datosJson == None else True
        return False
    """Funcion que registra si tenemos que realizar la peticion """
    
    def obtenerClima(self, aeropuerto):
        return DatosClima(self.cache[self.buscarAeropuerto(aeropuerto)][1])
    
    def realizarPeticion(self, aeropuerto):
        try:
            url = "https://api.openweathermap.org/data/2.5/weather?lat="\
                + str(aeropuerto.latitud) + "&lon=" + str(aeropuerto.longitud)\
                + "&appid=" + self.api + "&lang=es"
            f = urllib.request.urlopen(url,timeout=30)
            print("Request exitosa")
            return json.loads(f.read())
        except urllib.request.HTTPError as error:
            print(error)
            return None
    """Funcion que realiza dada una ciudad y la api su clima en datos json"""
