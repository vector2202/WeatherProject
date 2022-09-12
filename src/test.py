from re import template
from tkinter import *
from tkinter import ttk
import tkinter as tk

import urllib.request
import urllib.parse
import http.client
import json
import csv

class App(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.inicializarJsons()
        self.master = master
        self.master.minsize(500,250)
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
        
    def createWidgets(self):
        self.consultar = tk.Button(self, text="Consultar", command=self.consultarVuelo)
        self.consultar.pack()
        self.historial = tk.Button(self, text="Historial", command=self.mostrarHistorial)
        self.historial.pack()
        self.apiText = tk.Text(self)
        self.apiText.pack()
        self.apiBoton = tk.Button(self, text="API", command=self.registrarAPI)
        self.apiBoton.pack()
        
        self.ciudadOrigen = Label(self, text="Ciudad de origen")
        self.ciudadOrigen.pack()
        self.ciudadDestino = Label(self, text="Ciudad de destino")
        self.ciudadDestino.pack()

        self.climaOrigen = Label(self, text="Clima de origen")
        self.climaOrigen.pack()
        self.climaDestino = Label(self, text="Clima de destino")
        self.climaDestino.pack()

        self.origenes =('ACA', 'MEX', 'MTY')#Todos
        self.optionVarOrigen = tk.StringVar(self)
        self.origen = tk.OptionMenu(self, self.optionVarOrigen, self.origenes[0], *self.origenes, command=self.origenElegido)
        self.origen.pack()

        self.destinos =('CNC', 'SIN', 'SON')#Todos
        self.optionVarDestino = tk.StringVar(self)
        self.origen = tk.OptionMenu(self, self.optionVarDestino, self.destinos[0], *self.destinos, command=self.destinoElegido)
        self.origen.pack()

    def inicializarJsons(self):
        print("Inicializamos los Json de cada Aereopuerto")
        
    def consultarVuelo(self):
        #Se muestra tanto el clima de origen como el clima de destino con iconos.
        #Se guarda en un archivo los datos de los vuelos.
        print(self.djsonClimaOrigen)
        print(self.djsonClimaOrigen["weather"][0]["description"])
        print(self.djsonClimaDestino)
        print(self.djsonClimaDestino["weather"][0]["description"])
        print("Haciendo la request con la API dada", self.api)

        
    def mostrarHistorial(self):
        historial = open("../data/listaDeVuelos.txt")
        print(historial.read())
        print("Mostrando todos los vuelos consultados")#abrir y leer el archivo
        
    def registrarAPI(self):
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
        print("Cambiando la API")#sobreescribir el archivo de la api y la variable api
        
    def origenElegido(self, *args):
        print(f'Has elegido { self.optionVarOrigen.get()}')#redefinimos destino, establecer lat y long
        #Destino se tiene que redefinir con los posibles destinos del origen elegido
        #Se calcula el clima de la ciudad de Origen y se guarda
        longitud = str(-99.566)
        latitud = str(19.3371)
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitud+ "&lon=" + longitud + "&appid=" + self.api
        datoClimaOrigen = urllib.request.urlopen(url,timeout=30)
        self.djsonClimaOrigen = json.loads(datoClimaOrigen.read())
        
        
    def destinoElegido(self, *args):
        print(f'Has elegido { self.optionVarDestino.get()}')#redefinos origen, establecer lat y long
        #Origen se tiene que redefinir con los posibles origen del destino elegido
        #Se calcula el clima de la ciudad de Destino y se guarda
        longitud = str(-99.566)
        latitud = str(19.3371)
        url = "https://api.openweathermap.org/data/2.5/weather?lat=" + latitud+ "&lon=" + longitud + "&appid=" + self.api
        datoClimaDestino = urllib.request.urlopen(url,timeout=30)
        self.djsonClimaDestino = json.loads(datoClimaDestino.read())

        
        
root = tk.Tk()
app = App(root)
app.mainloop()
# En cada Aereopuerto.json tendremos 2 arreglos, 1 con los posibles destinos y otro con las posibles llegadas
#Archivo json de la API
#Archivo txt con todos los vuelos registrados
