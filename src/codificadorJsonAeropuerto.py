import json
from src.aeropuerto import Aeropuerto

class CodificadorAeropuerto(json.JSONEncoder):
    '''
    Clase para cambiar el formato y poder usar json
    '''
    def default(self, objeto):
        '''
        Esta clase convierte el objeto Aeropuerto en un formato json para escribir en los archivos json
        '''
        if isinstance(objeto, Aeropuerto):
            return [objeto.nombre, objeto.latitud, objeto.longitud]
        return json.JSONEncoder.default(self, objeto)
