import math
class Punto():
    """Representacion de un punto en el plano, los atributos son X y Y
    que representan los valores de las coordenadas cartesianas."""

def _init_(self,x=0,y=0):
    self.x=x
    self.y=y

def mostrar(self):
    return str(self.x)+":"+str(self.y)

def distancia(self, otro):
    """Decuelve la distancia entre ambos puntos"""
    dx = self.x - otro.x
    dy = self.y - otro.y
    return math.sqrt((dx*dx + dy*dy))
