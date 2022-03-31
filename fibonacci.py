from cProfile import label
from tkinter import *
from tkinter import messagebox
from math import sqrt


raiz = Tk()
raiz.title("Hallar secuencia Fibonacci")
raiz.geometry("500x300")
raiz.resizable(False,False)

miFrame = Frame(raiz)
miFrame.pack(fill= "y", expand="True")
miFrame.config(width="400" , height="300")

miLabel = Label(miFrame, text="Encuentre la secuencia de Fibonacci en un rango dado", font= (18))
miLabel.place(x = "15", y = "10")

cuadroTexto = Entry(miFrame)
cuadroTexto.place(x= "210", y = "80")
cuadroTexto.config(justify="left")

cuadroTexto2 = Entry(miFrame)
cuadroTexto2.place(x= "210", y = "150")
cuadroTexto2.config(justify="left")

labelNInicial = Label(miFrame, text= "Ingrese el numero inicial: ")
labelNInicial.place(x= "50", y = "80")


labelNFinal = Label(miFrame, text= "Ingrese el numero final: ")
labelNFinal.place(x= "50", y = "150")

def verificar(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def fibonacci():
    listaResultado = []
    inicio = float(cuadroTexto.get())
    final = float(cuadroTexto2.get())
    n = 0
    num = verificar(n)
    while num <= final:
        if inicio <= num:
            listaResultado.append(num)
        n += 1
        num = verificar(n)

    messagebox.showinfo(message= "Los numeros de Fibonacci en el rango dado son: " + str(listaResultado))


botonHallar = Button(miFrame, text = "Hallar", command= fibonacci)
botonHallar.place(x = 180, y = 220)
raiz.mainloop()