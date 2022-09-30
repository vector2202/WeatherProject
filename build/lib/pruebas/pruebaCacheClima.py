from src.aeropuerto import Aeropuerto
from src.cacheClima import CacheClima


def main():
    cacheEjemplo = CacheClima(11)
    aeropuerto1 = Aeropuerto('MEX', 19.4363, -99.0721)
    #aeropuerto2 = Aeropuerto('ACA', 16.7571, -99.754)
    cacheEjemplo.actualizarAPI("9d92b9e2262e46e5b34601d6f706cf43")
    assert(cacheEjemplo.refrescar(aeropuerto1))
    assert(cacheEjemplo.buscarAeropuerto(aeropuerto1))
    assert(cacheEjemplo.obtenerClima(aeropuerto1) ==\
           cacheEjemplo.realizarPeticion(aeropuerto1))
main()