from casilla import casilla
from tkinter import *

dimx=25
dimy=25

def reset_tablero(arg):
    cas1 = casilla("bomba", 1, 1)
    print(cas1)
    print(cas1.isBomb())

    cas2 = casilla("vacio", 3, 3)
    print(cas2)
    print(cas2.isBomb())

    cas3 = casilla("numero", 0, 1)
    print(cas3)
    print(cas3.isBomb())


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

    Label(about, text="Aqui iria un about").pack()

    about.mainloop()


def crea_tablero(dimx, dimy, bombas):



    frm = Frame()

    for j in range(dimy):
        for i in range(dimx):
            frm = Frame(root, width=25, height=25)
            btn = Button(frm)

            frm.grid_propagate(False)
            frm.columnconfigure(0, weight=1)
            frm.rowconfigure(0, weight=1)

            frm.grid(row=j, column=i)
            btn.grid(sticky="wens")


if __name__ == '__main__':
    # Crea una ventana root de 400x400, bloquea el tamaño y añade un icono.
    root = Tk()
    root.geometry('500x25')
    root.title("Buscaminas!!")
    root.iconbitmap("img/gradiente.ico")

    # Crea una barra menu
    menubar = Menu(root)

    # Crea la opcion partida para el menubar y añade el comando exit y reset
    partida = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Partida", menu=partida)
    partida.add_command(label="Nueva Partida", command=reset_tablero)
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

    # Crea tablero
    crea_tablero(20, 20, 7)

    root.config(menu=menubar)
    root.bind('<Return>', reset_tablero)
    root.mainloop()
