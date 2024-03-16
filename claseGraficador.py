import matplotlib.pyplot as plt
import numpy as np
from clasePunto import Punto

class Graficador:

    def __normasMaxMin(self, normas:'list[float]')->tuple:
        maximo = max(normas)
        minimo = min(normas)
        return((maximo,minimo))

    def __norma(self,puntoAGraficar: Punto)->float:
        x = puntoAGraficar.sumaDefuerzasEje()-puntoAGraficar.cordenadaX
        y = puntoAGraficar.sumaDefuerzasEje("y")-puntoAGraficar.CordenadaY
        normalizador = round(np.sqrt(x**2+y**2),3)
        return normalizador

    def vector(self, puntoAGraficar: Punto, norma: float, normas: 'list[float]', escala: float):
        x = puntoAGraficar.sumaDefuerzasEje()-puntoAGraficar.cordenadaX
        y = puntoAGraficar.sumaDefuerzasEje("y")-puntoAGraficar.CordenadaY
        normalizador = self.__norma(puntoAGraficar)
        multiplicador = ((normalizador-normas[1])*100/(normas[0]-normas[1]))*norma/normalizador #regal de 3 con origen el la norma minima y normalizada con el normalizador
        
        rojo = ((normalizador - normas[1]) / (normas[0] - normas[1]))**(1/5)
        verde = abs(1-rojo)

        colorAplicado = (rojo, verde, 0.2)

        #print(multiplicador)

        # Normalizar el vector
        x_norm = x / normalizador * multiplicador
        y_norm = y / normalizador * multiplicador

        plt.quiver(puntoAGraficar.cordenadaX, puntoAGraficar.CordenadaY, x_norm, y_norm,
                    color=colorAplicado, scale=escala, linewidth=0.5)

    def vectores(self, listaPuntos: 'list[Punto]', norma: float, escala: float = 20,
                  margenenes: float = 1):
        
        normas = list(map(self.__norma, listaPuntos))
        normas = self.__normasMaxMin(normas)
        print(normas)
        for punto in listaPuntos:
            self.vector(punto, norma, normas, escala)
        plt.margins(x=margenenes, y=margenenes)  # márgenes del 10% en x e y
        plt.show()    