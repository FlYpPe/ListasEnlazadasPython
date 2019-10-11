
from  Modulo_Nodo import Nodo

#1) Crear lista enlazada
#2) Agregar elemento
# 		2a) Al inicio
#2b) Al final
#2c) En posicion especifica
#3) Eliminar elemento
#4) Recorrer lista
#5) Buscar elemento
#6) Vacia
#7) Cantidad de elementos
#8) Vaciar lista


class ListaEnlazada:

    def __init__(self):
        self.nodoInicio = None
        self.nodoFin = None

    def agregarInicio(self, dato):
        nn = Nodo(dato)
        if (self.nodoInicio == None):
            self.nodoInicio = nn
        else:
            nn.setEnlace(self.nodoInicio)
            self.nodoInicio = nn
    def mostrarElementos(self):
        nodAct = Nodo()
        if (self.nodoInicio==None):



l = ListaEnlazada()
l.agregarInicio(1)
