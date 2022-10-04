from src.aeropuerto import Aeropuerto
from src.cacheClima import CacheClima
from src.datosClima import DatosClima

def main():
    cacheEjemplo = CacheClima(11)
    cacheEjemplo.actualizarAPI("9d92b9e2262e46e5b34601d6f706cf43")
    aeropuerto1 = Aeropuerto('MEX', 19.4363, -99.0721)
    aeropuerto2 = Aeropuerto('ACA', 16.7571, -99.754)
    assert(cacheEjemplo.refrescarClima(aeropuerto1)), "No se actualizaron los datos"
    #assert(cacheEjemplo.buscarAeropuerto(None) != -1), "Aeropuerto no encontrado"
    #assert(cacheEjemplo.obtenerClima(aeropuerto1).__eq__(DatosClima(cacheEjemplo.realizarPeticion(aeropuerto1)))), "Datos JSON distintos"
    assert(cacheEjemplo.realizarPeticion(None) != None), "Datos JSON nulos"
main()
