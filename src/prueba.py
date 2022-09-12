import urllib.request
import urllib.parse
import http.client
import json
import csv
from datetime import datetime
from datetime import timedelta

class CiudadesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ciudades):
            return [obj.nombre, obj.latitud, obj.longitud]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
class Ciudades:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
    def __str__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) + ", " + str(self.longitud) + "]r"
    def __repr__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) + ", " + str(self.longitud) + "]"
    
def funcionHash(ciudad, n):
    suma = 0
    for caracter in ciudad.nombre:
        suma += ord(caracter)
    return (suma + abs(int(float(ciudad.latitud))) + abs(int(float(ciudad.longitud)))) % n

def buscarCiudadOrigen(listaCiudades, ciudadOrigen, n):
    for i in range(n):
        if(len(listaCiudades[(funcionHash(ciudadOrigen, n) + i) % n]) == 0):
            return -1
        if(listaCiudades[(funcionHash(ciudadOrigen, n) + i) % n][0].nombre == ciudadOrigen.nombre):
            return i + funcionHash(ciudadOrigen, n)
    return -1

def buscarCiudad(listaCiudades, nombreCiudad):
    for ciudadesDestino in listaCiudades:
        if(ciudadesDestino.nombre == nombreCiudad):
            return True
    return False

def escribirDestinos(n):    
    with open('../data/dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        listaCiudades = [list()]
        
        for i in range(n):
            listaCiudades.append(list())
        #Vamos a guardar en el arreglo los n aereopuertos distintos con sus vuelos posibles.
        i = 0;
        for vuelo in reader:
            if(i > 0):
                ciudadOrigen = Ciudades(vuelo[0], vuelo[2], vuelo[3])
                index = buscarCiudadOrigen(listaCiudades, ciudadOrigen, n)
                if(index == -1):
                    for j in range(n):
                        if(len(listaCiudades[(funcionHash(ciudadOrigen, n) + j) % n]) == 0):
                            listaCiudades[(funcionHash(ciudadOrigen, n) + j) % n].append(Ciudades(ciudadOrigen.nombre, float(ciudadOrigen.latitud), float(ciudadOrigen.longitud)))
                            index = (funcionHash(ciudadOrigen, n) + j) % n
                            break
                if(not buscarCiudad(listaCiudades[index], vuelo[1])):
                    listaCiudades[index].append(Ciudades(vuelo[1], float(vuelo[4]), float(vuelo[5])))
            i += 1
            
        for i in range(n):
            if(len(listaCiudades[i]) > 0):
                with open(listaCiudades[i][0].nombre + '.json', 'w') as archivo:
                    json.dump(listaCiudades[i], archivo, indent=4, cls=CiudadesEncoder)
        #Abrimos el json con el codigo del origen:
        #escribimos un array con los destinos posibles en objeto {cod, long, lat}
        #El primer elemento del arreglo sera la informacion del mismo areopuerto
        
def leerDestinos(ciudadOrigen):
    with open(ciudadOrigen + ".json") as archivo:
        destinos = json.load(archivo)
        for destino in destinos:
            if(destino[0] != ciudadOrigen):
                print(destino)
        return destinos
def cargarDatos():
    with open("historial.json") as archivo:
        historial = json.load(archivo)
        return historial
def mostrarClima(datosOrigen, datosDestino):
    print(datosOrigen)
    print(datosDestino)
    historial = open("historial.txt", 'a')
    historial.write(str(datosOrigen) + str(datosDestino) + "\n")
    historial.close()
    #Crearemos un arreglo similar al de donde guardamos los vuelos pero ahora con el clima de cada aereopuerto en tupla con el tiempo cuando lo consultamos, con este tiempo podremos saber si necesitamos volver a calcular o no.
def leerHistorial():
    historial = open("historial.txt", 'r')
    print(historial.read())
    historial.close()
    
def main():
    n = 71
    escribirDestinos(n)
    historialClima = [list()]
    for i in range(n):
        historialClima.append(list())
    ciudadOrigen = Ciudades("MEX", 19.4363, -99.0721)
    api = "9d92b9e2262e46e5b34601d6f706cf43"
    if(len(historialClima[funcionHash(ciudadOrigen, n)]) > 0 and (datetime.now() - historialClima[funcionHash(ciudadOrigen, n)][1]) > datetime.timedelta(hours=0, minutes=30)):
        djsonOrigen = historialClima[funcionHash(ciudadOrigen, n)][0]
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(ciudadOrigen.latitud) + "&lon=" + str(ciudadOrigen.longitud) + "&appid=" + api
        f = urllib.request.urlopen(url,timeout=30)
        djsonOrigen = json.loads(f.read())
        historialClima[funcionHash(ciudadOrigen, n)].append(djsonOrigen)
        historialClima[funcionHash(ciudadOrigen, n)].append(datetime.now())

    destinos = leerDestinos(ciudadOrigen.nombre)
    ciudadDestinoCodigo = input()
    
    
    longitudDestino = 0.0
    latitudDestino = 0.0
    for destino in destinos:
        if (destino[0] == ciudadDestinoCodigo):
            latitudDestino = destino[1]
            longitudDestino = destino[2]
    ciudadDestino = Ciudades(ciudadDestinoCodigo, latitudDestino, longitudDestino)
    if(len(historialClima[funcionHash(ciudadDestino, n)]) > 0 and (datetime.now() - historialClima[funcionHash(ciudadDestino, n)][1]) > datetime.timedelta(hours=0, minutes=30)):
        djsonDestino = historialClima[funcionHash(ciudadOrigen, n)][0]
    else:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitudDestino) + "&lon=" + str(longitudDestino) + "&appid=" + api
        f = urllib.request.urlopen(url,timeout=30)
        djsonDestino = json.loads(f.read())
        historialClima[funcionHash(ciudadOrigen, n)].append(djsonOrigen)
        historialClima[funcionHash(ciudadOrigen, n)].append(datetime.now())
    mostrarClima(djsonOrigen, djsonDestino)
    leerHistorial()
    #print(djson["weather"][0]["description"])
main()
