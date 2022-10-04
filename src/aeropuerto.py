class Aeropuerto:
    '''
    Clase que hace referencia a los aeropuertos
    '''
    def __init__(self, nombre, latitud, longitud):
        '''
            Atributos de la clase Aeropuerto
        '''
        self.nombre = nombre
        self.longitud = longitud
        self.latitud = latitud


    def funcionHash(self, hashSize):
        ''' 
        Funcion que obtiene el valor hash de un aeropuerto, dado su nombre, longitud latitud
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
        Clase Aeropuerto para guardar el nombre y su longitud y latitud para calcular su clima
        '''
        return "[ " + self.nombre + ", " + str(self.latitud) +\
            ", " + str(self.longitud) + "]"
    

    def __eq__(self, objeto) -> bool:
        '''
        Funcion booleana en donde comparamos con los atributos de la clase.
        '''
        if(isinstance(objeto, Aeropuerto)):
            return objeto.nombre == self.nombre and\
                objeto.longitud == self.longitud and\
                objeto.latitud == self.latitud
        return False
    
