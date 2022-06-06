#***************************************************************
"""mpiexec -n 4 python3 lab13_4.py
la función mapeo"""
from mpi4py import MPI
import math
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
n = 40
x = range(n)
m = int(math.ceil(float(len(x)) / size))
x_chunk = list(x [rank*m: (rank + 1)*m])
r_chunk = list(map(math.sqrt, x_chunk))
# Una sola lista de datos
r = comm.allreduce(r_chunk)
# Una matriz con todos los datos al proceso 0
rr = comm.allgather(r_chunk)
#Una matriz con todos los datos al proceso 1
rrr = comm.gather(r_chunk, root = 1)
if rank == 0:
    print('del proceso 0\n', r)
    print(rr)
    print(rrr)
if rank == 1:
    print('del proceso 1\n', rrr)
#***************************************************************
