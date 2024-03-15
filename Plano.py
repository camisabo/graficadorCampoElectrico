from clasePunto import Punto
from claseCarga import Carga
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.scatter([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()
import matplotlib as mpl
class plano:

    # Declaracion de variables
    __espaciado: float
    __matrizPuntos: list
    __cargas: 'list[Carga]'

    def __init__(self, cargas: list, espaciado: float=1) -> None:
        self.__espaciado = espaciado
        self.__cargas = cargas

    def __mayorYMenorDistanciaEje(self, eje: str ="x") -> tuple:
        minimo: float = None
        maximo: float = none
        valor: float = 0

        eje = eje.lower()
        
        for carga in self.__cargas:
            if eje == "x":
                valor = carga.cordenadaX
            elif eje == "y":
                valor = carga.CordenadaY
            
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
        matrizResultado: 'list[Punto]'

        distanciasEnX = self.__mayorYMenorDistanciaEje()
        distanciasEnY = self.__mayorYMenorDistanciaEje("y")
        refernciaParaMargenX = max(abs(distanciasEnX[0]), abs(distanciasEnX[1]))
        refernciaParaMargenY = max(abs(distanciasEnY[0]), abs(distanciasEnY[1]))

        margenX = refernciaParaMargenX*porcentaje/100
        margenY = refernciaParaMargenY*porcentaje/100
        

        rangoEnX =range((distanciasEnX[0]-margenX, distanciasEnX[1]+margenX,self.__espaciado))
        rangoEnY =range((distanciasEnY[0]-margenY, distanciasEnY[1]+margenX,self.__espaciado))

        for cordenadaX in rangoEnX:
            for cordenadaY in rangoEnY:
                puntoActual = Punto(cordenadaX,cordenadaY)
                matrizResultado.append(puntoActual)
        
        