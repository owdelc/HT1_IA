"""

Inspirado en el codigo de: https://github.com/maxwellreynolds/Maze

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt


#Clase de vectores 
class Vertex:
    def __init__(self,x_coord,y_coord):
        self.x=x_coord
        self.y=y_coord
        self.d=float('inf') #distance from source
        self.parent_x=None
        self.parent_y=None
        self.processed=False
        self.index_in_queue=None

#Obtencion de ubicaciones adyacentes
def obtencion_adyacentes(mat,r,c):
    shape=mat.shape
    neighbors=[]
    
    if r > 0 and not mat[r-1][c].processed:
         neighbors.append(mat[r-1][c])
    if r < shape[0] - 1 and not mat[r+1][c].processed:
            neighbors.append(mat[r+1][c])
    if c > 0 and not mat[r][c-1].processed:
        neighbors.append(mat[r][c-1])
    if c < shape[1] - 1 and not mat[r][c+1].processed:
            neighbors.append(mat[r][c+1])
    return neighbors


def bubble_up(cola, indice):
    if indice <= 0:
        return cola
    p_indice=(indice-1)//2
    if cola[indice].d < cola[p_indice].d:
            cola[indice], cola[p_indice]=cola[p_indice], cola[indice]
            cola[indice].indice_in_cola=indice
            cola[p_indice].indice_in_cola=p_indice
            cola = bubble_up(cola, p_indice)
    return cola
    
def bubble_down(cola, indice):
    length=len(cola)
    lc_indice=2*indice+1
    rc_indice=lc_indice+1
    if lc_indice >= length:
        return cola
    if lc_indice < length and rc_indice >= length:
        if cola[indice].d > cola[lc_indice].d:
            cola[indice], cola[lc_indice]=cola[lc_indice], cola[indice]
            cola[indice].indice_in_cola=indice
            cola[lc_indice].indice_in_cola=lc_indice
            cola = bubble_down(cola, lc_indice)
    else:
        small = lc_indice
        if cola[lc_indice].d > cola[rc_indice].d:
            small = rc_indice
        if cola[small].d < cola[indice].d:
            cola[indice],cola[small]=cola[small],cola[indice]
            cola[indice].index_in_cola=indice
            cola[small].index_in_cola=small
            cola = bubble_down(cola, small)
    return cola

#Se obtiene la distancia
def obtener_distancia(img,u,v):
    return 0.1 + (float(img[v][0])-float(img[u][0]))**2+(float(img[v][1])-float(img[u][1]))**2+(float(img[v][2])-float(img[u][2]))**2

#Se dibuja el camino en la imagen
def dibujar_camino(img,path, thickness=2):
    x0,y0=path[0]
    for vertex in path[1:]:
        x1,y1=vertex
        cv2.line(img,(x0,y0),(x1,y1),(0,0,255),thickness)
        x0,y0=vertex

#Ejecucion de A-Star (Djikstra)
def ALgoritmo_Djikstra(img,src,dst):
    pq=[] 
    source_x=src[0]
    source_y=src[1]
    dest_x=dst[0]
    dest_y=dst[1]
    imagerows,imagecols=img.shape[0],img.shape[1]
    matrix = np.full((imagerows, imagecols), None) 
    for r in range(imagerows):
        for c in range(imagecols):
            matrix[r][c]=Vertex(c,r)
            matrix[r][c].index_in_queue=len(pq)
            pq.append(matrix[r][c])
    matrix[source_y][source_x].d=0
    pq=bubble_up(pq, matrix[source_y][source_x].index_in_queue)
    while len(pq) > 0:
        u=pq[0]
        u.processed=True
        pq[0]=pq[-1]
        pq[0].index_in_queue=0
        pq.pop()
        pq=bubble_down(pq,0)
        neighbors = obtencion_adyacentes(matrix,u.y,u.x)
        for v in neighbors:
            dist=obtener_distancia(img,(u.y,u.x),(v.y,v.x))
            if u.d + dist < v.d:
                v.d = u.d+dist
                v.parent_x=u.x
                v.parent_y=u.y
                idx=v.index_in_queue
                pq=bubble_down(pq,idx)
                pq=bubble_up(pq,idx)
                          
    path=[]
    iter_v=matrix[dest_y][dest_x]
    path.append((dest_x,dest_y))
    while(iter_v.y!=source_y or iter_v.x!=source_x):
        path.append((iter_v.x,iter_v.y))
        iter_v=matrix[iter_v.parent_y][iter_v.parent_x]

    path.append((source_x,source_y))
    return path
