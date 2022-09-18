from re import template
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

import urllib.request
import urllib.parse
import http.client
import json
import csv
import sys
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
def revisarCsv(archivo):
    with open('data/' + archivo, 'r') as file:
        contenido = csv.reader(file)
        i = 0
        for vuelo in contenido:
            if(len(vuelo) != 6):
                raise Exception("Formato de csv incorrecto")
            if(i > 0):
                if(type(vuelo[0]) != str or type(vuelo[1]) != str or type(vuelo[2]) != float or type(vuelo[3]) != float or type(vuelo[4]) != float or type(vuelo[5]) != float):
                    raise Exception("Formato de csv incorrecto")
                
"""Funcion que verifica que el formato del csv sea correcto"""
def escribirDestinos(archivo, n):    
    with open('data/' + archivo, 'r') as file:
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
                with open("data/" + listaCiudades[i][0].nombre + '.json', 'w') as archivo:
                    json.dump(listaCiudades[i], archivo, indent=4, cls=CiudadesEncoder)
        return listaCiudades
"""Funcion que escribe en un 'Nombre'.json para cada ciudad de origen, escribe los destinos disponibles, recibe un n que es el tamño de la tabla hash """
def leerDestinos(ciudadOrigen):
    try:
        destinos = []
        with open("data/" + ciudadOrigen + ".json") as archivo:
            datos = json.load(archivo)
            for dato in datos:
                if(dato[0] != ciudadOrigen):
                    destinos.append(dato)
            return destinos
    except OSError as error:
        return None
""" Leemos con la ciudad de origen todos sus destinos posibles"""
def cargarDatos():
    with open("data/historial.json") as archivo:
        historial = json.load(archivo)
        return historial
        
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
    try:
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(ciudad.latitud) + "&lon=" + str(ciudad.longitud) + "&appid=" + api + "&lang=es"
        f = urllib.request.urlopen(url,timeout=30)
        return json.loads(f.read())
    except urllib.request.HTTPError as error:
        print(error)
        return None
"""Funcion que realiza dada una ciudad y la api su clima en datos json"""
def obtenerClima(cacheClima, ciudad, n, api):
    index = buscarCiudadClima(cacheClima, ciudad, n)
    if(index != -1):#Si el clima ya se registro previamente
        if((datetime.now() - cacheClima[index][2]) >= timedelta(minutes=30)):
            #Si ya paso tiempo desde la ultima consulta
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
    try:
        f = open ('data/nVuelo.txt','r')
        contenido = f.read()
        numero = int(contenido)
        f.close()
    except OSError as error:
        numero = 0
    print("Vuelo " + str(numero))
    
    f = open ('data/nVuelo.txt','w')
    f.write(str(numero + 1))
    f.close()
    return numero
"""Funcion que devuelve cuantos vuelos hemos reguistrado"""

def convertirVuelo(datosOrigen, datosDestino):
    if(datosOrigen == None or datosDestino == None):
        return ""
    informacion = "Vuelo " + str(obtenerNumeroDeVuelo()) + " a las: " + datetime.now().strftime("%H: %M: %S") + "\n"
    informacion += "Origen: " + datosOrigen['name'] + ", " + datosOrigen['sys']['country'] + ", Temperatura: " + str(datosOrigen['main']['temp']) + "\n"
    informacion += "Destino: " + datosDestino['name'] + ", " + datosDestino['sys']['country'] + ", Temperatura: " + str(datosDestino['main']['temp']) + "\n"
    return informacion
"""Funcion que devuelve datos los datos json un dato en string con la hora y numero de vuelo"""

#Aqui comienza la interfaz.
class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid() # Esto es la cuadricula para poder poner los terxtos y opciones.
        self.inicializarJsons()
        self.createWidgets()
        self.master = master
        self.master.minsize(400,250)
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"

        
    def createWidgets(self):
        self.historial = ttk.Button(self, text="Historial", command=self.mostrarHistorial)#boton de historial para mostrar lo consultado
        #self.historial.pack(side=LEFT, padx=20, pady=20)
        self.historial.place(x=20,y=20)

        #Seccion de la API
        self.apiText = ttk.Label(text="Escriba la llave:")
        self.apiText.place(x=200,y=20)
        self.apiLlave = ttk.Entry()#caja de texto para escribir la llave de la API
        self.apiLlave.place(x=320, y=20, width=60)
        self.apiBoton = ttk.Button(self, text="API", command=self.registrarAPI)
        self.apiBoton.place(x=390, y=20)
        #self.apiBoton.pack(side=RIGHT, padx=290, pady=20)
        
        #Boton para moestrar los climas
        self.consultar = ttk.Button(self, text="Consultar", command=self.destinoElegido)
        self.consultar.place(x=390,y=130)
        #self.consultar.pack(side=RIGHT,padx=390,pady=50)

        #Label para cd Origen y Destino
        self.ciudadOrigenLabel = Label(self, text="Ciudad de origen")
        self.ciudadOrigenLabel.place(x=20,y=100)
        self.ciudadDestinoLabel = Label(self, text="Ciudad de destino:")
        self.ciudadDestinoLabel.place(x=200, y=100) 

        #Arreglos de informacion de origenes y destinos
        self.optionVarOrigen = tk.StringVar(self)
        self.origen = tk.OptionMenu(self, self.optionVarOrigen, self.listaOrigenes[0], *self.listaOrigenes, command=self.origenElegido)
        self.origen.place(x=20, y=130)
        self.optionVarOrigen.set("Selecciona el origen:")

        self.optionVarDestino = tk.StringVar(self)
        self.optionVarDestino.set('')
        self.destino = tk.OptionMenu(self, self.optionVarDestino, None,  *self.listaDestinos, command=self.destinoElegido)
        self.destino.place(x=200, y=130)
        self.optionVarDestino.set("Selecciona el destino:")

        
        #Informacion que se va a mostrar
        self.climaOrigenDatos = StringVar()
        self.climaDestinoDatos = StringVar()
        self.climaOrigenDatos.set("")
        self.climaDestinoDatos.set("")
        self.climaOrigen = ttk.Label(self, textvariable=self.climaOrigenDatos)
        self.climaOrigen.place(x=20, y=170)
        self.climaDestino = ttk.Label(self, textvariable=self.climaDestinoDatos)
        self.climaDestino.place(x=200, y=170)

        #self.labelMostrarClima = ttk.Label(self, text= mostrarClima)
        #self.labelMostrarClima.place(x=20, y=190)
        
        #Boton para salir del programa
        self.buttonQuit = ttk.Button(self, text="Salir del programa", command = root.quit)
        self.buttonQuit.pack(padx=200, pady=300)
        #self.buttonQuit.place(x=200, y=300)

    def inicializarJsons(self):
        #Tamaño de la tabla de dispersion
        self.n = 71
        #Escribimos los .JSON de cada aereopuerto
        archivo = "dataset1.csv"
        #Revisamos si el archivo CSV es correcto
        try:
            revisarCsv(archivo)
        except Exception as exception:
            sys.exit(str(exception))
        #Escribimos los JSON de cada cd Origen
        listaCiudades = escribirDestinos(archivo, self.n)
        
        #Inicializamos la lista de ciudades origen
        self.listaOrigenes = []
        self.listaDestinos = []
        for x in listaCiudades:
            if(len(x) > 0):
                self.listaOrigenes.append(x[0].nombre)
            
        #Creamos la cache de los climas
        self.cacheClima = [list()]
        for i in range(self.n):
            self.cacheClima.append(list())

    def mostrarClima(self, datosOrigen, datosDestino):
        #En lugar del print, hay que mandarlos a los labels
        self.climaOrigenDatos.set(self.convertirDatos(datosOrigen))
        self.climaDestinoDatos.set(self.convertirDatos(datosDestino))
        #Registramos el vuelo en un txt
        historial = open("data/historial.txt", 'a')
        historial.write(convertirVuelo(datosOrigen, datosDestino))
        historial.close()
        """Funcion que muestra el clima y escribe el vuelo en un historial"""
    def convertirDatos(self, datos):
        if(datos == None):
            return ""
        informacion = datos['name'] + "," + datos['sys']['country'] + "\n"
        informacion += datos['weather'][0]['description'] + "\n"
        
        informacion += "Temperatura: " + str(datos['main']['temp'] - 273) + "\n"
        informacion += "Sensacion: "+ str(datos['main']['feels_like'] - 273) + "\n"
        informacion += "Temp. minima: " + str(datos['main']['temp_min']) + "\n"
        informacion += "Temp. maxima: " + str(datos['main']['temp_max']) + "\n"
        informacion += "Amanecer: " + str(datos['sys']['sunrise']) + "\n"
        informacion += "Atardecer: " + str(datos['sys']['sunset']) + "\n"
        self.iconURL = "http://openweathermap.org/img/w/" + str(datos['weather'][0]['icon']) + ".png"
        return informacion
    """Funcion que devuelve la informacion dado el json del clima"""

    def consultarVuelo(self):
        self.mostrarClima(self.cacheClima[buscarCiudadClima(self.cacheClima, self.ciudadOrigen, self.n)][1], self.cacheClima[buscarCiudadClima(self.cacheClima, self.ciudadDestino, self.n)][1])
        
    
    def mostrarHistorial(self):
        historial = open("data/historial.txt", 'r')
        print(historial.read())
        tk.messagebox.showinfo("Historial",text=historial.read())
        historial.close()

    #def onClick(self):
        #tk.messagebox.showinfo("Historial",text=historial.read())

    def registrarAPI(self):
        self.api = self.apiLlave.get()
        print(str(self.api))#sobreescribir el archivo de la api y la variable api

    def origenElegido(self, *args):
        stringCiudad = self.optionVarOrigen.get()
        print("Has elegido" + stringCiudad)
        self.destinosDisponibles = leerDestinos(stringCiudad)
        self.listaDestinos = []
        if(self.destinosDisponibles != None):
            self.ciudadOrigen = Ciudades(self.destinosDisponibles[0][0], self.destinosDisponibles[0][1], self.destinosDisponibles[0][2])
            self.cacheClima = obtenerClima(self.cacheClima, self.ciudadOrigen, self.n, self.api)
            for destino in self.destinosDisponibles:
                self.listaDestinos.append(destino[0])
            self.optionVarDestino.set('')
            self.destino['menu'].delete(0, 'end')
            # Insert list of new options (tk._setit hooks them up to var)
            for ciudad in self.listaDestinos:
                self.destino['menu'].add_command(label=ciudad, command=tk._setit(self.optionVarDestino, ciudad))
        else:
            print("Ciudad de origen no existente")
            
    def destinoElegido(self, *args):
        stringDestino = self.optionVarDestino.get()
        print("Has elegido " + stringDestino)
        longitudDestino = 0.0
        latitudDestino = 0.0
        destinoEncontrado = False
        if(self.destinosDisponibles != None):
            for destino in self.destinosDisponibles:
                if (destino[0] == stringDestino):
                    latitudDestino = destino[1]
                    longitudDestino = destino[2]
                    destinoEncontrado = True
            if(destinoEncontrado):
                self.ciudadDestino = Ciudades(stringDestino, latitudDestino, longitudDestino)
                self.cacheClima = obtenerClima(self.cacheClima, self.ciudadDestino, self.n, self.api)
                self.consultarVuelo()
            else:
                print("La ciudad de destino es invalida")

root = tk.Tk()
root.title("Bienvenidos a CheckWeather por- Victor Torres y Diego Castro")
#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='../img/icon.png'))
#root.configure(background='green')
app = App(root)
app.mainloop()
