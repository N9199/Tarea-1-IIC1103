"""Aqui se inicializa el Bingo y se simula cada turno"""
import tkinter as tk
import random
import time
from tkinter import simpledialog
from Tarea_1 import *
root = tk.Tk().geometry('{}x{}'.format("550", "650"))
bingo = Application(master=root)


def new_game():
    for i in range(5):
        for j in range(5):
            for k in range(2):
                bingo.marcar_numero(i, j, False, k + 1)
    if bingo.preguntar_monto(1) == 0 and bingo.preguntar_monto(2) == 0:
        for i in range(len(bingo.jugadores)):
            temp = simpledialog.askinteger(
                "Monto", "Hola Jugador " + str(i + 1) + ", cual es monto que desea cargar para este juego?")
            while temp is None:
                temp = simpledialog.askinteger(
                    "Monto", "Jugador " + str(i + 1) + ", por favor ingrese un monto")
            bingo.mostrar_dinero(i + 1, temp)
    b = [[], [], [], [], []]
    for i in range(100):
        b[int(i / 20)].append(i + 1)
    
    for jugador in range(len(bingo.jugadores)):
        for i in range(len(b)):
            temp = random.sample(b[i], k=5)
            #if jugador:
                #temp = b[i][:5]
            #else:
                #temp = random.sample(b[i], k=5)
            for j in range(5):
                bingo.colocar_numero(j, i, str(temp[j]), jugador + 1)
    apuesta = []
    for i in range(len(bingo.jugadores)):
        monto = bingo.preguntar_monto(i + 1)
        temp = simpledialog.askinteger(
            "Apuesta", "Jugador " + str(i + 1) + " cuanto quieres apostar (disponible:" + str(monto) + ")")
        while temp is None or temp > monto or temp <= 0:
            temp = simpledialog.askinteger("Apuesta", "Jugador " + str(
                i + 1) + " por favor ingrese un valor valido (disponible:" + str(monto) + ")")
        apuesta.append(temp)
        bingo.mostrar_dinero(i + 1, monto - temp)

    lista = []
    for i in range(100):
        lista.append(i + 1)
    random.shuffle(lista)
    #lista = [45, 44, 43, 22, 62, 81, 1]
    #print(lista)
    return [apuesta, lista]


def simular_turno():
    """Funcion que simula los turnos del bingo"""
    global lista
    global apuesta
    temp = lista.pop()
    print(temp)
    a = 0
    for i in range(5): 
        if a == 2:
            break
        for j in range(5):
            if bingo.obtener_numero(i, j, 1) == temp:
                bingo.marcar_numero(i, j, True, 1)
                a += 1
            if bingo.obtener_numero(i, j, 2) == temp:
                bingo.marcar_numero(i, j, True, 2)
                a += 1
            if a == 2:
                break
    asdf2 = [1, 1]
    for i in range(5):
        for j in range(5):
            for k in range(2):
                if asdf2[k]==1 and not bingo.esta_marcado(i, j, k + 1):
                    asdf2[k] = 0
    #print(asdf2)
    for k in range(2):
        if asdf2[k]:
            asdf2[k] = 4
        else:
            asdf2[k] = 1
    #print(asdf2)
    for i in range(5):
        for j in range(5):
            for k in range(2):
                if asdf2[k]==1 and ((i < 2 and abs(j + i - 2) == 2) or (i >= 2 and j == 2)) and not bingo.esta_marcado(i, j, k + 1):
                    #print("Bingo")
                    asdf2[k] = 0
    #print(asdf2)
    for k in range(2):
        if asdf2[k]:
            asdf2[k] = 3
        else:
            asdf2[k] = 1
    #print(asdf2)
    for i in range(5):
        for k in range(2):
            if asdf2[k]==1 and not bingo.esta_marcado(i, i, k + 1):
                asdf2[k] = 0
    #print(asdf2)
    for k in range(2):
        if asdf2[k]:
            asdf2[k] = 2
        else:
            asdf2[k] = 1
    #print(asdf2)
    if asdf2 != [1, 1]:
        if asdf2[0] < asdf2[1]:
            monto = bingo.preguntar_monto(2)
            temp = 0
            for n in apuesta:
                temp += n
            bingo.mostrar_dinero(2, monto + temp)
        elif asdf2[0] > asdf2[1]:
            monto = bingo.preguntar_monto(1)
            temp = 0
            for n in apuesta:
                temp += n
            bingo.mostrar_dinero(1, monto + temp)
        else:
            for k in range(2):
                monto = bingo.preguntar_monto(k + 1)
                bingo.mostrar_dinero(k + 1, monto + apuesta[k])
        if bingo.preguntar_monto(1) == 0 or bingo.preguntar_monto(2) == 0:
            temp = "no"
        else:
            temp = simpledialog.askstring("Nuevo juego", "Quieren jugar de nuevo?")
            while temp.lower() != "si" and temp.lower() != "no":
                temp = simpledialog.askstring("Nuevo juego", "Quieren jugar de nuevo?")
        if temp == "no":
            print("Hasta luego")
            bingo.cerrar_ventana()
        else:
            temp = new_game()
            lista = temp[1]
            apuesta = temp[0]

for k in range(2):
    bingo.mostrar_dinero(k + 1, 0)

temp = new_game()
apuesta = temp[0]
lista = temp[1]
bingo.button.config(command=simular_turno)
bingo.mainloop()
