import math

class DatosClima:
    def __init__(self, datosJSON) -> None:
        self.ubicacion = datosJSON['name'] + "," + datosJSON['sys']['country']
        self.descripcion = datosJSON['weather'][0]['description']
        self.temperatura = str(math.floor(datosJSON['main']['temp'] - 273))
        self.sensacion = str(math.floor(datosJSON['main']['feels_like'] - 273))
        self.tempeaturaMinima = str(math.floor(datosJSON['main']['temp_min'] - 273))
        self.tempeaturaMaxima = str(math.floor(datosJSON['main']['temp_max'] - 273))
        self.icono = "http://openweathermap.org/img/w/" + str(datosJSON['weather'][0]['icon']) + ".png"
        #informacion += "Amanecer: " + str(datosJSON['sys']['sunrise']) + "\n"
        #informacion += "Atardecer: " + str(datosJSON['sys']['sunset']) + "\n"

    def __str__(self) -> str:
        return self.ubicacion + '\n' + self.descripcion + '\nTemperatura: ' + self.temperatura + '\nSensacion: ' + self.sensacion + '\nTemperatura Maxima: ' + self.tempeaturaMaxima + '\nTemperatura Minima: ' + self.tempeaturaMinima
    
    def __repr__(self) -> str:
        return self.ubicacion + '\n' + self.descripcion + '\nTemperatura: ' + self.temperatura + '\nSensacion: ' + self.sensacion + '\nTemperatura Maxima: ' + self.tempeaturaMaxima + '\nTemperatura Minima: ' + self.tempeaturaMinima
