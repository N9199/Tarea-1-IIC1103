"""Aqui se inicializa el Bingo y se simula cada turno"""
import tkinter as tk
import random
from tkinter import simpledialog
from Tarea_1 import *

bingo = Application(master=tk.Tk().geometry('{}x{}'.format("650", "650")))

def simular_turno():
    """Funcion que simula los turnos del bingo"""
    pass

bingo.jugadores = [Jugador(0), Jugador(0)]

for i in range(len(bingo.jugadores)):
    temp = simpledialog.askinteger("Monto", "Hola Jugador "+str(i+1)+", cual es monto que desea cargar para este juego?")
    while temp is None:
        temp = simpledialog.askinteger("Monto", "Jugador "+str(i+1)+", por favor ingrese un monto")
    bingo.jugadores[i].monto = temp
    bingo.mostrar_dinero(i+1, bingo.jugadores[i].monto)

bingo.button.config(command=simular_turno)

newgame = True
while newgame:
    print("Hello")
    for jugador in range(len(bingo.jugadores)):
        l = [[], [], [], [], []]
        for i in range(100):
            l[int(i/20)].append(i+1)

        for i in range(len(l)):
            temp = random.sample(l[i], k=5)
            print(temp)
            for j in range(5):
                print("pos_y:", j, "letra:", i, len(temp))
                bingo.colocar_numero(j, i, temp[j], 1)
    newgame = False

bingo.mainloop()