from casilla import Casilla
from tkinter import *
from emoji import *

def open_ranking():
    ranking = Toplevel(root)
    ranking.title("Ranking")
    ranking.geometry("200x200")
    ranking.maxsize(width=200, height=200)
    ranking.minsize(width=200, height=200)

    Label(ranking, text="Aqui iria un ranking").pack()

    ranking.mainloop()


def open_version():
    version = Toplevel(root)
    version.title("Ranking")
    version.geometry("200x200")
    version.maxsize(width=200, height=200)
    version.minsize(width=200, height=200)

    Label(version, text="Aqui iria un version").pack()

    version.mainloop()


def open_about():
    about = Toplevel(root)
    about.title("Ranking")
    about.geometry("200x200")
    about.maxsize(width=200, height=200)
    about.minsize(width=200, height=200)

    Label(about, text="Size: {}".format(root.geometry())).pack()

    about.mainloop()


# def crea_tablero(dimx, dimy, bombas):
#     frm = Frame()
#
#     for j in range(dimy):
#         for i in range(dimx):
#             # sq = Casilla(frm,0)
#             # sq.frm.pack()
#             pass
#
#     # frm.pack()

def muestraHijos(self):
    print(self)


def rellena_tablero(tablero):
    dimx = 20
    dimy = 20

    btn = Button()

    for i in range(dimx):
        for j in range(dimy):

            btn = Button(tablero, text="", command=muestraHijos)
            btn.pack(side=LEFT)



if __name__ == '__main__':
    # Crea una ventana root de 400x400, bloquea el tamaño y añade un icono.
    root = Tk()
    root.geometry('500x520')
    root.title("Buscaminas!!")
    root.iconbitmap("img/gradiente.ico")

    # Crea una barra menu
    menubar = Menu(root)

    # Crea la opcion partida para el menubar y añade el comando exit y reset
    partida = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Partida", menu=partida)
    partida.add_command(label="Nueva Partida")
    partida.add_command(label="Exit", command=root.destroy)

    # Crea la opcion datos para el menubar y añade el comando ranking
    datos = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Datos", menu=datos)
    datos.add_command(label="Ranking", command=open_ranking)

    # Crea la opcion help para el menubar y añade los comandos version y about
    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Ayuda", menu=help)
    help.add_command(label="Version", command=open_version)
    help.add_command(label="About", command=open_about)

    # Crea dos frames, uno para el estado de la partida y otro para el tablero
    estado = Frame(root, bg="grey", height=25)
    estadoBtn = Button(estado, text=emojize(":alien:"))

    tablero = Frame(root)


    # Packing de los frames
    estado.pack(fill=X)
    estadoBtn.pack()
    tablero.pack(expand=True, fill=BOTH)
    tablero.config(bg="black")

    rellena_tablero(tablero)

    root.config(menu=menubar)



    root.mainloop()
