import tkinter
from src.interfaz import Interfaz

def main():
    raiz = tkinter.Tk()
    raiz.title("CheckWeather")
    interfaz = Interfaz(raiz)
    interfaz.mainloop()
    
main()
