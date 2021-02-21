from tkinter import *
from emoji import *

class Casilla:

    tipos = [":bomb:", "num", ""]

    frm = ""
    contenido=""

    def __init__(self, parentFrm, tipo=2, w=25, h=25):
        self.contenido = self.tipos[tipo]

        frm = Frame(parentFrm, width=w, height=h)
        btn = Button(frm)

        frm.grid_propagate(False)
        frm.columnconfigure(0, weight=1)
        frm.rowconfigure(0, weight=1)

        btn.grid(sticky="wens")

    def __str__(self):
        return emojize(self.contenido) if (self.contenido == self.tipos[0]) else self.contenido

    def isBomb(self):
        return self.casType=="bomba"
