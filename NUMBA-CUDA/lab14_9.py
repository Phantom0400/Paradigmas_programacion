#***************************************************************
""" Trabajos con el GPU
montecarlo con NUMBA-CUDA"""
from __future__ import print_function, absolute_import
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states
from numba.cuda.random import xoroshiro128p_uniform_float64
import numpy as np
import random as ran
@cuda.jit
def calcularpi_kernel(rng_states, iteraciones, out):
    """ Encontrar el valor maximo en value y guardarlo
en result[0] """
    ii = cuda.grid(1)
    #Calcular pi dibujando puntos (x, y) al azar y encontrarlo
    # la fraccion de ellos que cae dentro del circulo unitario
    cae_dentro = 0 
    for i in range(iteraciones):
        x = xoroshiro128p_uniform_float64(rng_states, ii)
        y = xoroshiro128p_uniform_float64(rng_states, ii)
        if x**2 + y**2 <= 1.0:
            cae_dentro += 1
    out[ii] = 4.0 * cae_dentro / iteraciones
""" Procesos de cuda """
hilosporbloque = 64
bloques = 24
# Arreglos necesarios
seed1 = ran.uniform(-1, 1)
seed2 = ran.seed(seed1)
seed = ran.randint(0, 1000)
rng_states = create_xoroshiro128p_states(hilosporbloque*bloques, seed)
out = np.zeros(hilosporbloque*bloques, dtype = np.float64)
# Llamar a la funcion
calcularpi_kernel[bloques, hilosporbloque](rng_states, 10000, out)
print('Pi: ', out.mean())
#***************************************************************