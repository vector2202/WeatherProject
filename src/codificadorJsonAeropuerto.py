import json
from src.aeropuerto import Aeropuerto

class CodificadorAeropuerto(json.JSONEncoder):
    def default(self, obj):
        '''
        Esta ciudad convierte el objeto Ciudades en un formato json para escribir en los archivos json
        '''
        if isinstance(obj, Aeropuerto):
            return [obj.nombre, obj.latitud, obj.longitud]
        return json.JSONEncoder.default(self, obj)
