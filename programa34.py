class Circulo():
    def __init__(self,radio):
        self.radio=radio

    @property
    def radio(self):
        print("Estoy dando el radio")
        return self._radio
    
    @radio.setter
    def radio(self,radio):
        if radio>=0:
            self._radio = radio
        else:
            print("Radio debe ser positivo")
            self,_radio=0