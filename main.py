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

while (salir != True):
  print("*** Bienvenido a Maze Solver ***")
  print("1. BFS")
  print("2. DFS")
  print("3. A-Star")

  opcion = numEnt()

  if opcion == 1:
    print('*** Algoritmo BFS ***\n')
    

   
  elif opcion == 2:
    print('*** Algoritmo DFS ***\n')
    1

  elif opcion == 3:
    print('*** Algoritmo A-Star ***\n')

  elif opcion == 4:

    salir = True