class Dni():

    def _init_(self,numero):
        self.numero=numero

    def _calcular_letra(self):
        letras = 'TRWAGMYFPDXBNJZZSQVHLCKE'
        return letras[int(self.numero)%23]
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def letra(self):
        return self._letra
    
    @numero.setter
    def numero(self,numero):
        if len(numero)==8 and numero.isdigit():
            self._numero = numero
            self._letra = self._calcular_letra()
        else:
            self._numero=0
            self._letra = ""
            print("Dni Incorrecto")

    def mostrar(self):
        return self.numero+self.letra