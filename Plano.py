from clasePunto import Punto
from claseCarga import Carga
import matplotlib.pyplot as plt
import numpy as np
from claseGraficador import Graficador
from creadorCarpetas import creadorCarpetas

import matplotlib as mpl
class plano:

    # Declaracion de variables
    __espaciado: float
    __matrizPuntos: list
    __cargas: list
    __graf: Graficador

    def __init__(self, cargas: list, espaciado: float=1) -> None:
        self.__espaciado = espaciado
        self.__cargas = cargas
        self.__graf = Graficador()

    def __mayorYMenorDistanciaEje(self, eje: str ="x") -> tuple:
        """mira todas las cargas y devuelve la cordenada menor y mayor en el eje especificado, por defecto el eje
        esta en 'x' """
        minimo: float = None
        maximo: float = None
        valor: float = 0

        eje = eje.lower()
        
        for cargaAEvaluar in self.__cargas:
            if eje == "x":
                valor = cargaAEvaluar.cordenadaX
            elif eje == "y":
                valor = cargaAEvaluar.CordenadaY
            
            if maximo == None:
                maximo = valor
                minimo = valor
            else:
                if maximo < max((valor,maximo)):
                    maximo = valor
                if minimo > min((valor, minimo)):
                    minimo = valor
        return (minimo, maximo)
    
    def __crearMatriz(self, porcentaje: float = 10) ->list:
        """usando un porcentaje que por defecto es 10 crea, una lista de punntos que rodean a las cargas por un margen
        definido en base al porcentaje dado"""

        matrizResultado: 'list[Punto]' =[]

        distanciasEnX = self.__mayorYMenorDistanciaEje()
        distanciasEnY = self.__mayorYMenorDistanciaEje("y")
        refernciaParaMargenX = max(abs(distanciasEnX[0]), abs(distanciasEnX[1]))
        refernciaParaMargenY = max(abs(distanciasEnY[0]), abs(distanciasEnY[1]))

        margenX = refernciaParaMargenX*porcentaje/100
        margenY = refernciaParaMargenY*porcentaje/100
        
        rangoEnX =np.arange(distanciasEnX[0]-margenX, distanciasEnX[1]+margenX,self.__espaciado)
        rangoEnY =np.arange(distanciasEnY[0]-margenY, distanciasEnY[1]+margenX,self.__espaciado)


        for cordenadaX in rangoEnX:
            
            for cordenadaY in rangoEnY:
                puntoActual = Punto(cordenadaX,cordenadaY)
                for cargaEvaluada in self.__cargas:
                    puntoActual.guardarFuerza(cargaEvaluada)
                matrizResultado.append(puntoActual)

        return (matrizResultado)
    
    def graficarPuntos(self, norma: float, escala: float = 20, margenes: float = 1,
                        porFuera: float = 6):
        
        self.__matrizPuntos = self.__crearMatriz(porFuera*100)
        #print(self.__matrizPuntos)
        self.__graf.vectores(self.__matrizPuntos, norma, escala, margenes)
        pass

    def guardarDatosEimagen(self, nombre:str):
        carp = creadorCarpetas()
        ruta = carp.guardarDatos(self.__matrizPuntos, nombre)
        self.__graf.guardarImagen(ruta)
