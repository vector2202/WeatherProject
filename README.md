# WeatherProject
_Proyecto 1 de la Modelado y Programacion en el cual tenemos que desarrollar una aplicacion en la cual mediante el uso de servicios web, proporcionemos mediante un sistema amigable, datos climatologicos acerca de dos ciudades, ya que el sistema sera desarrollado para aeropuertos en los cuales se desea conocer el clima de la ciudad de origen y de la ciudad de destino._
## Comenzando 🚀
_Estas instrucciones permitiran hacer una copia del proyecto en funcionamiento para el fin de utilizarlo como sistema de consulta de clima acerca de vuelos._

### Pre-requisitos 📋
_
_Se necesita instalar request de Python_
```
pip install request
```

### Instalación 🔧

_Para que el sistema funcione de manera correcta, tiene que tener un archivo donde los vuelos estan almacenados en el directorio data/_

_En el directorio actual hay un archivo denominado dataset1.csv, ese es el formato a seguir de los vuelos que queremos registrar en la base de datos, si queremos ingresar un nuevo formato basta remplazar este con el mismo nombre_

## Ejecutando el programa ⚙️

_La interfaz es muy amigable e intuitiva, al abrirla apareceran opciones para ingresar nuestra propia llave API, nostros proporcionamos una por default pero si se quiere se puede modificar, solo basta presionar el boton de API, para mostrar los ultimos 3 vuelos realizados basta con presionar el boton de consultar y para registrar un vuelo primero se tiene que seleccionar una ciudad de origen, luego una ciudad de destino y presionar consultar._

_Para ejecutar la aplicacion debe correrse la siguiente lineada situada desde el directorio principal (Donde esta contenido este readme y todos los directorios)_

```
python src/app.py
```

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Tkinter](https://docs.python.org/3/library/tk.html) - Usado para generar la interfaz
* [Request](https://docs.python.org/es/3.9/library/urllib.request.html) - Usado para las request de la API
* [JSON](https://docs.python.org/3/library/json.html) - Usado para filtrar los datos del csv
* [Datetime](https://docs.python.org/3/library/datetime.html) - Usado evitar hacer peticiones innecesarias
* [CSV](https://docs.python.org/3/library/csv.html) - Usado leer archivos csv

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Victor Torres** - *Desarrollador* - [villanuevand](https://github.com/villanuevand)
* **Diego Castro** - *Desarrollador* - [fulanitodetal](#fulanito-de-tal)
