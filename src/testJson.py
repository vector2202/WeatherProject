import json
from datetime import datetime, timedelta
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
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
data = {}

acapulco = Ciudades("ACA", 99, -10)
mexico = Ciudades("MEX", 10, 77)
monterrey = Ciudades("MTY", 10, 77)
datas = {"ciudad":{acapulco, mexico, monterrey}}
data['ciudad'] = []
data['ciudad'].append(acapulco)
data['ciudad'].append(mexico)
data['ciudad'].append(monterrey)
ciudades = [acapulco, mexico, monterrey]
array3 = {'ciudad':[acapulco, mexico, monterrey]}
#print(json.dumps(datas))
#with open(acapulco.nombre + '.json', 'w') as archivo:
#    json.dump(data, archivo, indent=4, cls=ComplexEncoder)
#    for ciudad in datas["ciudad"]:
#        json.dump(ciudad.__dict__, archivo, indent=4)
    #for x in data['ciudad']:
    #    json.dump(ComplexEncoder().encode(x), archivo, indent=4)

#with open("ACA.json") as archivo:
#    datos = json.load(archivo)
#    for d in datos:
#        print(d)
now = datetime.now()
now2 = datetime.now()
if(now2 - now > timedelta(seconds=0)):
    print("CHK1" + str(now2-now))
print(datetime.now().strftime("%H: %M: %S"))
 #   for d in datos['ciudad']:
 #       print(d)
