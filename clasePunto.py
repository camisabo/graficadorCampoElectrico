from claseCarga import Carga
from math import sqrt
class Punto:
    # Declaracion de variables
    __cargaDeprueba:float = 1
    __cordenadaX = None
    __cordenadaY = None
    __moduloFuerza = None
    __fuerzasSobreElPunto = []

    def __init__(self, cordenadaX_: float, CordenadaY_: float):
        self.__cordenadaX = cordenadaX_
        self.__cordenadaY = CordenadaY_
        self.__moduloFuerza:float = 0
        self.__fuerzasSobreElPunto = []

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
        return self.__cordenadaY

    # Setter para CordenadaY
    @CordenadaY.setter
    def CordenadaY(self, valor):
        self.__cordenadaY = valor
    
    # Getter para ModuloFuerza
    @property
    def ModuloFuerza(self):
        return self.__moduloFuerza
    
    # Setter para ModuloFuerza
    @ModuloFuerza.setter
    def ModuloFuerza(self, valor):
        self.__moduloFuerza = valor

    # getter para FuerzasSobreElPunto
    @property
    def fuerzasSobreElPunto(self):
        return self.__fuerzasSobreElPunto
    
    def distanciaACarga(self,cargaAEvaluar: Carga)-> tuple:
        """funcion que toma una carga como argumento y retorna la tupla ordenada de distancias con respecto a 
        la carga, si el valor es positivo el punto se encuentra a la inquierda y/o abajo de la carga evaluada"""

        distanciaACargaX = self.__cordenadaX-cargaAEvaluar.cordenadaX
        distanciaACargaY = self.__cordenadaY-cargaAEvaluar.CordenadaY
        return(distanciaACargaX,distanciaACargaY,round(sqrt(distanciaACargaX**2 + distanciaACargaY**2),3))
    
    def __calcularFuerzaEje(self, eje: str, cargaAEvaluar: Carga)->float:
        """Funcion que toma una carga, y calcula la fuerza ejercida sobre el punto actual, si el eje es diferente
        a 'x' o 'y' la funcion devolvera el modulo de la fuerza"""
        cordenadas = self.distanciaACarga(cargaAEvaluar)
        resultado: float = cargaAEvaluar.cantidadCarga *   Punto.__cargaDeprueba * Carga.constante / (cordenadas[2]**2)
        
        if eje == "x":
            resultado = resultado*(cordenadas[0]/cordenadas[2])
        elif eje == "y":
            resultado = resultado*(cordenadas[1]/cordenadas[2])
        
        resultado = round(resultado,3)
        return resultado
    
    def guardarFuerza(self,cargaAEvaluar: Carga):
        """funcion que guaeda en __fuerzasSobreElPunto las fuerzas sobre el punto"""
        fuerza = self.__calcularFuerzaEje("",cargaAEvaluar)
        fuerzaEnX = self.__calcularFuerzaEje("x",cargaAEvaluar)
        fuerzaEnY = self.__calcularFuerzaEje("y",cargaAEvaluar)

        self.__fuerzasSobreElPunto.append((fuerzaEnX, fuerzaEnY, fuerza))
        pass

    def sumaDefuerzasEje(self, eje: str = "x")->float:
        eje = eje.lower()
        resultado: float = 0
        if eje == "x":
            referencia = 0
        elif eje == "y":
            referencia = 1
        else:
            referencia = 2

        for fuerza in self.__fuerzasSobreElPunto:
            resultado += fuerza[referencia]
        return resultado
