from clasePunto import Punto
import os
import csv
import numpy as np


class creadorCarpetas:

    def __crearCarpeta(self, nombreCarpeta: str):
        os.makedirs(nombreCarpeta, exist_ok=True)
    
    def __crearCSV(self, matriz: 'list[Punto]', rutaArchivo: str):
        datos = [["Cordenada X", "Cordenada Y"]]
        puntoActual: int = 1
        for puntoEvaluado in matriz:
            if len(datos[0]) == 2:
                for i in range(0,len(puntoEvaluado.fuerzasSobreElPunto)):
                    datos[0].append("fuerza X "+str(i+1))
                    datos[0].append("fuerza Y "+str(i+1))
                    datos[0].append("fuerza neta "+str(i+1))
                datos[0].append("fuerza total X")
                datos[0].append("fuerza total Y")
                datos[0].append("fuerza neta total")
                    
            datos.append([puntoEvaluado.cordenadaX, puntoEvaluado.CordenadaY])
        
            for fuerza in puntoEvaluado.fuerzasSobreElPunto:
                datos[puntoActual].append(fuerza[0])
                datos[puntoActual].append(fuerza[1])
                datos[puntoActual].append(fuerza[2])
            
            fuerzaXTot = puntoEvaluado.sumaDefuerzasEje()
            fuerzaYTot = puntoEvaluado.sumaDefuerzasEje("y")
            
            datos[puntoActual].append(fuerzaXTot)
            datos[puntoActual].append(fuerzaYTot)
            datos[puntoActual].append(round(np.sqrt(fuerzaXTot**2+fuerzaYTot**2),3))
            puntoActual += 1

        with open(rutaArchivo, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(datos)
    
    def guardarDatos(self, matriz: 'list[Punto]', nombre: str)->str:
        self.__crearCarpeta(nombre)
        ruta = os.path.join(nombre,"datos.csv")
        self.__crearCSV(matriz, ruta)
        return os.path.join(nombre,nombre+".png")