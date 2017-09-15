"""Aqui se inicializa el Bingo y se simula cada turno"""
import tkinter as tk
import random
from tkinter import simpledialog
from Tarea_1 import *
root = tk.Tk().geometry('{}x{}'.format("550", "650"))
bingo = Application(master=root)

def simular_turno():
    """Funcion que simula los turnos del bingo"""
    pass

for i in range(len(bingo.jugadores)):
    temp = simpledialog.askinteger("Monto", "Hola Jugador "+str(i+1)+", cual es monto que desea cargar para este juego?")
    while temp is None:
        temp = simpledialog.askinteger("Monto", "Jugador "+str(i+1)+", por favor ingrese un monto")
    bingo.mostrar_dinero(i+1, temp)

bingo.button.config(command=simular_turno)

newgame = True
while newgame:
    for jugador in range(len(bingo.jugadores)):
        l = [[], [], [], [], []]
        for i in range(100):
            l[int(i/20)].append(i+1)

        for i in range(len(l)):
            temp = random.sample(l[i], k=5)
            for j in range(5):
                bingo.colocar_numero(j, i, str(temp[j]), jugador+1)
    newgame = False

bingo.mainloop()
