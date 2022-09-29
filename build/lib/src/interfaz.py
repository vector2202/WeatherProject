from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sys
from aeropuerto import Aeropuerto

from archivosCSV import escribirDestinos, leerDestinos, revisarCsv
from historial import convertirVuelo
from cacheClima import CacheClima
from listaDeAeropuertos import ListaDeAeropuertos

class Interfaz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid() # Esto es la cuadricula para poder poner los textos y opciones.
        self.inicializarJsons()
        self.createWidgets()
        self.master = master
        self.master.minsize(400,250)
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
        #self.owm = OpenWeatherMap()
        #self.temp_icon = OWIconLabel(self, weather_icon = owm.get_icon_data)
        #self.temp_icon.grid(row=0, column=0)
    
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

        #iconURL = "http://openweathermap.org/img/w/" + str(datos['weather'][0]['icon']) + ".png"
        #self.labelMostrarClima = ttk.Label(self, text= mostrarClima)
        #self.labelMostrarClima.place(x=20, y=190)

        #imageUrl = "http://openweathermap.org/img/w/.png"
        #u = urlopen(imageUrl)
        #rawData = u.read()
        #u.close()
        #photo = ImageTk.PhotoImage(data=rawData)
        #label = tk.Label(image=photo)
        #label.image = photo
        #label.pack()
        #Boton para salir del programa
        self.buttonQuit = ttk.Button(self, text="Salir del programa", command=self.saluda)
        self.buttonQuit.pack(padx=200, pady=350)
        
    def saluda(self):
        print("Hola")
    
    def inicializarJsons(self):
        nombreArchivoCSV = "dataset1.csv"
        #Tamaño de la tabla de dispersion
        tamañoDiccionario = 71
        self.listaOrigenes = []
        self.listaDestinos = []
        
        try:
            #Revisamos si el archivo CSV es correcto
            revisarCsv(nombreArchivoCSV)
        except Exception as exception:
            sys.exit(str(exception))
        #Escribimos los JSON de cada cd Origen
        listaAeropuertos = escribirDestinos(nombreArchivoCSV, tamañoDiccionario)
        #Inicializamos la lista de ciudades origen
        self.listaOrigenes = listaAeropuertos.obtenerNombres()
        #Creamos la cache de los climas
        self.cache = CacheClima(tamañoDiccionario)

    def origenElegido(self, *args):
        nombreAeropuertoOrigen = self.optionVarOrigen.get()
        self.destinosDisponibles = leerDestinos(nombreAeropuertoOrigen)#try excepto en lugar de un if none
        self.listaDestinos = []
        if(self.destinosDisponibles != None):
            self.aeropuertoOrigen = Aeropuerto(self.destinosDisponibles[0][0], self.destinosDisponibles[0][1], self.destinosDisponibles[0][2])
            self.cache.refrescar(self.aeropuertoOrigen)
            self.destinosDisponibles.pop(0)
            
            for destino in self.destinosDisponibles:
                self.listaDestinos.append(destino[0])
            self.destino['menu'].delete(0, 'end')
            for aeropuertoDestino in self.listaDestinos:
                self.destino['menu'].add_command(label=aeropuertoDestino, command=tk._setit(self.optionVarDestino, aeropuertoDestino))
                
        else:
            print("Ciudad de origen no existente")
            
    def destinoElegido(self, *args):
        nombreAeropuertoDestino = self.optionVarDestino.get()
        if(self.destinosDisponibles != None):
            for destino in self.destinosDisponibles:
                if (destino[0] == nombreAeropuertoDestino):
                    self.aeropuertoDestino = Aeropuerto(nombreAeropuertoDestino, destino[1], destino[2])
                    self.cache.refrescar(self.aeropuertoDestino)
                    self.consultarVuelo()
                    return
        print("La ciudad de destino es invalida")

    def consultarVuelo(self):
        #definir los Json
        self.mostrarClima(self.cache.obtenerClima(self.aeropuertoOrigen), self.cache.obtenerClima(self.aeropuertoDestino))
        
    def mostrarClima(self, datosOrigen, datosDestino):
        self.climaOrigenDatos.set(datosOrigen)
        self.climaDestinoDatos.set(datosDestino)
        #Registramos el vuelo en un txt
        archivoHistorial = open("datos/historial.txt", 'a')
        archivoHistorial.write(convertirVuelo(datosOrigen, datosDestino))
        archivoHistorial.close()
        """Funcion que muestra el clima y escribe el vuelo en un historial"""
        
    
    def mostrarHistorial(self):
        n = 3*3 
        with open("datos/historial.txt", 'r') as file:
            information = ""
            for line in (file.readlines()[-n:]):
                information += line + "\n"
        tkinter.messagebox.showinfo("Historial", message=information)

    def registrarAPI(self):
        self.api = self.apiLlave.get()
        self.cache.actualizarAPI(self.api)
        print(str(self.api))#sobreescribir el archivo de la api y la variable api
