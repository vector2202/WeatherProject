# WeatherProject
_Proyecto 1 de la Modelado y Programacion en el cual tenemos que desarrollar una aplicacion en la cual mediante el uso de servicios web, proporcionemos mediante un sistema amigable, datos climatologicos acerca de dos ciudades, ya que el sistema sera desarrollado para aeropuertos en los cuales se desea conocer el clima de la ciudad de origen y de la ciudad de destino._
## Comenzando 🚀
_Estas instrucciones permitiran hacer una copia del proyecto en funcionamiento para el fin de utilizarlo como sistema de consulta de clima acerca de vuelos._

### Pre-requisitos 📋
_La aplicacion esta desarrolada en python, para verificar que este instalado en el sistema, inserte en la terminal:_
```
python --version
```

_En caso de que no tenga instalado corra el siguiente comando:_

```
sudo dnf install python
```

_dnf en el caso de las distribuciones de redHat, depende de cada distribucion el comando_ 

_Tambien se requiere de tener pip instalado, por lo que hay que correr:_
```
command -v pip
```
_En caso de que no este instalado, ejecute la siguiente linea:_
```
$ python get-pip.py
```

_Ya con python y pip instalados, se necesita instalar request de Python, corriendo el siguiente comando:_
```
pip install request
```

### Instalación 🔧

_Para que el sistema funcione de manera correcta, tiene que tener un archivo donde los vuelos estan almacenados en el directorio data/_ 

_En el directorio actual hay un archivo denominado dataset1.csv, ese es el formato a seguir de los vuelos que queremos registrar en la base de datos, si queremos ingresar un nuevo formato basta remplazar este con el mismo nombre en este archivo se encuentran 3000 vuelos_

_En cuanto al sistema se refiere es necesario instalar setup.py para que se añada a las librerias de python los paquetes que usamos, en este caso basta con correr:_
```
sudo python setup.py install
```
_Se corre en modo administrador porque hay archivos que necesitamos permisos para escrbirlos, esto lo que hace es establecer que paquetes hay en los proyectos para que se puedan exportar facilmente_
## Ejecutando el programa ⚙️

### Pruebas de cada paquete 🔩
Las pruebas contenidas el el directorio pruebas cada archivo contiene la prueba de cada funcion por lo que para ejecutar las pruebas basta con correr:

```
python3.10 pruebas/pruebaNombreDeArchivo.py
```
Y se ejecutara las pruebas, obviamente se puede editar el documento para probar distintas entradas, si el archivo no genera ningun mensaje es que todas las pruebas fueron correctas
### Ejecucion del sistema ⌨️
Se le deja a continuacion la llave valida para que pueda ejecutar la aplicacion, esto es solo por calificacion, posteriormente se eliminara.
Llave valida: 9d92b9e2262e46e5b34601d6f706cf43

Para ejecutar el sistema, la aplicacion y que funcione se tiene que ejecutar:

```
python3.10 src/main.py
```

La interfaz es muy amigable e intuitiva, al abrirla necesitamos ingresar una llave API valida ya que por default es una llave vacia, solo se tiene que ingresar en el textbox y presionar el boton de API, para mostrar los ultimos 3 vuelos realizados basta con presionar el boton de historial y para registrar un vuelo primero se tiene que seleccionar una ciudad de origen, luego una ciudad de destino y presionar consultar y aparecen los datos del clima abajo de cada ciudad.

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Tkinter](https://docs.python.org/3/library/tk.html) - Usado para generar la interfaz
* [Request](https://docs.python.org/es/3.9/library/urllib.request.html) - Usado para las request de la API
* [JSON](https://docs.python.org/3/library/json.html) - Usado para filtrar los datos del csv
* [Datetime](https://docs.python.org/3/library/datetime.html) - Usado evitar hacer peticiones innecesarias
* [CSV](https://docs.python.org/3/library/csv.html) - Usado leer archivos csv

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Victor Torres** - *Desarrollador* - [vector2202](https://github.com/vector2202)
* **Diego Castro** - *Desarrollador* - [DiegoCastroRendon](https://github.com/DiegoCastroRendon)
