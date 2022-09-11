import json

class Ciudades:
    def __init__(self, nombre, longitud, latitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud


acapulco = Ciudades("ACA", 99, -10)
mexico = Ciudades("MEX", 10, 77)
monterrey = Ciudades("MTY", 10, 77)
ciudades = [acapulco, mexico, monterrey]
#with open(ciudades[0].nombre + ".json", 'w') as archivo:
#    for ciudad in ciudades:
#        json.dump(ciudad.__dict__, archivo, indent=4)

with open("ACA.json") as archivo:
    datos = json.load(archivo)
    for x in datos:
        print(x)
    
#    print(datos)
