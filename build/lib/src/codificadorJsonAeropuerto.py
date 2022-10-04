import json
from src.aeropuerto import Aeropuerto

class CodificadorAeropuerto(json.JSONEncoder):
    '''
    Clase para cambiar el formato y poder usar json
    '''
    def default(self, objeto):
        '''
        Esta ciudad convierte el objeto Ciudades en un formato json para escribir en los archivos json
        '''
        if isinstance(objeto, Aeropuerto):
            return [objeto.nombre, objeto.latitud, objeto.longitud]
        return json.JSONEncoder.default(self, objeto)
