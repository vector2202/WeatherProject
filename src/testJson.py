import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Ciudades):
            return [obj.nombre, obj.longitud, obj.latitud]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
class Ciudades:
    def __init__(self, nombre, longitud, latitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud

data = {}
acapulco = Ciudades("ACA", 99, -10)
mexico = Ciudades("MEX", 10, 77)
monterrey = Ciudades("MTY", 10, 77)
data['ciudad'] = []
data['ciudad'].append(acapulco)
data['ciudad'].append(mexico)
data['ciudad'].append(monterrey)
ciudades = [acapulco, mexico, monterrey]
#with open(acapulco.nombre + '.json', 'w') as archivo:
#    for ciudad in data['ciudad']:
#        json.dump((ciudad).__dict__, archivo, indent=4)
    #for x in data['ciudad']:
    #    json.dump(ComplexEncoder().encode(x), archivo, indent=4)

#with open("ACA.json") as archivo:
#    datos = json.load(archivo)
#    print(datos)
