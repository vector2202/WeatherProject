from re import template
from tkinter import *
from tkinter import ttk
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
        self.master = master
        self.master.minsize(500,250)
        
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
    def consultarVuelo(self):
        print("Haciendo la request con la API dada")#con la api, hacemos la request con api, lat, long, escribimos en ambas etiquetas
    def mostrarHistorial(self):
        print("Mostrando todos los vuelos consultados")#abrir y leer el archivo
    def registrarAPI(self):
        print("Cambiando la API")#sobreescribir el archivo de la api
    def origenElegido(self, *args):
        print(f'Has elegido { self.optionVarOrigen.get()}')#redefinimos destino, establecer lat y long
    def destinoElegido(self, *args):
        print(f'Has elegido { self.optionVarDestino.get()}')#redefinos origen, establecer lat y long
        
root = tk.Tk()
app = App(root)
app.mainloop()
