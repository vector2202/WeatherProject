from src.listaDeAeropuertos import ListaDeAeropuertos


def main():
    listaPrueba = ListaDeAeropuertos(11)
    assert(listaPrueba.procesarVuelo(None))
    assert(listaPrueba.buscarAeropuertoOrigen('MEX'))
    lista = []
    assert(listaPrueba.buscarAeropuertoDestino(lista, 'MEX'))
    assert(listaPrueba.insertarAeropuerto('MEX'))
    assert(listaPrueba.escribirAeropuertosJson())
    assert(listaPrueba.obtenerNombres())
    
