class Nodo:

    def __init__(self, dato=None):
        self.dato = dato
        self.enlace = None

    def getDato(self):
        return self.dato
    def setDato(self, dato):
        self.dato = dato
        pass
    def getEnlace(self):
        return self.enlace

    def setEnlace(self, enlace):
        self.enlace = enlace
        pass