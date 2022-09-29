import tkinter
from interfaz import Interfaz

def main():
    raiz = tkinter.Tk()
    raiz.title("CheckWeather")
    interfaz = Interfaz(raiz)
    interfaz.mainloop()
    
main()
