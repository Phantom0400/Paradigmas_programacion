#**************************************************************
""" mpiexec -n 4 python3 lab13_3.py
colectar con numpy"""
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = 10
""" Arreglo de ceros de tamño n
sumado un escalar en cada entrada"""
sendarray = np.zeros(n, dtype = 'i') + rank
recvarray = None
if rank == 0:
    """ Matriz de tamaño de procesos * n
    dtype es el tipo de dato 'i' es entero"""
    recvarray = np.empty([size, n], dtype = 'i')
""" Gather es rápido para numpy
enviar el proceso a root"""
comm.Gather(sendarray, recvarray, root = 0)
if rank == 0:
    for i in range(size):
        """ Revisa fila or fila la matriz : los elementos de 
        esa dimansión allclase es un método de numpy que compara 
        todos los elementos """
        assert np.allclose(recvarray[i,:], i)
print(recvarray)
#**************************************************************
