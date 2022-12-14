from src.aeropuerto import Aeropuerto
from src.cacheClima import CacheClima
from src.historialVuelos import convertirAVuelo, obtenerNumeroDeVuelo

def main():
    assert(type(obtenerNumeroDeVuelo()) == int), "Tipo de dato incorrecto"
    aeropuerto1 = Aeropuerto('MEX', 19.4363, -99.0721)
    cacheClima = CacheClima(11)
    cacheClima.actualizarAPI("9d92b9e2262e46e5b34601d6f706cf43")
    cacheClima.refrescarClima(aeropuerto1)
    assert(type(convertirAVuelo(cacheClima.obtenerClima(None),\
                                cacheClima.obtenerClima(None))) == str)
    
main()
