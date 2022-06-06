#***************************************************************
"""MPI avanzado
Broadcast con MPI 
distribucion de datos
mpiexec -n 4 python3 lab3.py"""
from mpi4py import MPI
comm = MPI.COMM_WORLD #Objeto comunicador
rank = comm.Get_rank() #Quién Soy
""" El proceso 0 tiene todos los datos y los demas no """
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3], 
            'key2' : ('abc' , 'xyz')}
else:
    data = None
"""Envia diccionario a todos los procesos desde root """
data = comm.bcast(data, root = 0)
print(data)
#***************************************************************
