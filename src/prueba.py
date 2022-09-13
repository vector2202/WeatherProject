import urllib.request
import urllib.parse
import http.client
import json
import csv
from datetime import datetime, timedelta


class CiudadesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ciudades):
            return [obj.nombre, obj.latitud, obj.longitud]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
    """Esta ciudad convierte el objeto Ciudades en un formato json para escribir en los archivos json"""
    
class Ciudades:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
    def __str__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) + ", " + str(self.longitud) + "]"
    def __repr__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) + ", " + str(self.longitud) + "]"
    """" Clase ciudades para guardar la ciudad y su longitud y latitud para calcular su clima """

def funcionHash(ciudad, n):
    suma = 0
    for caracter in ciudad.nombre:
        suma += ord(caracter)
    return (suma + abs(int(float(ciudad.latitud))) + abs(int(float(ciudad.longitud)))) % n
""" Funcion que obtiene el valor hash de una ciudad, dado su nombre, longitud ciudad """

def buscarCiudadOrigen(listaCiudades, ciudadOrigen, n):
    llaveHash = funcionHash(ciudadOrigen, n)
    for i in range(n):
        if(len(listaCiudades[(llaveHash + i) % n]) == 0):
            return -1#Si la casilla que le corresponderia esta vacia
        if(listaCiudades[(llaveHash + i) % n][0].nombre == ciudadOrigen.nombre):
            return i + llaveHash
    return -1
""" Funcion que busca en el arreglo de ciudades, una ciudad dado su nombre, si no la encuentra devuelve -1"""

def buscarCiudad(listaCiudades, nombreCiudad):
    for ciudadesDestino in listaCiudades:
        if(ciudadesDestino.nombre == nombreCiudad):
            return True
    return False
""" Funcion que busca si la ciudad destino ya esta considerada en en arreglo de los destinos de la ciudad"""

def escribirDestinos(n):    
    with open('../data/dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        #Lista de listas donde cada casilla contiene a una ciudad y sus destinos posibles
        listaCiudades = [list()]
        #Inicializamos todas las casillas con listas vacias
        for i in range(n):
            listaCiudades.append(list())
        #Vamos a guardar en el arreglo los n aereopuertos distintos con sus vuelos posibles.
        i = 0;
        for vuelo in reader:
            if(i > 0):#Evitamos leer las descripciones
                #Inicializamos la ciudad origen
                ciudadOrigen = Ciudades(vuelo[0], vuelo[2], vuelo[3])
                #Obtenemos el indice de la ciudad
                index = buscarCiudadOrigen(listaCiudades, ciudadOrigen, n)
                if(index == -1):#Si la ciudad no existe, la registramos
                    for j in range(n):#En la primera posicion disponible a partir de su HK
                        if(len(listaCiudades[(funcionHash(ciudadOrigen, n) + j) % n]) == 0):
                            listaCiudades[(funcionHash(ciudadOrigen, n) + j) % n].append(Ciudades(ciudadOrigen.nombre, float(ciudadOrigen.latitud), float(ciudadOrigen.longitud)))
                            index = (funcionHash(ciudadOrigen, n) + j) % n
                            break
                if(not buscarCiudad(listaCiudades[index], vuelo[1])):#Si el vuelo no ha sido registrado
                    listaCiudades[index].append(Ciudades(vuelo[1], float(vuelo[4]), float(vuelo[5])))
            i += 1
            
        for i in range(n):
            if(len(listaCiudades[i]) > 0):#Para cada ciudad que fue registrada
                #Abrimos el json de la ciudad correspondiente y escribimos la ciudad y todos sus destinos
                with open(listaCiudades[i][0].nombre + '.json', 'w') as archivo:
                    json.dump(listaCiudades[i], archivo, indent=4, cls=CiudadesEncoder)
"""Funcion que escribe en un 'Nombre'.json para cada ciudad de origen, escribe los destinos disponibles, recibe un n que es el tamño de la tabla hash """
def leerDestinos(ciudadOrigen):
    with open(ciudadOrigen + ".json") as archivo:
        destinos = json.load(archivo)
        for destino in destinos:
            if(destino[0] != ciudadOrigen):
                print(destino)
        return destinos
""" Leemos con la ciudad de origen todos sus destinos posibles"""
def cargarDatos():
    with open("historial.json") as archivo:
        historial = json.load(archivo)
        return historial
    
def convertirDatos(datos):
    informacion = "Clima: " + datos['weather'][0]['main'] + "\n"
    informacion += "Descripcion: " + datos['weather'][0]['description'] + "\n"
    #print(datos['wheather'][0]['icon'])
    informacion += "Temperatura: " + str(datos['main']['temp'] - 273) + "\n"
    informacion += "Sensacion: "+ str(datos['main']['feels_like'] - 273) + "\n"
    informacion += "Temp. minima: " + str(datos['main']['temp_min']) + "\n"
    informacion += "Temp. maxima: " + str(datos['main']['temp_max']) + "\n"
    informacion += "Ciudad: " + datos['sys']['country'] + "\n"
    informacion += "Nombre: " + datos['name'] + "\n"
    informacion += "Amanecer: " + str(datos['sys']['sunrise']) + "\n"
    informacion += "Atardecer: " + str(datos['sys']['sunset']) + "\n"
    return informacion
"""Funcion que devuelve la informacion dado el json del clima"""
    
def leerHistorial():
    historial = open("historial.txt", 'r')
    print(historial.read())
    historial.close()
"""Funcion que lee el historial"""
def buscarCiudadClima(cacheClima, ciudad, n):
    llaveHash = funcionHash(ciudad, n)
    for i in range(n):
        if(len(cacheClima[(llaveHash + i) % n]) == 0):
            return -1
        if(cacheClima[(llaveHash + i) % n][0] == ciudad.nombre):
            return i + llaveHash
    return -1
"""Funcion que busca con una ciudad clima donde esta ubicada en la cache"""
def realizarPeticion(ciudad, api):
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(ciudad.latitud) + "&lon=" + str(ciudad.longitud) + "&appid=" + api + "&lang=es"
    f = urllib.request.urlopen(url,timeout=30)
    return json.loads(f.read())
"""Funcion que realiza dada una ciudad y la api su clima en datos json"""
def obtenerClima(cacheClima, ciudad, n, api):
    index = buscarCiudadClima(cacheClima, ciudad, n)
    if(index != -1):#Si el clima ya se registro previamente
        if((datetime.now() - cacheClima[index][2]) < timedelta(minutes=30)):
            datosJson = cacheClima[index][1]#Usar la cache
        else:#Si ya paso tiempo desde la ultima consulta
            datosJson = realizarPeticion(ciudad, api)
            cacheClima[index][1] = datosJson
            cacheClima[index][2] = datetime.now()
    else:#Registramos el clima
        for i in range(n):
            index = (funcionHash(ciudad, n) + i) % n
            if(len(cacheClima[index]) == 0): 
                datosJson = realizarPeticion(ciudad, api)
                cacheClima[index] = [ciudad.nombre, datosJson, datetime.now()]
                break
    return cacheClima
"""Funcion que registra si tenemos que realizar la peticion """
def obtenerNumeroDeVuelo():
    f = open ('nVuelo.txt','r')
    contenido = f.read()
    numero = int(contenido)
    print(str(numero))
    f.close()
    f = open ('nVuelo.txt','w')
    f.write(str(numero + 1))
    f.close()
    return numero
"""Funcion que devuelve cuantos vuelos hemos reguistrado"""

def convertirVuelo(datosOrigen, datosDestino):
    informacion = "Vuelo " + str(obtenerNumeroDeVuelo()) + " a las: " + datetime.now().strftime("%H: %M: %S") + "\n"
    informacion += "Origen: " + datosOrigen['name'] + ", " + datosOrigen['sys']['country'] + ", Temperatura: " + str(datosOrigen['main']['temp']) + "\n"
    informacion += "Destino: " + datosDestino['name'] + ", " + datosDestino['sys']['country'] + ", Temperatura: " + str(datosDestino['main']['temp']) + "\n"
    return informacion
"""Funcion que devuelve datos los datos json un dato en string con la hora y numero de vuelo"""

def mostrarClima(datosOrigen, datosDestino):
    #En lugar del print, hay que mandarlos a los labels
    print(convertirDatos(datosOrigen))
    print(convertirDatos(datosDestino))
    #Registramos el vuelo en un txt
    historial = open("historial.txt", 'a')
    historial.write(convertirVuelo(datosOrigen, datosDestino))
    historial.close()
"""Funcion que muestra el clima y escribe el vuelo en un historial"""

def main():
    #Tamaño de la tabla de dispersion
    n = 71
    #Escribimos los .JSON de cada aereopuerto
    escribirDestinos(n)
    #API utilizada para las solicitudes
    api = "9d92b9e2262e46e5b34601d6f706cf43"

    #Creamos la cache de los climas
    cacheClima = [list()]
    for i in range(n):
        cacheClima.append(list())

    #Ciudad de Origen y lo guardamos en la cache
    stringCiudad = "MEX"#Esta es la seleccion de aereopuerto origen
    #funcion str->objCiudad mediante abriendo str.json
    
    #Obtenemos el destino y lo guardamos en la cache
    destinos = leerDestinos(stringCiudad)
    ciudadOrigen = Ciudades(destinos[0][0], destinos[0][1], destinos[0][2])
    print("Nuestra ciudad origne" + str(ciudadOrigen))
    cacheClima = obtenerClima(cacheClima, ciudadOrigen, n, api)
    
    ciudadDestinoCodigo = input()#Esta es la seleccion de aereopuerto destino
    longitudDestino = 0.0
    latitudDestino = 0.0
    for destino in destinos:
        if (destino[0] == ciudadDestinoCodigo):
            latitudDestino = destino[1]
            longitudDestino = destino[2]
            
    ciudadDestino = Ciudades(ciudadDestinoCodigo, latitudDestino, longitudDestino)
    cacheClima = obtenerClima(cacheClima, ciudadDestino, n, api)
    #Mostramos el clima de ambas ciudades, los labels van aqui
    mostrarClima(cacheClima[buscarCiudadClima(cacheClima, ciudadOrigen, n)][1], cacheClima[buscarCiudadClima(cacheClima, ciudadDestino, n)][1])
    #leerHistorial()
main()
