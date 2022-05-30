#***************************************************************
""" COmando: mpiexec -n 4 python3 lab12_6.py"""
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
randNum = np.zeros(1)
if rank == 1:
    dst = 0
    src = 0
if rank == 0:
    dst = 1
    src = 1
randNum = np.random.random_sample(1)
print('Proceso ' + str(rank) + ' generó ' +str(randNum[0]))
comm.Isend(randNum, dest = dst)
req = comm.Irecv(randNum, source = src)
req.Wait()
print('Proceso ' + str(rank) + ' recibió el número ' + str(randNum[0])) 
#***************************************************************
