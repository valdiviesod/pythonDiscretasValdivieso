from cProfile import label
from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.title("Hallar numeros primos")
raiz.geometry("400x300")
raiz.resizable(False,False)

miFrame = Frame(raiz)
miFrame.pack(fill= "y", expand="True")
miFrame.config(width="400" , height="300")

miLabel = Label(miFrame, text="Encuentre los números primos de un rango dado", font= (18))
miLabel.place(x = "20", y = "10")

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

botonHallar = Button(miFrame, text = "Hallar", command= calculoPrimos)
botonHallar.place(x = 180, y = 220)
raiz.mainloop()