from PIL import Image
import matplotlib.pyplot as plt

def discretizacion(imagen):
  
    #se lee la imagen 
    ima=Image.open(imagen)

    #se obtiene el tamaño de la imagen
    height, width = ima.size
    
    #se calcula el numero de pixeles de la imagen
    i_size = (int(width/2), int(height/2))
   
    #se crea una imagen de la mitad de la imagen original
    small_ima=ima.resize(i_size,Image.BILINEAR)

    #se guarda la imagen con nuevo tamaño en una variable
    resultado = small_ima.resize(ima.size, Image.NEAREST)

    #Se guarda la imagen en un archivo con nombre nurvo
    filename="resultado_" + imagen 
    resultado.save(filename)

    print("*** Discretizacion exitosa ***")



