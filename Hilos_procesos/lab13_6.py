#***************************************************************
"""Programa con hilos del modulo multiprocesisng"""
from multiprocessing import Process
import os
import math
import time
def calc():
    for i in range(0, 4000000):
        math.sqrt(i)
procesos = []
cpus = os.cpu_count()
print('Núcleos en tu CPU: ' + str(cpus))
for i in range(cpus):
    print('registrando el hilo %d' % i)
    procesos.append(Process(target = calc))
start = time.time()
for proceso in procesos:
    proceso.start()
for proceso in procesos:
    proceso.join()
end = time.time()
print('Se tardo: ' + str(end - start))
#***************************************************************
