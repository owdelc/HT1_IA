#se importan las funciones
from MazeGen import busquedaBFS
from discretizar import discretizacion
import matplotlib.pyplot as plt
from Djikstra import ALgoritmo_Djikstra, dibujar_camino
import cv2

#Funcion para manejar entradas de menu 
def numEnt():
    correcto = False
    num = 0
    while (correcto != True):
        try:
            num = int(input("Ingrese el numero de algoritmo deseado: "))
            correcto = True
        except ValueError:
            print("No ingreso un numero")
    return num

salir = False
opcion = 0

#Menu de opciones
while (salir != True):
  print("*** Bienvenido a Maze Solver ***")
  print("1. BFS")
  print("2. DFS")
  print("3. A-Star")

  opcion = numEnt()

  if opcion == 1:
    print('*** Algoritmo BFS ***\n')
    archivo = input("Ingrese el nombre del archivo: ")
    discretizacion(archivo)
    nuevo_archivo = "resultado_" + archivo
    busquedaBFS(nuevo_archivo)

   
  elif opcion == 2:
    print('*** Algoritmo DFS ***\n')
    #No se logro implementar

  elif opcion == 3:
    print('*** Algoritmo A-Star ***\n')
    
    archivo = input("Ingrese el nombre del archivo: ")    
    imagen = cv2.imread(archivo)
    resultado = ALgoritmo_Djikstra(imagen,(460,460),(500,80))
    dibujar_camino(imagen, resultado)
    plt.imshow(imagen)
    plt.show()
    
    

    

  elif opcion == 4:

    salir = True