#***************************************************************
""" Ejemplo con numba """
from numba import jit
import numpy
import time
@jit(nopython = True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t
def lento(a):
    t = 0.0
    #Para cada renglon
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a + t
x = numpy.arange(10000).reshape(100, 100)
#La primera llamada incluye el tiempo de compilacion
start = time.time()
rapido(x)
end = time.time()
print('Tiempo incluyendo compilación: %s' % (end - start))
# La segunda llamda es para obtener el tiempo de ejecucion
start = time.time()
rapido(x)
end = time.time()
print('Tiempo usando numba: %s' % (end - start))
# La segunda llamda es para obtener el tiempo de ejecucion
start = time.time()
lento(x)
end = time.time()
print('Tiempo usando python vanilla: %s' % (end - start))
#***************************************************************
