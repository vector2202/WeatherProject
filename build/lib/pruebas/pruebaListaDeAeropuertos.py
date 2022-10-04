from src.aeropuerto import Aeropuerto
from src.listaDeAeropuertos import ListaDeAeropuertos


def main():
    listaPrueba = ListaDeAeropuertos(11)
    vuelo = ['ACA', 'MEX', 16.7571, -99.754, 19.4363, -99.0721]
    aeropuerto1 = Aeropuerto('ACA', 16.7571, -99.754)
    aeropuerto2 = Aeropuerto('MEX', 19.4363, -99.0721)
    aeropuertoPrueba = Aeropuerto('MTY', 0 ,0)
    assert(listaPrueba.procesarVuelo(vuelo) != -1), "Aeropuerto no insertado"
    assert(listaPrueba.buscarAeropuertoOrigen(aeropuerto1) != -1), "Aeropuerto inexistente"
    #assert(listaPrueba.buscarAeropuertoDestino([], aeropuerto2.nombre)), "Aeropuerto inexistente"
    assert(listaPrueba.insertarAeropuertoOrigen(aeropuertoPrueba) != -1), "No se inserto el aeropuerto"
    listaPrueba.escribirAeropuertosJson()
    #assert(listaPrueba.revisarArchivosJSON()), "JSONs no escritos"
    assert(listaPrueba.obtenerNombres() == ['ACA', 'MTY'])
    
main()
