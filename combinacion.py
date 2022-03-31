from cProfile import label
from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.title("Combinaciones")
raiz.geometry("500x300")
raiz.resizable(False,False)

miFrame = Frame(raiz)
miFrame.pack(fill= "y", expand="True")
miFrame.config(width="400" , height="300")

miLabel = Label(miFrame, text="Encuentre la combinacion de los valores dados", font= (18))
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


raiz.mainloop()