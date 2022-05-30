#***************************************************************
""" comando: mpiexec -n 4 python3 lab12_2.py"""
from mpi4py import MPI
class Mensaje:
    def __init__(self, rank):
        self.x = [i for i in range(rank*10)]
        self.p = 'vengo del proceso ' + str(rank)
# Programa principal
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)
    src = rank - 1 if rank != 0 else size - 1
    dst = rank + 1 if rank != size - 1 else 0
    # Envio no Bloquente
    comm.isend(s, dest = dst)
    # Receptor no bloquente con espera
    # req : request (peticion de espera)
    req = comm.irecv(source = src)
    a = req.wait()
    print('Soy el proceso ' + str(rank) + ', el resultado es ' + str(len(a.x)), a.p)
#***************************************************************
