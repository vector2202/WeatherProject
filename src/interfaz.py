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
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid() 
<<<<<<< HEAD
        self.inicializarJSONs()
        self.crearBotones()
        self.crearEtiquetas()
        self.crearEntrada()
        self.crearMenus()
=======
        self.inicializarJsons()
>>>>>>> main
        self.master = master
        self.master.minsize(400,250)
        self.createButtons()
        self.createLabels()
        self.createEntries()
        self.createMenus()
        self.api = "9d92b9e2262e46e5b34601d6f706cf43"
 

<<<<<<< HEAD
    def crearBotones(self):
=======
    def createButtons(self):
>>>>>>> main
        ttk.Button(self, text="Historial", command=self.mostrarHistorial).place(x=20,y=20)
        ttk.Button(self, text="API", command=self.registrarAPI).place(x=390, y=20)
        ttk.Button(self, text="Salir del programa",\
                  command=self.saluda).pack(padx=200, pady=350)
<<<<<<< HEAD
        ttk.Button(self, text="Consultar", command=self.seleccionAeropuertoDestino).place(x=390, y=130)


    def crearMenus(self):
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
        self.llaveAPI = ttk.Entry()
        self.llaveAPI.place(x=320, y=20, width=60)

    def saluda(self):
        print("Hola")
    
    def inicializarJSONs(self):
=======


    def createMenus(self):
        self.optionVarOrigen = tk.StringVar(self)
        self.optionVarOrigen.set("Selecciona el origen:")
        tk.OptionMenu(self, self.optionVarOrigen,\
                self.listaOrigenes[0], *self.listaOrigenes,\
                command=self.origenElegido).place(x=20, y=130)
        self.optionVarDestino = tk.StringVar(self)
        self.optionVarDestino.set("Selecciona el destino:")
        tk.OptionMenu(self, self.optionVarDestino, None,\
                *self.listaDestinos,command=self.destinoElegido).place(x=200, y=130)


    def createLabels(self):
        ttk.Label(text="Escriba la llave:").place(x=200,y=20)
        Label(self, text="Ciudad de origen").place(x=20,y=100)
        Label(self, text="Ciudad de destino:").place(x=200, y=100) 
        self.climaOrigenDatos = StringVar()
        self.climaDestinoDatos = StringVar()
        self.climaOrigenDatos.set("")
        self.climaDestinoDatos.set("")
        ttk.Label(self, textvariable=self.climaOrigenDatos).place(x=20, y=170)
        ttk.Label(self, textvariable=self.climaDestinoDatos).place(x=200, y=170)
        

    def createEntries(self):
        ttk.Entry().place(x=320, y=20, width=60)


    def saluda(self):
        print("Hola")
    

    def inicializarJsons(self):
>>>>>>> main
        nombreArchivoCSV = "dataset1.csv"
        tamañoDiccionario = 71
        self.listaAeropuertosOrigen = []
        self.listaAeropuertosDestino = []
        try:
<<<<<<< HEAD
            revisarCSV(nombreArchivoCSV)
        except Exception as exception:
            sys.exit(str(exception))
        listaAeropuertos = escribirDestinos(nombreArchivoCSV, tamañoDiccionario)
        self.listaAeropuertosOrigen = listaAeropuertos.obtenerNombres()
        self.cache = CacheClima(tamañoDiccionario)


    def seleccionAeropuertoOrigen(self, *args):
        nombreAeropuertoOrigen = self.aeropuertoOrigenSeleccionado.get()
=======
            revisarCsv(nombreArchivoCSV)
        except Exception as exception:
            sys.exit(str(exception))
        listaAeropuertos = escribirDestinos(nombreArchivoCSV, tamañoDiccionario)
        self.listaOrigenes = listaAeropuertos.obtenerNombres()
        self.cache = CacheClima(tamañoDiccionario)


    def origenElegido(self, *args):
        nombreAeropuertoOrigen = self.optionVarOrigen.get()
>>>>>>> main
        self.destinosDisponibles = leerDestinos(nombreAeropuertoOrigen)
        if(self.destinosDisponibles != None):
            self.aeropuertoOrigen = Aeropuerto\
                (self.destinosDisponibles[0][0],\
                 self.destinosDisponibles[0][1], self.destinosDisponibles[0][2])
            self.request = self.cache.refrescarClima(self.aeropuertoOrigen)
            self.destinosDisponibles.pop(0)
<<<<<<< HEAD
            self.listaAeropuertosDestino = self.obtenerNombreDestinos(self.destinosDisponibles)
            self.aeropuertoDestinoSeleccionado.set('')
            self.menuAeropuertoDestino['menu'].delete(0, 'end')    
            for aeropuertoDestino in self.listaAeropuertosDestino:
                self.menuAeropuertoDestino['menu'].add_command\
=======
            self.listaDestinos = self.obtenerNombreDestinos(self.destinosDisponibles)
            self.optionVarDestino.set('')
            self.destino['menu'].delete(0, 'end')    
            for aeropuertoDestino in self.listaDestinos:
                self.destino['menu'].add_command\
>>>>>>> main
                    (label=aeropuertoDestino, command=tk._setit\
                     (self.aeropuertoDestinoSeleccionado, aeropuertoDestino))
            return True
        return False


    def obtenerNombreDestinos(self, destinos):
        lista = []
        for destino in destinos:
                lista.append(destino[0])
        return lista
            

<<<<<<< HEAD
    def seleccionAeropuertoDestino(self, *args):
        nombreAeropuertoDestino = self.aeropuertoDestinoSeleccionado.get()
=======
    def destinoElegido(self, *args):
        nombreAeropuertoDestino = self.optionVarDestino.get()
>>>>>>> main
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
        if(self.request):
            self.mostrarClima(self.cache.obtenerClima(self.aeropuertoOrigen),\
                              self.cache.obtenerClima(self.aeropuertoDestino))
        else:
            print("No hay datos")


    def mostrarClima(self, datosOrigen, datosDestino):
        '''
        Esto deberia ser una docstring para documetnar la funcion o metodo.
        '''
<<<<<<< HEAD
        self.datosClimaAeropuertoOrigen.set(datosOrigen)
        self.datosClimaAeropuertoDestino.set(datosDestino)
        with open("datos/historial.txt",'a') as archivoHistorial:
            archivoHistorial.write(convertirAVuelo(datosOrigen, datosDestino))
=======
        self.climaOrigenDatos.set(datosOrigen)
        self.climaDestinoDatos.set(datosDestino)
        with open("datos/historial.txt",'a') as archivoHistorial:
            archivoHistorial.write(convertirVuelo(datosOrigen, datosDestino))
>>>>>>> main
        
    
    def mostrarHistorial(self):
        n = 3*3 
        with open("datos/historial.txt", 'r') as archivo:
            informacion = ""
            for linea in (archivo.readlines()[-n:]):
                informacion += linea + "\n"
        tkinter.messagebox.showinfo("Historial", message=informacion)


    def registrarAPI(self):
        self.api = self.llaveAPI.get()
        self.cache.actualizarAPI(self.api)
        print(str(self.api)) 
