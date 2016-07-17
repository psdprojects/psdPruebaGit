import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
#from matplotlib.backend_bases import key_press_handler
import threading
import socket

from matplotlib.figure import Figure
from Tkinter import Label
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()
root.wm_title("PSD projects")
titleLabel = Label(root, text="Developed by PSD projects")
titleLabel.pack()
lista1 = [0]
contador = 0
interfazCreada = False

f = plt.figure()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.139", 10111))
s.listen(1)
sc, addr = s.accept()

def socketConnection():
    global sc, interfazCreada

    if interfazCreada == False:
        interfazCreada = True
        print("interfaz creada")
        while True:
            datoRecibido = sc.recv(1024)            
            print("dato")
            insertPoint()
        
        
def insertPoint():
    global contador, lista1, canvas, f
    contador = contador + 1
    lista1.append(contador)
    #threading.Timer(1,insertPoint).start()
    plt.subplot(2, 1, 1)
    plt.plot(lista1,marker='o', linestyle='-', color='g', label = "Temperatura 1")
    plt.subplot(2, 1, 2)
    plt.plot(lista1,marker='o', linestyle='-', color='g', label = "Temperatura 1")
    f.canvas.draw()
    plt.cla()
    #a.plot(lista1,marker='o', linestyle='-', color='g', label = "Temperatura 1")
    print("inserta punto")

    # a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
#canvas.show()
#canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

#Barra de navegacion (Button bar) figura python
toolbar = NavigationToolbar2TkAgg(canvas, root)
toolbar.update()
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

def evento():
    print("evento")

button = Tk.Button(root, text='Evento', command=evento)
button.pack(side=Tk.BOTTOM)
t = threading.Thread(target=socketConnection)
t.start()
Tk.mainloop()

