import math

class DatosClima:
    '''
    Clase para obtener los datos del clima usando json
    '''
    def __init__(self, datosJSON) -> None:
        '''
        Atributos de la clase para cada dato del clima
        '''
        
        self.ubicacion = datosJSON['name'] + ", " + datosJSON['sys']['country']
        self.descripcion = datosJSON['weather'][0]['description']
        self.temperatura = str(math.floor(datosJSON['main']['temp'] - 273))
        self.sensacion = str(math.floor(datosJSON['main']['feels_like'] - 273))
        self.tempeaturaMinima = str(math.floor(datosJSON['main']['temp_min']\
                                               - 273))
        self.tempeaturaMaxima = str(math.floor(datosJSON['main']['temp_max']\
                                               - 273))
        self.icono = "http://openweathermap.org/img/w/" +\
            str(datosJSON['weather'][0]['icon']) + ".png"


    def __str__(self) -> str:
        '''
        Funcion que nos regresa un string de la informacion requerida
        '''
        return self.ubicacion + '\n' + self.descripcion +\
            '\nTemperatura: ' + self.temperatura + '\nSensacion: '\
            + self.sensacion + '\nTemperatura Maxima: '\
            + self.tempeaturaMaxima + '\nTemperatura Minima: '\
            + self.tempeaturaMinima


    def __repr__(self) -> str:
        '''
        Funcion que regresa la representacion del objeto en string 
        '''
        return self.ubicacion + '\n' + self.descripcion +\
            '\nTemperatura: ' + self.temperatura + '\nSensacion: '\
            + self.sensacion + '\nTemperatura Maxima: '\
            + self.tempeaturaMaxima + '\nTemperatura Minima: '\
            + self.tempeaturaMinimai


    def __eq__(self, objeto) -> bool:
        '''
        Funcion para comparar ciertas instancias
        '''
        if isinstance(objeto, DatosClima):
            return self.ubicacion == objeto.ubicacion and\
                self.temperatura == objeto.temperatura and\
                self.tempeaturaMaxima == objeto.tempeaturaMaxima and\
                self.tempeaturaMinima == objeto.tempeaturaMinima
        return False


    def __ne__(self, objeto) -> bool:
        '''
        Funcion para cuando nuestros objetos no son iguales
        '''
        return not self.__eq__(objeto)
