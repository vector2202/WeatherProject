from datetime import datetime

def obtenerNumeroDeVuelo():
    '''
    Funcion que devuelve cuantos vuelos hemos reguistrado
    '''
    try:
        with open('datos/nVuelo.txt','r') as archivoNumeroDeVuelo:
            numeroDeVuelo = archivoNumeroDeVuelo.read()
            numeroDeVuelo = int(numeroDeVuelo)
    except OSError as error:
        numeroDeVuelo = 0
    with open('datos/nVuelo.txt','w') as archivoNumeroDeVuelo:
        archivoNumeroDeVuelo.write(str(numeroDeVuelo + 1))
    return numeroDeVuelo
<<<<<<< HEAD:src/historialVuelos.py


def convertirAVuelo(datosOrigen, datosDestino):
=======


def convertirVuelo(datosOrigen, datosDestino):
>>>>>>> main:src/historial.py
    '''
    Funcion que devuelve datos los datos json un dato en string con la hora y numero de vuelo
    '''
    if(datosOrigen == None or datosDestino == None):
        return ""
    informacion = "Vuelo " + str(obtenerNumeroDeVuelo()) + " a las: "\
        + datetime.now().strftime("%H: %M: %S") + "\n"
    informacion += "Origen: " + datosOrigen.ubicacion + ", Temperatura: "\
        + datosOrigen.temperatura + "\n"
    informacion += "Destino: " + datosDestino.ubicacion + ", Temperatura: "\
        + datosDestino.temperatura + "\n"
    return informacion

