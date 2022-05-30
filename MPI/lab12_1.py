#***********************************************************
# Linea de comando: mpiexec -n 4 python3 lab12_1.py
from mpi4py import MPI
#Objeto comunicador
comm = MPI.COMM_WORLD
# Cuantos somos 
size = comm.Get_size()
# Quien es
rank = comm.Get_rank()
# Si soy el cero hago esto:
if rank == 0:
    print('Yo soy el proceso 0')
elif rank == 1: # Si soy el 1 hago esto
    print('Yo soy el proceso 1')
else: # Si no soy ninguno de los anteriores
    print('Yo no soy ninguno de los anteriores')
print('Reportandose desde el proceso ' + str(rank) + ' de ' + str(size))
#***********************************************************
