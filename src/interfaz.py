from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import sys
from src.aeropuerto import Aeropuerto
from src.procesarArchivos import escribirDestinos, leerDestinos, revisarCSV
from src.historialVuelos import convertirAVuelo
from src.cacheClima import CacheClima


class Interfaz(tk.Frame):
    '''
    Clase para crear y organizar la interfaz
    '''
    def __init__(self, master):
        '''
        Construye los atributos necesarios para nuestra interfaz
        '''
        tk.Frame.__init__(self, master)
        self.grid() 
        self.inicializarJSONs()
        self.crearBotones()
        self.crearEtiquetas()
        self.crearEntrada()
        self.crearMenus()
        self.master = master
        self.master.minsize(400,250)
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
 

    def crearBotones(self):
        '''
        Funcion que nos permite crear botones que estan asociados a ciertas funciones
        '''
        ttk.Button(self, text="Historial", command=self.mostrarHistorial).place(x=20,y=20)
        ttk.Button(self, text="API", command=self.registrarAPI).place(x=390, y=20)
        ttk.Button(self, text="Salir del programa",\
                   command=self.salida).pack(padx=200, pady=350)
        ttk.Button(self, text="Consultar", command=self.seleccionAeropuertoDestino).place(x=390, y=130)


    def crearMenus(self):
        '''
        Funcion que nos muestra los menus tanto para el lugar de origen como de destino
        '''
        self.aeropuertoOrigenSeleccionado = tk.StringVar(self)
        self.aeropuertoOrigenSeleccionado.set("Selecciona el origen:")
        self.menuAeropuertoOrigen = tk.OptionMenu(self, self.aeropuertoOrigenSeleccionado,\
                                                   self.listaAeropuertosOrigen[0],\
                                                   *self.listaAeropuertosOrigen,\
                                                   command=self.seleccionAeropuertoOrigen)
        self.menuAeropuertoOrigen.place(x=20, y=130)
        self.aeropuertoDestinoSeleccionado = tk.StringVar(self)
        self.aeropuertoDestinoSeleccionado.set("Selecciona el destino:")
        self.menuAeropuertoDestino = tk.OptionMenu(self, self.aeropuertoDestinoSeleccionado, None,\
                                                  *self.listaAeropuertosDestino,\
                                                  command=self.seleccionAeropuertoDestino)
        self.menuAeropuertoDestino.place(x=200, y=130)

    def crearEtiquetas(self):
        '''
        Funcion que crea las etiquetas para mostrar ciertos mensajes en nuestra interfaz (es meramente visual)
        '''
        ttk.Label(text="Escriba la llave:").place(x=200,y=20)
        Label(self, text="Ciudad de origen").place(x=20,y=100)
        Label(self, text="Ciudad de destino:").place(x=200, y=100) 
        self.datosClimaAeropuertoOrigen = StringVar()
        self.datosClimaAeropuertoDestino = StringVar()
        self.datosClimaAeropuertoOrigen.set("")
        self.datosClimaAeropuertoDestino.set("")
        self.climaAeropuertoOrigen = ttk.Label(self, textvariable=self.datosClimaAeropuertoOrigen).place(x=20, y=170)
        self.climaAeropuertoDestino = ttk.Label(self, textvariable=self.datosClimaAeropuertoDestino).place(x=200, y=170)
        
    def crearEntrada(self):
        '''
        Funcion para que se pueda escribir la llave de la API
        '''
        self.llaveAPI = ttk.Entry()
        self.llaveAPI.place(x=320, y=20, width=60)

    
    def salida(self):
        tk.Frame.destroy

    def inicializarJSONs(self):
        '''
        Funcion que inicializa nuestras listas y hacemos uso de nuestro dataset
        '''
        nombreArchivoCSV = "dataset1.csv"
        tamañoDiccionario = 71
        self.listaAeropuertosOrigen = []
        self.listaAeropuertosDestino = []
        try:
            revisarCSV(nombreArchivoCSV)
        except Exception as exception:
            sys.exit(str(exception))
        listaAeropuertos = escribirDestinos(nombreArchivoCSV, tamañoDiccionario)
        self.listaAeropuertosOrigen = listaAeropuertos.obtenerNombres()
        self.cache = CacheClima(tamañoDiccionario)


    def seleccionAeropuertoOrigen(self, *args):
        '''
        Funcion para cuando hacemos la seleccion de nuestro aeropuerto de origen y poder revisas los posibles destinos y el clima
        '''
        nombreAeropuertoOrigen = self.aeropuertoOrigenSeleccionado.get()
        self.destinosDisponibles = leerDestinos(nombreAeropuertoOrigen)
        if(self.destinosDisponibles != None):
            self.aeropuertoOrigen = Aeropuerto\
                (self.destinosDisponibles[0][0],\
                 self.destinosDisponibles[0][1], self.destinosDisponibles[0][2])
            self.request = self.cache.refrescarClima(self.aeropuertoOrigen)
            self.destinosDisponibles.pop(0)
            self.listaAeropuertosDestino = self.obtenerNombreDestinos(self.destinosDisponibles)
            self.aeropuertoDestinoSeleccionado.set('')
            self.menuAeropuertoDestino['menu'].delete(0, 'end')    
            for aeropuertoDestino in self.listaAeropuertosDestino:
                self.menuAeropuertoDestino['menu'].add_command\
                    (label=aeropuertoDestino, command=tk._setit\
                     (self.aeropuertoDestinoSeleccionado, aeropuertoDestino))
            return True
        return False


    def obtenerNombreDestinos(self, destinos):
        '''
        Funcion que nos regresa una lista con los nombres de lugares destinos
        '''
        lista = []
        for destino in destinos:
                lista.append(destino[0])
        return lista
            

    def seleccionAeropuertoDestino(self, *args):
        '''
        Funcion para seleccionar nuestro aeropuerto destino
        '''
        nombreAeropuertoDestino = self.aeropuertoDestinoSeleccionado.get()
        if(self.destinosDisponibles != None):
            for destino in self.destinosDisponibles:
                if (destino[0] == nombreAeropuertoDestino):
                    self.aeropuertoDestino = \
                        Aeropuerto(nombreAeropuertoDestino, destino[1],\
                                   destino[2])
                    self.request = self.request and\
                        self.cache.refrescarClima(self.aeropuertoDestino)
                    self.consultarVuelo()
                    return True
        return False


    def consultarVuelo(self):
        '''
        Fucion para hacer las consultas de los vuelos
        '''
        if(self.request):
            self.mostrarClima(self.cache.obtenerClima(self.aeropuertoOrigen),\
                              self.cache.obtenerClima(self.aeropuertoDestino))
        else:
            print("No hay datos")


    def mostrarClima(self, datosOrigen, datosDestino):
        '''
        Funcion para poder mostrar el clima de los datos de origen y destino
        '''
        self.datosClimaAeropuertoOrigen.set(datosOrigen)
        self.datosClimaAeropuertoDestino.set(datosDestino)
        with open("datos/historial.txt",'a') as archivoHistorial:
            archivoHistorial.write(convertirAVuelo(datosOrigen, datosDestino))
        
    
    def mostrarHistorial(self):
        '''
        Funcion para mostrar el historial de lo consultado
        '''
        n = 3*3 
        with open("datos/historial.txt", 'r') as archivo:
            informacion = ""
            for linea in (archivo.readlines()[-n:]):
                informacion += linea + "\n"
        tkinter.messagebox.showinfo("Historial", message=informacion)


    def registrarAPI(self):
        '''
        Funcion par registrar nuestra llave
        '''
        self.api = self.llaveAPI.get()
        self.cache.actualizarAPI(self.api)
        print(str(self.api)) 
