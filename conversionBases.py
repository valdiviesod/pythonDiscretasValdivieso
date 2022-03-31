import tkinter as tk
from tkinter import ttk
from cProfile import label
from tkinter import *
from tkinter import messagebox

raiz = tk.Tk()
raiz.title("Conversion de bases")
raiz.geometry("400x200")
raiz.resizable(False,False)

miFrame = Frame(raiz)
miFrame.pack(fill= "y", expand="True")
miFrame.config(width="350" , height="100")

labelTop = tk.Label(miFrame,
                    text = "Ingrese el numero y la base a la que se va a convertir:")
labelTop.place(x = "40", y = "30")

cuadroTexto = Entry(miFrame)
cuadroTexto.place(x= "105", y = "70")
cuadroTexto.config(justify="center")

comboBases = ttk.Combobox(miFrame, state= 'readonly')
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

botonConvertir = Button(miFrame, text = "Convertir", command= cambioBase)
botonConvertir.place(x = 130, y = 140)


raiz.mainloop()