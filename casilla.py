class casilla:

    def __init__(self, tipoCasilla, posX, posY):
        self.casType = tipoCasilla
        self.x = posX
        self.y = posY

    def __str__(self):
        return "Casilla de tipo: %s, en pos (%d, %d)" %(self.casType, self.x, self.y)

    def isBomb(self):
        return self.casType=="bomba"
