import urllib.request
import urllib.parse
import http.client
import json
import csv

def funcionHash(vuelo):
    print("Funcion de los jsons")
    #Debemos crear una funcionHash que nos ayude a enmascarar nuestras ciudades para guardarlas en el arreglo
    return 0
    
def escribirDestinos():
    print("Escribiendo en cada json los posibles destinos.")
    #Abrimos el json con el codigo del origen:
    #escribimos un array con los destinos posibles en objeto{cod, long, lat}
    #El primer elemento del arreglo sera la informacion del mismo areopuerto
    with open('../data/dataset1.csv', 'r') as file:
        reader = csv.reader(file)
        #Tenemos que crear un arreglo que en vuelos[origen] = {vuelosDestino}
        #posteriormente recorremos el arreglo y escribimos todos los vuelos destino en los origen.json

        listaCiudades = []
        i = 0;
        for x in range(97):
            listaCiudades.append(0)

        #Vamos a guardar en el arreglo los n aereopuertos distintos con sus vuelos posibles.
        for row in reader:
            if(i > 0):
                if(row[0] != listaCiudades[funcionHash(row)]):
                    listaCiudades[funcionHash(row)] = row[0]
                    print("Ciudad: " + row[0] + "en " + str(abs(int (float(row[2]) + float(row[3]))) % 97))
            i += 1
            #print(row[0] + "," + row[1] + "," + row[2] + ","+ row[3] + ", " + row[4] + ", " + row[5])
            #row[0] contiene cdO, [1] cdD, [2] origenLat, [3] longOrigen, [4] latDest, [5] longDest
            #valorHash(row)
    
def leerDestinos():
    print("Leyendo los destinos")
    ciudadOrigen = "Aca"
    with open(ciudadOrigen + ".json") as archivo:
        datos = json.load(archivo)
    print(datos)
    #Leeremos los destinos y los guardamos en un arreglo
def guardarClima():
    print("Guardando el clima en una cache")
    #Crearemos un arreglo similar al de donde guardamos los vuelos pero ahora con el clima de cada aereopuerto en tupla con el tiempo cuando lo consultamos, con este tiempo podremos saber si necesitamos volver a calcular o no.

def main():        
        url = "https://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid=9d92b9e2262e46e5b34601d6f706cf43"
        f = urllib.request.urlopen(url,timeout=30)
        djson = json.loads(f.read())
        print(djson)
        print(djson["weather"][0]["description"])

main()
