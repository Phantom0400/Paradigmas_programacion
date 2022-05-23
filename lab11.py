#********************************************************
"""Octree"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import Axes3D
class Particula():
    def __init__(self, x:float, y:float, z:float):
        self.x = x
        self.y = y 
        self.z = z

class Nodo():
    def __init__(self, x0:float, y0:float, z0:float, w:float, h:float, d:float, particulas):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.ancho = w
        self.alto = h
        self.profundidad = d
        self.particulas = particulas
        self.hijos = []
    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto
    def get_profundidad(self):
        return self.profundidad
    def get_particulas(self):
        return self.particulas
def subdivision_recursiva(nodo:Nodo, k:int):
    if len(nodo.particulas) <= k:
        return None
    w_ = float(0.5*nodo.ancho)
    h_ = float(0.5*nodo.alto)
    d_ = float(0.5*nodo.profundidad)

    p = cuantas_contiene(nodo.x0, nodo.y0, nodo.z0, w_, h_, d_, nodo.particulas)
    nodo.x1 = Nodo(nodo.x0, nodo.z0, w_, h_, d_, p)
    subdivision_recursiva(nodo.x1, k)

    p = cuantas_contiene(nodo.x0, nodo.y0 + h_, nodo.z0, w_, h_, d_, nodo.particulas)
    nodo.x2 = Nodo(nodo.x0, nodo.y0 + h_, nodo.z0, w_, h_, d_, p)
    subdivision_recursiva(nodo.x2, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0, nodo.z0, w_, h_, d_, nodo.particulas)
    nodo.x3 = Nodo(nodo.x0 + w_, nodo.y0, nodo.z0, w_, h_, d_, p)
    subdivision_recursiva(nodo.x3, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0 + h_, nodo.z0, w_, h_, d_, nodo.particulas)
    nodo.x4 = Nodo(nodo.x0 + w_, nodo.y0 + h_, w_, h_, d_, p)
    subdivision_recursiva(nodo.x4, k)

    p = cuantas_contiene(nodo.x0, nodo.y0, nodo.z0 + d_, w_, h_, d_, nodo.particulas)
    nodo.x5 = Nodo(nodo.x0, nodo.y0, nodo.z0 + d_, w_, h_, d_, p)
    subdivision_recursiva(nodo.x5, k)

    p = cuantas_contiene(nodo.x0, nodo.y0 + h_, nodo.z0 + d_, w_, h_, d_, nodo.particulas)
    nodo.x6 = Nodo(nodo.x0, nodo.yo + h_, nodo.z0 + d_, w_, h_, d_, p)
    subdivision_recursiva(nodo.x6, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0, nodo.z0 + d_, w_, h_, d_, nodo.particulas)
    nodo.x7 = Nodo(nodo.x + w_, nodo.y0, nodo.z0 + d_, w_, h_, d_, nodo.particulas)
    subdivision_recursiva(nodo.x7, k)

    p = cuantas_contiene(nodo.x0 + w_, nodo.y0 + h_, nodo.z0 + d_, w_, h_, d_, nodo.particulas)
    nodo.x8 = Nodo(nodo.x0 + w_, nodo.y0 + h_, nodo.z0 + d_, w_, h_, d_, p)
    subdivision_recursiva(nodo.x8, k)

    nodo.hijos = [nodo.x1, nodo.x2, nodo.x3, nodo.x4, nodo.x5, nodo.x6, nodo.x7, nodo.x8]

def cuantas_contiene(x:float, y:float, z:float, w:float, h:float, d:float, particulas):
    pts = []
    for particula in particulas:
        if particula.x >= x and particulas.x <= x + w and partiucla.y >= y and particula.y <= y + h and particula.z >= z and particula.z <= z + d:
            pts.append(particula)
    return pts

def encontrar_hijos(nodo):
    if not nodo.hijos:
        return [nodo]
    else:
        hijos = []
        for hijo in nodo.hijos:
            hijos += (encontrar_hijos(hijo))
    return hijos

class Octree():
    def __init__(self, k:int, n:int):
        self.umbral = k
        self.particulas = [Particula(random.uniform(0, 10), random(0, 10), random.unifom(0, 10)) for x in range(n)]
        self.root = Nodo(0, 0, 0, 10, 10, 10, self.particulas)

    def add_particula(self, x:float, y:float, z:float):
        self.particulas.append(Particula(x, y, z))
    
    def get_particulas(self):
        return self.particulas

    def subdividir(self):
        subdivision_recursiva(self.root, self.umbral)

    def visualizacion(self):
        fig = plt.figure(figsize = (4, 4))
        ax = fig.add_subplot(111, projection = '3d')
        x = [particula.x for particula in self.particulas]
        y = [particula.y for particula in self.particulas]
        z = [particula.z for particula in self.particulas]
        ax.scatter(x, y, z, 'ro')
        plt.show()
        return None

octree = Octree(1, 100)
octree.subdividir()
octree.visualizacion()
#********************************************************
