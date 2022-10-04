from src.aeropuerto import Aeropuerto
from src.procesarArchivos import escribirDestinos, leerDestinos, revisarCSV
def elementosDistintos(x1, x2):
    if(len(x1) == 0 and len(x2) == 0):
        return False
    elif(len(x2) != 2):
        return True
    else:
        for i in range(len(x1)):
            if(not x1[i].__eq__(Aeropuerto(x2[i][0], x2[i][1], x2[i][2]))):
                return True
        return False

def compararLista(lista1, lista2):
    if(len(lista1) != len(lista2)):
        return False
    for i in range(len(lista1)):
        if(elementosDistintos(lista1[i], lista2[i])):
            return False
    return True
def main():
    assert(revisarCSV('dataset1.csv')), "Base de datos invalida"
    lista = escribirDestinos("../pruebas/datosPrueba/baseDeDatos.csv", 2)
    assert(compararLista(lista.lista, [[], [['TLC', 19.3371, -99.566], ['MTY', 25.7785, -100.107]],[]])), "Destinos invalidos"
    assert(leerDestinos('ACA') == [['ACA', 16.7571, -99.754],\
                                   ['MEX', 19.4363, -99.0721]]), "Aeropuerto no valido"
main()
