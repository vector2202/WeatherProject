class Aeropuerto:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        
    def funcionHash(self, hashSize):
        suma = 0
        for caracter in self.nombre:#Suma de valores ASCII
            suma += ord(caracter)
        return (suma + abs(int(float(self.latitud))) +\
                abs(int(float(self.longitud)))) % hashSize
    """ Funcion que obtiene el valor hash de una ciudad, dado su nombre, longitud ciudad """

    def __str__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) +\
            ", " + str(self.longitud) + "]"
    
    def __repr__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) +\
            ", " + str(self.longitud) + "]"
    
    """" Clase ciudades para guardar la ciudad y su longitud y latitud para calcular su clima """
