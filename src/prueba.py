import urllib.request
import urllib.parse
import http.client
import json
import csv

from tkinter import *
from tkinter import messagebox

with open('../data/dataset1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0] + "," + row[1] + "," + row[2] + ","+ row[3])

url = "https://api.openweathermap.org/data/2.5/weather?lat=19.3371&lon=-99.566&appid=9d92b9e2262e46e5b34601d6f706cf43"

f = urllib.request.urlopen(url,timeout=30)
djson = json.loads(f.read())
print(djson)
print(djson["weather"][0]["description"])

