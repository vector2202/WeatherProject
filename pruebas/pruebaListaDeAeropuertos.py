from src.aeropuerto import Aeropuerto
from src.listaDeAeropuertos import ListaDeAeropuertos


def main():
    listaPrueba = ListaDeAeropuertos(11)
    vuelo = ['ACA', 'MEX', 16.7571, -99.754, 19.4363, -99.0721]
    aeropuerto1 = Aeropuerto('ACA', 16.7571, -99.754)
    aeropuerto2 = Aeropuerto('MEX', 19.4363, -99.0721)
    aeropuertoPrueba = Aeropuerto('MTY', 0 ,0)
    assert(listaPrueba.procesarVuelo(vuelo) != -1)
    assert(listaPrueba.buscarAeropuertoOrigen(aeropuerto1) != -1)
    assert(listaPrueba.buscarAeropuertoDestino(listaPrueba.lista, aeropuerto2))
    assert(listaPrueba.insertarAeropuerto(aeropuertoPrueba) != -1)
    listaPrueba.escribirAeropuertosJson()
    assert(listaPrueba.revisarArchivos())
    assert(listaPrueba.obtenerNombres() == ['ACA', 'MTY'])
    
main()
