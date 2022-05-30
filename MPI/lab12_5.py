#*************************************************************
""" Comando: mpiexec -n 4 python3 lab14_5.py"""
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
# Arreglo de un solo elemento
randNum = np.zeros(1)
if rank == 1:
    randNum = np.random.random_sample(1)
    print('Proceso ' + str(rank) + ' genró ' + str(randNum[0]))
    comm.Isend(randNum, dest = 0)
    req = comm.Irecv(randNum, source = 0)
    req.Wait()
    print('Proceso ' + str(rank) + ' recibió el número ' + str(randNum[0])) 
if rank == 0:
    randNum = np.random.random_sample(1)
    print('Proceso ' + str(rank) + ' generó ' + str(randNum[0]))
    comm.Isend(randNum, dest = 1)
    req = comm.Irecv(randNum, source = 1)
    req.Wait()
    print('Proceso ' + str(rank) + ' recibió el número ' + str(randNum[0]))
#*************************************************************
