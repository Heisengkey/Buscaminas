# from casilla import Casilla
# from tkinter import *
# from emoji import *
#
# def open_ranking():
#     ranking = Toplevel(root)
#     ranking.title("Ranking")
#     ranking.geometry("200x200")
#     ranking.maxsize(width=200, height=200)
#     ranking.minsize(width=200, height=200)
#
#     Label(ranking, text="Aqui iria un ranking").pack()
#
#     ranking.mainloop()
#
#
# def open_version():
#     version = Toplevel(root)
#     version.title("Ranking")
#     version.geometry("200x200")
#     version.maxsize(width=200, height=200)
#     version.minsize(width=200, height=200)
#
#     Label(version, text="Aqui iria un version").pack()
#
#     version.mainloop()
#
#
# def open_about():
#     about = Toplevel(root)
#     about.title("Ranking")
#     about.geometry("200x200")
#     about.maxsize(width=200, height=200)
#     about.minsize(width=200, height=200)
#
#     Label(about, text="Size: {}".format(root.geometry())).pack()
#
#     about.mainloop()
#
#
# # def crea_tablero(dimx, dimy, bombas):
# #     frm = Frame()
# #
# #     for j in range(dimy):
# #         for i in range(dimx):
# #             # sq = Casilla(frm,0)
# #             # sq.frm.pack()
# #             pass
# #
# #     # frm.pack()
#
# def muestraHijos(self):
#     print(self)
#
#
# def rellena_tablero(tablero):
#     dimx = 20
#     dimy = 20
#
#     btn = Button()
#
#     for i in range(dimx):
#         for j in range(dimy):
#
#             btn = Button(tablero, text="", command=muestraHijos)
#             btn.pack(side=LEFT)
#
#
#
# if __name__ == '__main__':
#     # Crea una ventana root de 400x400, bloquea el tamaño y añade un icono.
#     root = Tk()
#     root.geometry('500x520')
#     root.title("Buscaminas!!")
#     root.iconbitmap("img/gradiente.ico")
#
#     # Crea una barra menu
#     menubar = Menu(root)
#
#     # Crea la opcion partida para el menubar y añade el comando exit y reset
#     partida = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Partida", menu=partida)
#     partida.add_command(label="Nueva Partida")
#     partida.add_command(label="Exit", command=root.destroy)
#
#     # Crea la opcion datos para el menubar y añade el comando ranking
#     datos = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Datos", menu=datos)
#     datos.add_command(label="Ranking", command=open_ranking)
#
#     # Crea la opcion help para el menubar y añade los comandos version y about
#     help = Menu(menubar, tearoff=0)
#     menubar.add_cascade(label="Ayuda", menu=help)
#     help.add_command(label="Version", command=open_version)
#     help.add_command(label="About", command=open_about)
#
#     # Crea dos frames, uno para el estado de la partida y otro para el tablero
#     estado = Frame(root, bg="grey", height=25)
#     estadoBtn = Button(estado, text=emojize(":alien:"))
#
#     tablero = Frame(root)
#
#
#     # Packing de los frames
#     estado.pack(fill=X)
#     estadoBtn.pack()
#     tablero.pack(expand=True, fill=BOTH)
#     tablero.config(bg="black")
#
#     rellena_tablero(tablero)
#
#     root.config(menu=menubar)
#
#
#
#     root.mainloop()

import random as rnd
from emoji import *


def cuentaBombasAdy(y, x, listaPartida):
    # Contador para bombas
    nBombs = 0

    # Lista para las coordenadas de los vecinos de nuestra pos
    coordList = []

    # Lista con todas los posibles vecinos, para no hacer lios con tanta coordenada
    coords = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1],  # 0   1   2       Estas son las pos de la lista en
              [x - 1, y], [x + 1, y],  # 3       4       forma de tablero, para una mejor lectura
              [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]  # 5   6   7

    if x in range(1, len(listaPartida[x]) - 1) and y in range(1, len(listaPartida) - 1):
        coordList = coords
    else:
        if x == 0 and y == 0:  # Esq sup izq
            coordList.append(coords[4])
            coordList.append(coords[6])
            coordList.append(coords[7])
        if (x == 0) and (y == (len(listaPartida) - 1)):  # Es inf izq
            coordList.append(coords[1])
            coordList.append(coords[2])
            coordList.append(coords[4])
        if (x == (len(listaPartida[x]) - 1)) and (y == 0):  # Esq sup der
            coordList.append(coords[3])
            coordList.append(coords[5])
            coordList.append(coords[6])
        if (x == (len(listaPartida[x]) - 1)) and (y == (len(listaPartida) - 1)):  # Esq inf der
            coordList.append(coords[0])
            coordList.append(coords[1])
            coordList.append(coords[3])
        if (x == 0) and (y in range(1, len(listaPartida) - 1)):  # Lateral
            coordList.extend(coords[1:3])
            coordList.append(coords[4])
            coordList.extend(coords[6:])
        if y == 0 and x in range(1, len(listaPartida) - 1):
            coordList.extend(coords[3:])
        if x == len(listaPartida[x]) - 1 and y in range(1, len(listaPartida) - 1):
            coordList.extend(coords[:2])
            coordList.append(coords[3])
            coordList.extend(coords[5:7])
        if y == len(listaPartida) - 1 and x in range(1, len(listaPartida) - 1):
            coordList.extend(coords[:5])

    # print("Para las coord: {}, {} miramos las coord {}".format(x, y, coordList))

    for cX, cY in coordList:
        if listaPartida[cX][cY] == 1:
            nBombs += 1

    return nBombs


def creaTableroOld(n, lista):
    simbolos = [":white_large_square:", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:"]
    listaPartida = [lista[i:i + n] for i in range(0, len(lista), n)]

    dibujaTemp(listaPartida)

    errores = []

    tablero = [[] for i in range(n)]

    for y in range(n):  # Recorremos las lineas del tablero
        for x in range(n):  # Recorremos cada casilla en la linea
            if listaPartida[y][x] == 0:
                tablero[y].append(cuentaBombasAdy(y, x, listaPartida))
            else:
                tablero[y].append(emojize(":bomb:"))
    dibujaTemp(tablero, "tableroTemConstruido.txt")
    return tablero


def generaBombas(nBomb, n):
    lista = list()
    for i in range(nBomb):
        rndCoor = rnd.randrange(0, n ** 2)
        while rndCoor in lista:
            rndCoor = rnd.randrange(0, n ** 2)
        lista.append(rndCoor)
    return lista


def dibujaTemp(mapa, path="tableroTem.txt"):
    f = open(path, "w")
    print(mapa)
    for linea in mapa:
        for cas in linea:
            if cas == emojize(":bomb:"):
                f.write("* ")
            else:
                f.write(f"{cas} ")
        f.write("\n")


def dibujaTablero(mapa):
    f = open("tablero.txt", "w")
    for linea in mapa:
        for casilla in linea:
            if casilla == 0:
                f.write("0")
            elif casilla in range(1, 9):
                f.write(casilla.__str__())
            else:
                f.write("*")
            f.write(" ")
        f.write("\n")
    f.close()

    print(f"Fichero guradado como {f.name}")



if __name__ == '__main__':
    # n = int(input("Introduce n para tablero: "))
    # numBombas = int(input("Introduce el numero de bombas: "))

    n = 9
    numBombas = 10

    listaBomb = generaBombas(numBombas, n)
    lista = [1 if x in listaBomb else 0 for x in range(n ** 2)]
    listaCasillas = [Casilla(x % n, x // n, "bomb") if x in listaBomb else Casilla(x % n, x // n, "void") for x in
                     range(n ** 2)]

    # print(prob)
    # print(lista)
    # print("Num de bombas = {}".format(lista.count(1)))
    # print("Num de casillas libres = {}".format(lista.count(0)))
    # print("Mostrando tablero")
    # print(range(n))

    print(f"Tablero antigüo:    {creaTableroOld(n, lista)}")
    print(f"Tablero nuevo:      {creaTablero(n, listaCasillas)}")

    # mapa = [lista[i:i + n] for i in range(0, len(lista), n)]
    #
    # print(f"Max para la y es {len(mapa)}")
    # print(f"Max para la x es {len(mapa[0])}")
    #
    dibujaTablero(creaTableroOld(n, lista))

    # coords = [[x,y] for x in range(pow(len(lista),-2))]
