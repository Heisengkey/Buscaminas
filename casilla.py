from tkinter import *
from emoji import *

class Casilla:

    tipos = [":bomb:", "num", ""]

    def __init__(self, parentFrm, tipo=2, w=25, h=25, coorX, coorY):
        # __contenido = self.tipos[tipo]
        #
        # __frm = Frame(parentFrm, width=w, height=h)
        # btn = Button(__frm)
        #
        #
        # __frm.grid_propagate(False)
        # __frm.columnconfigure(0, weight=1)
        # __frm.rowconfigure(0, weight=1)
        #
        # btn.grid(sticky="wens")
        __x = coorX
        __y = coorY

    def __str__(self):
        return emojize(self.contenido) if (self.contenido == self.tipos[0]) else self.contenido

    def isBomb(self):
        return self.casType=="bomba"

    def getNumBombAdyacent(self):
        pass