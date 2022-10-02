from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sys
from src.aeropuerto import Aeropuerto
from src.archivosCSV import escribirDestinos, leerDestinos, revisarCsv
from src.historial import convertirVuelo
from src.cacheClima import CacheClima


class Interfaz(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid() 
        self.inicializarJsons()
        self.createWidgets()
        self.master = master
        self.master.minsize(400,250)
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
    

    def createWidgets(self):
        ttk.Button(self, text="Historial", command=self.mostrarHistorial).place(x=20,y=20)
        ttk.Label(text="Escriba la llave:").place(x=200,y=20)
        ttk.Entry().place(x=320, y=20, width=60)
        ttk.Button(self, text="API", command=self.registrarAPI).place(x=390, y=20)
        
        Label(self, text="Ciudad de origen").place(x=20,y=100)
        Label(self, text="Ciudad de destino:").place(x=200, y=100) 

        self.optionVarOrigen = tk.StringVar(self)
        self.origen = tk.OptionMenu(self, self.optionVarOrigen,\
                                    self.listaOrigenes[0], *self.listaOrigenes,\
                                    command=self.origenElegido)
        self.origen.place(x=20, y=130)
        self.optionVarOrigen.set("Selecciona el origen:")

        self.optionVarDestino = tk.StringVar(self)
        self.optionVarDestino.set('')
        self.destino = tk.OptionMenu(self, self.optionVarDestino, None,\
                                     *self.listaDestinos,command=self.destinoElegido)
        self.destino.place(x=200, y=130)
        self.optionVarDestino.set("Selecciona el destino:")
    
        self.climaOrigenDatos = StringVar()
        self.climaDestinoDatos = StringVar()
        self.climaOrigenDatos.set("")
        self.climaDestinoDatos.set("")
        ttk.Label(self, textvariable=self.climaOrigenDatos).place(x=20, y=170)
        ttk.Label(self, textvariable=self.climaDestinoDatos).place(x=200, y=170)

        ttk.Button(self, text="Salir del programa",\
                  command=self.saluda).pack(padx=200, pady=350)
       

    def saluda(self):
        print("Hola")
    

    def inicializarJsons(self):
        nombreArchivoCSV = "dataset1.csv"
        tamañoDiccionario = 71
        self.listaOrigenes = []
        self.listaDestinos = []
        try:
            revisarCsv(nombreArchivoCSV)
        except Exception as exception:
            sys.exit(str(exception))
        listaAeropuertos = escribirDestinos(nombreArchivoCSV, tamañoDiccionario)
        self.listaOrigenes = listaAeropuertos.obtenerNombres()
        self.cache = CacheClima(tamañoDiccionario)


    def origenElegido(self, *args):
        nombreAeropuertoOrigen = self.optionVarOrigen.get()
        self.destinosDisponibles = leerDestinos(nombreAeropuertoOrigen)
        if(self.destinosDisponibles != None):
            self.aeropuertoOrigen = Aeropuerto\
                (self.destinosDisponibles[0][0],\
                 self.destinosDisponibles[0][1], self.destinosDisponibles[0][2])
            self.request = self.cache.refrescar(self.aeropuertoOrigen)
            self.destinosDisponibles.pop(0)
            self.listaDestinos = self.obtenerNombreDestinos(self.destinosDisponibles)
            self.optionVarDestino.set('')
            self.destino['menu'].delete(0, 'end')    
            for aeropuertoDestino in self.listaDestinos:
                self.destino['menu'].add_command\
                    (label=aeropuertoDestino, command=tk._setit\
                     (self.optionVarDestino, aeropuertoDestino))
            return True
        return False


    def obtenerNombreDestinos(self, destinos):
        lista = []
        for destino in destinos:
                lista.append(destino[0])
        return lista
            

    def destinoElegido(self, *args):
        nombreAeropuertoDestino = self.optionVarDestino.get()
        if(self.destinosDisponibles != None):
            for destino in self.destinosDisponibles:
                if (destino[0] == nombreAeropuertoDestino):
                    self.aeropuertoDestino = \
                        Aeropuerto(nombreAeropuertoDestino, destino[1],\
                                   destino[2])
                    self.request = self.request and\
                        self.cache.refrescar(self.aeropuertoDestino)
                    self.consultarVuelo()
                    return True
        return False


    def consultarVuelo(self):
        if(self.request):
            self.mostrarClima(self.cache.obtenerClima(self.aeropuertoOrigen),\
                              self.cache.obtenerClima(self.aeropuertoDestino))
        else:
            print("No hay datos")


    def mostrarClima(self, datosOrigen, datosDestino):
        '''
        Esto deberia ser una docstring para documetnar la funcion o metodo.
        '''
        self.climaOrigenDatos.set(datosOrigen)
        self.climaDestinoDatos.set(datosDestino)
        with open("datos/historial.txt",'a') as archivoHistorial:
            archivoHistorial.write(convertirVuelo(datosOrigen, datosDestino))
        
    
    def mostrarHistorial(self):
        n = 3*3 
        with open("datos/historial.txt", 'r') as archivo:
            informacion = ""
            for linea in (archivo.readlines()[-n:]):
                informacion += linea + "\n"
        tkinter.messagebox.showinfo("Historial", message=informacion)


    def registrarAPI(self):
        self.api = self.apiLlave.get()
        self.cache.actualizarAPI(self.api)
        print(str(self.api)) 
