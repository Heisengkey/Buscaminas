from enum import Enum

class tipoCasilla(Enum):
    bomba = 1
    numero = 2
    vacio = 3

class casilla:

    def __init__(self, tipoCas):


