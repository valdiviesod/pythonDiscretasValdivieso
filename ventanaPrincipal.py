from cgitb import text
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from math import sqrt
import tkinter as tk
from tkinter import ttk

raiz = Tk()
raiz.title("Ventana principal")
raiz.geometry("500x400")
raiz.resizable(False,False)


def abrirPrimos():
    def calculoPrimos():
        inicio = cuadroTexto.get()
        final = cuadroTexto2.get()
        listaResultado = []
        contador = 0
        for num in range(int(inicio), int(final) + 1):
                contadorNoPrimos = 0
                i = 2
                while i < num and contadorNoPrimos == 0:
                    modulo = num % i
                    if modulo == 0:
                            contadorNoPrimos += 1
                    else:
                        i += 1

                if contadorNoPrimos == 0:
                    contador += 1
                    listaResultado.append(num)    
                    if 1 in listaResultado:
                        listaResultado.remove(1)
                    else: 
                        continue
        messagebox.showinfo(message= "Hay" + " " + str(len(listaResultado)) + " " + "numeros primos en el rango dado, estos son: "+
        str(listaResultado))
    ventanaPrimos = Toplevel()
    ventanaPrimos.title("Hallar numeros primos")
    ventanaPrimos.geometry("400x300")
    raiz.resizable(False,False)
    miLabel = Label(ventanaPrimos, text="Encuentre los números primos de un rango dado", font= (18))
    miLabel.place(x = "20", y = "10")

    cuadroTexto = Entry(ventanaPrimos)
    cuadroTexto.place(x= "210", y = "80")
    cuadroTexto.config(justify="left")

    cuadroTexto2 = Entry(ventanaPrimos)
    cuadroTexto2.place(x= "210", y = "150")
    cuadroTexto2.config(justify="left")

    labelNInicial = Label(ventanaPrimos, text= "Ingrese el numero inicial: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFinal = Label(ventanaPrimos, text= "Ingrese el numero final: ")
    labelNFinal.place(x= "50", y = "150")

    botonHallar = Button(ventanaPrimos, text = "Hallar", command= calculoPrimos)
    botonHallar.place(x = 180, y = 220)
    
def abrirFibo():
    ventanaFibo = Toplevel()
    ventanaFibo.title("Hallar secuencia Fibonacci")
    ventanaFibo.geometry("500x300")
    ventanaFibo.resizable(False,False)

    miLabel = Label(ventanaFibo, text="Encuentre la secuencia de Fibonacci en un rango dado", font= (18))
    miLabel.place(x = "15", y = "10")

    cuadroTexto = Entry(ventanaFibo)
    cuadroTexto.place(x= "210", y = "80")
    cuadroTexto.config(justify="left")

    cuadroTexto2 = Entry(ventanaFibo)
    cuadroTexto2.place(x= "210", y = "150")
    cuadroTexto2.config(justify="left")

    labelNInicial = Label(ventanaFibo, text= "Ingrese el numero inicial: ")
    labelNInicial.place(x= "50", y = "80")


    labelNFinal = Label(ventanaFibo, text= "Ingrese el numero final: ")
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


    botonHallar = Button(ventanaFibo, text = "Hallar", command= fibonacci)
    botonHallar.place(x = 180, y = 220)

def abrirBases():
    ventanaBases = Toplevel()
    ventanaBases.title("Conversion de bases")
    ventanaBases.geometry("400x200")
    ventanaBases.resizable(False,False)

    labelTop = tk.Label(ventanaBases,
                    text = "Ingrese el numero y la base a la que se va a convertir:")
    labelTop.place(x = "40", y = "30")

    cuadroTexto = Entry(ventanaBases)
    cuadroTexto.place(x= "105", y = "70")
    cuadroTexto.config(justify="center")

    comboBases = ttk.Combobox(ventanaBases, state= 'readonly')
    comboBases.place(x = "95", y = "100")

    opciones = ["Base 6", "Base 7", "Base 8", "Base 9"] 

    comboBases['values'] = opciones

    def base6(n):
        final = []
        resultado = []
        while n != 0:
            final.append(n % 6)
            n = n // 6
        for i in reversed(final):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 6 es: "+ ''.join(map(str, resultado)))

    def base7(n):
        final = []
        resultado = []
        while n != 0:
            final.append(n % 7)
            n = n // 7
        for i in reversed(final):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 7 es: "+ ''.join(map(str, resultado)))

    def base8(n):
        final = []
        resultado = []
        while n != 0:
            final.append(n % 8)
            n = n // 8
        for i in reversed(final):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 8 es: "+ ''.join(map(str, resultado)))

    def base9(n):
        final = []
        resultado = []
        while n != 0:
            final.append(n % 9)
            n = n // 9
        for i in reversed(final):
            resultado.append(i)
        messagebox.showinfo(message= "El numero en base 9 es: "+ ''.join(map(str, resultado)))
        resultado.clear()

    def cambioBase():
        if comboBases.get() == "Base 6":
            base6(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 7":
            base7(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 8":
            base8(int(cuadroTexto.get()))
        elif comboBases.get() == "Base 9":
            base9(int(cuadroTexto.get()))

    botonConvertir = Button(ventanaBases, text = "Convertir", command= cambioBase)
    botonConvertir.place(x = 130, y = 140)
    

labelQueDesea = Label(raiz, text= "¿Que desea hacer?")
labelQueDesea.place(x = 195, y = 60)

botonFibonacci = Button(raiz, text = "Hallar numeros primos", command= abrirPrimos)
botonFibonacci.place(x = 180, y = 120)

botonBases = Button(raiz, text = "Hallar secuencia de Fibonacci", command=abrirFibo)
botonBases.place(x = 160, y = 170)

botonPrimos = Button(raiz, text = "Conversion de bases", command=abrirBases)
botonPrimos.place(x = 185, y = 220)

raiz.mainloop()

