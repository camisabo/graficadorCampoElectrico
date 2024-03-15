from typing import Any


class Carga:
    """Esta clase representa una carga q en un plano carteciano, por lo que tiene 
    como argumentos, su pocicion en el espacio asi como su valor de carga"""

    constante = 9*10^2

    def __init__(self, cordenadaX_: float, CordenadaY_: float, cantidadCarga_: float):
        self.__cordenadaX = cordenadaX_
        self.__CordenadaY = CordenadaY_
        self.__cantidadCarga = cantidadCarga_

    # Getter para cordenadaX
    @property
    def cordenadaX(self):
        return self.__cordenadaX

    # Setter para cordenadaX
    @cordenadaX.setter
    def cordenadaX(self, valor):
        self.__cordenadaX = valor

    # Getter para CordenadaY
    @property
    def CordenadaY(self):
        return self.__CordenadaY

    # Setter para CordenadaY
    @CordenadaY.setter
    def CordenadaY(self, valor):
        self.__CordenadaY = valor

    # Getter para cantidadCarga
    @property
    def cantidadCarga(self):
        return self.__cantidadCarga

    # Setter para cantidadCarga
    @cantidadCarga.setter
    def cantidadCarga(self, valor):
        self.__cantidadCarga = valor

    
