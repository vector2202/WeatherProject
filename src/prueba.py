import urllib.request
import urllib.parse
import http.client
import numpy
import json
import csv

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ciudades):
            return [obj.nombre, obj.longitud, obj.latitud]
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
    
def funcionHash(vuelo, n):
    suma = 0
    for caracter in vuelo[0]:
        suma += ord(caracter)
    return (suma + abs(int(float(vuelo[2]))) + abs(int(float(vuelo[3])))) % n
def buscarCiudadOrigen(listaCiudades, vuelo, n):
    for i in range(n):
        if(len(listaCiudades[(funcionHash(vuelo, n) + i) % n]) == 0):
            return -1
        if(listaCiudades[(funcionHash(vuelo, n) + i) % n][0].nombre == vuelo[0]):
            return i
    return -1
def buscarCiudad(listaCiudades, nombreCiudad):
    #print("Buscando " + nombreCiudad + " con " + str(len(listaCiudades)))
    #print(listaCiudades)
    for ciudadesDestino in listaCiudades:
        if(ciudadesDestino.nombre == nombreCiudad):
            return True
    return False

def escribirDestinos():    
    with open('../data/dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        #Tenemos que crear un arreglo que en vuelos[origen] = {vuelosDestino}
        #posteriormente recorremos el arreglo y escribimos todos los vuelos destino en los origen.json
        listaCiudades = [list()]
        n = 71
        for i in range(n):
            listaCiudades.append(list())
        #Vamos a guardar en el arreglo los n aereopuertos distintos con sus vuelos posibles.
        i = 0;
        for vuelo in reader:
            if(len(listaCiudades[0]) > 0):
                print("Mexico0 se ha creado")
            if(len(listaCiudades[1]) > 0):
                print("Mexico1 se ha creado")
            if(i > 0):
                index = buscarCiudadOrigen(listaCiudades, vuelo, n)
                if(index == -1):
                    for j in range(n):
                        if(len(listaCiudades[(funcionHash(vuelo, n) + j) % n]) == 0):
                            listaCiudades[(funcionHash(vuelo, n) + j) % n].append(Ciudades(vuelo[0], float(vuelo[2]), float(vuelo[3])))
                            index = (funcionHash(vuelo, n) + j) % n
                            print("La ciudad " + vuelo[0] + " se esta creando, hk: " + str(index))    
                            break
                    print("Acabamos")
                if(not buscarCiudad(listaCiudades[index], vuelo[1])):
                    listaCiudades[index].append(Ciudades(vuelo[1], float(vuelo[4]), float(vuelo[5])))
            i += 1
        for i in range(n):
            if(len(listaCiudades[i]) > 0):
                print("La ciudad " + listaCiudades[i][0].nombre + " en el indice " + str(i))
        #row[0] contiene cdO, [1] cdD, [2] origenLat, [3] longOrigen, [4] latDest, [5] longDest
        
        #Abrimos el json con el codigo del origen:
        #escribimos un array con los destinos posibles en objeto {cod, long, lat}
        #El primer elemento del arreglo sera la informacion del mismo areopuerto
        
def leerDestinos():
    print("Leyendo los destinos")
    ciudadOrigen = "Aca"
    with open(ciudadOrigen + ".json") as archivo:
        datos = json.load(archivo)
    print(datos)
    #Leeremos los destinos y los guardamos en un arreglo
    
def guardarClima():
    print("Guardando el clima en una cache")
    #Crearemos un arreglo similar al de donde guardamos los vuelos pero ahora con el clima de cada aereopuerto en tupla con el tiempo cuando lo consultamos, con este tiempo podremos saber si necesitamos volver a calcular o no.

def main():
    escribirDestinos()
    
    #url = "https://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid=9d92b9e2262e46e5b34601d6f706cf43"
    #f = urllib.request.urlopen(url,timeout=30)
    #djson = json.loads(f.read())
    #print(djson)
    #print(djson["weather"][0]["description"])

main()
