from src.listaDeAeropuertos import ListaDeAeropuertos


def main():
    listaPrueba = ListaDeAeropuertos(11)
    vuelo = ['ACA', 'MEX', 16.7571, -99.754, 19.4363, -99.0721]
    assert(listaPrueba.procesarVuelo(vuelo))
    assert(listaPrueba.buscarAeropuertoOrigen('ACA'))
    lista = []
    assert(listaPrueba.buscarAeropuertoDestino(lista, 'MEX'))
    assert(listaPrueba.insertarAeropuerto('MTY'))
    assert(listaPrueba.escribirAeropuertosJson())
    assert(listaPrueba.obtenerNombres())
    
main()
