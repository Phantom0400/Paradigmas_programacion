#**************************************************************
""" mpiexec -n 4 python3 lab13_1.py
Emisión de arreglos de numpy"""
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
# Tamaño del arreglo
n = 10
if rank == 0:
    # Arreglo de enteros del 1 al n - 1
    data = np.arange(n, dtype = 'i')
else:
    # Arreglo de enteros vacio de tamaño n
    data = np.empty(n , dtype = 'i')
""" Broadcast pero que indica el tipo de dato
Optmizando para comunicacion rápida"""
comm.Bcast([data, MPI.INT], root = 0)
# Asegurarse que todo salio bien 
for i in range(n):
    assert data[i] == i
print(data)
#**************************************************************
