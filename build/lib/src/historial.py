from datetime import datetime
def obtenerNumeroDeVuelo():
    try:
        archivoNumeroDeVuelo = open ('datos/nVuelo.txt','r')
        numeroDeVuelo = archivoNumeroDeVuelo.read()
        numeroDeVuelo = int(numeroDeVuelo)
        archivoNumeroDeVuelo.close()
    except OSError as error:
        numeroDeVuelo = 0
    archivoNumeroDeVuelo = open ('datos/nVuelo.txt','w')
    archivoNumeroDeVuelo.write(str(numeroDeVuelo + 1))
    archivoNumeroDeVuelo.close()
    return numeroDeVuelo
"""Funcion que devuelve cuantos vuelos hemos reguistrado"""

def convertirVuelo(datosOrigen, datosDestino):
    if(datosOrigen == None or datosDestino == None):
        return ""
    informacion = "Vuelo " + str(obtenerNumeroDeVuelo()) + " a las: " + datetime.now().strftime("%H: %M: %S") + "\n"
    informacion += "Origen: " + datosOrigen.ubicacion + ", Temperatura: " + datosOrigen.temperatura + "\n"
    informacion += "Destino: " + datosDestino.ubicacion + ", Temperatura: " + datosDestino.temperatura + "\n"
    return informacion
"""Funcion que devuelve datos los datos json un dato en string con la hora y numero de vuelo"""

