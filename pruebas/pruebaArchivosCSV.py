from src.archivosCSV import escribirDestinos, leerDestinos, revisarCsv

def main():
    assert(revisarCsv('dataset1.csv'))
    assert(escribirDestinos("../pruebas/datosPrueba/baseDeDatos.csv", 71)\
           == [[['TLC', 19.3371, -99.566],['MTY', 25.7785, -100.107]]])
    assert(leerDestinos("ACA") == [['ACA', 16.7571, -99.754],\
                                   ['MEX', 19.4363, -99.0721]])
main()
