#***************************************************************
""" Comando de execusión: mpiexec -n 4 python3 lab12_7.py"""
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
# Se indica el tipo de dato explicitamente 
if rank == 0:
    # Arreglo de enteros del 0 al 9 
    data = np.arange(10, dtype = 'i')
    # Envio bloqueante especifiando el tipo de dato
    comm.Send([data, MPI.INT], dest = 1, tag = 77)
elif rank == 1:
    data = np.empty(10, dtype = 'i')
    comm.Recv([data, MPI.INT], source = 0, tag = 77)
    print(str(data))
""" También se puede sin decir el tipo de dato pero deben 
coincidir el tipo de dato en los extremos del mensaje"""
if rank == 0:
    data = np.arange(10, dtype = np.float64)
    comm.Send(data, dest = 1, tag = 13)
elif rank == 1:
    data = np.empty(10, dtype = np.float64)
    comm.Recv(data, source = 0, tag =13)
    print(data)
#***************************************************************
