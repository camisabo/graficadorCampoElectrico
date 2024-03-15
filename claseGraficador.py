import matplotlib.pyplot as plt
import numpy as np
from clasePunto import Punto

class Graficador:

    # Declaracion de variables

    def vector(self, puntoAGraficar: Punto, escala: float):
        
        x = puntoAGraficar.fuerzasSobreElPunto[0][0]-puntoAGraficar.cordenadaX
        y = puntoAGraficar.fuerzasSobreElPunto[0][1]-puntoAGraficar.CordenadaY
        normalizador = np.sqrt(x**2+y**2)

        # Normalizar el vector
        x_norm = x / normalizador
        y_norm = y / normalizador

        plt.quiver(puntoAGraficar.cordenadaX, puntoAGraficar.CordenadaY, x_norm, y_norm, color=['r'], scale=escala)

    def vectores(self, listaPuntos: 'list[Punto]', escala: float = 20, margenenes: float = 1):
        for punto in listaPuntos:
            self.vector(punto, escala)
        plt.margins(x=margenenes, y=margenenes)  # márgenes del 10% en x e y
        plt.show()    