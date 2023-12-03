from programa33 import Punto
class Punto3d(Punto):
    def _int_(self,x=0,y=0,z=0):
        super()._init_(x,y)
        self.z=z

    @property
    def z(self):
        print("Doy z")
        return self._z
    
    @z.setter
    def z(self,z):
        print("Cambio z")
        self._z=z

    def mostrar(self):
        return super().mostrar()+":"+str(self.z)
    
    def distancia(self,otro):
        dx = self._x - otro._x
        dy = self._y - otro._y
        dz = self._z - otro._z
        return (dx*dx + dy*dy + dz*dz)**0.5
    