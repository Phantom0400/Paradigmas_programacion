#***************************************************************
""" genrador con muchos procesadores corriendo en paralelo """
from multiprocessing import Process
import random
import os
N:int = 10
def generador(N:float) -> None:
    semilla:float = random.uniform(-1, 1)
    print('La semilla es: ' + str(semilla))
    random.seed(semilla)
    for i in range(N):
        x:float = random.uniform(-1, 1)
        y:float = random.uniform(-1, 1)
        print('x = ' + str(x), '\ty = ' + str(y))
procesos = []
cpus:int = os.cpu_count()
print('Porcesadores = ' +str(cpus))
for i in range(cpus):
    procesos.append(Process(target = generador, args = (N,)))
#Comienza todos los procesos en paralelo
for proceso in procesos:
    proceso.start()
# Espera a que los procesos terminen
for proceso in procesos:
    proceso.join()

#***************************************************************
