import matplotlib.pyplot as plt
import numpy as np
from clasePunto import Punto

class Graficador:

    # Declaracion de variables

    def vector(self, puntoAGraficar: Punto):
        plt.quiver(puntoAGraficar.cordenadaX, puntoAGraficar.CordenadaY, puntoAGraficar.fuerzasSobreElPunto[0],
        puntoAGraficar.fuerzasSobreElPunto[1], color=['r'], scale=21)
        plt.show()
