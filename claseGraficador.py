import matplotlib.pyplot as plt
import numpy as np
from clasePunto import Punto

class Graficador:

    # Declaracion de variables

    def vector(self, puntoAGraficar: Punto, escala: float):

        plt.quiver(puntoAGraficar.cordenadaX, puntoAGraficar.CordenadaY, puntoAGraficar.fuerzasSobreElPunto[0][0],
        puntoAGraficar.fuerzasSobreElPunto[0][1], color=['r'], scale=escala,)

    def vectores(self, listaPuntos: 'list[Punto]', escala: float = 20, margenenes: float = 1):
        for punto in listaPuntos:
            self.vector(punto, escala)
        plt.margins(x=margenenes, y=margenenes)  # márgenes del 10% en x e y
        plt.show()    