class Aeropuerto:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud
        
    def funcionHash(self, hashSize):
        ''' 
        Funcion que obtiene el valor hash de una ciudad, dado su nombre, longitud ciudad
        '''
        suma = 0
        for caracter in self.nombre: #Suma de valores ASCII
            suma += ord(caracter)
        return (suma + abs(int(float(self.latitud))) +\
                abs(int(float(self.longitud)))) % hashSize

    def __str__(self):
        return "[ " + self.nombre + ", " + str(self.latitud) +\
            ", " + str(self.longitud) + "]"
    
    def __repr__(self):
        '''
        Clase ciudades para guardar la ciudad y su longitud y latitud para calcular su clima
        '''
        return "[ " + self.nombre + ", " + str(self.latitud) +\
            ", " + str(self.longitud) + "]"
<<<<<<< HEAD
    def __eq__(self, objeto) -> bool:
        if(isinstance(objeto, Aeropuerto)):
            return objeto.nombre == self.nombre and\
                objeto.longitud == self.longitud and\
                objeto.latitud == self.latitud
        return False
=======
    
>>>>>>> main
