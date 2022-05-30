#***************************************************************
"""Comando para ejecutar: mpiexec -n 4 python3 lab12_2.py"""
from mpi4py import MPI
# Objeto mensaje
class Mensaje:
    def __init__(self, rank):
        self.x = range(rank*10) #Lista de numeros
        self.p = 'vengo del proceso ' + str(rank) # identificador
# Programa principal
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)
    fuente = rank - 1 if rank != 0 else size - 1
    destino = rank + 1 if rank != size - 1 else 0
    """send y recv son operaciones bloqueantes y generan que el 
    código se atore esperando que alguien reciba el mensaje 
    esto se resuelve envienaod con los pares y reciviendo con 
    los impres"""
    # Si soy par
    if rank % 2 == 0:
        # Enviar s al destinatario
        comm.send(s, dest = destino)
        # Recibir de source y lo pone en m
        m = comm.recv(source = fuente)
    else: # Si no soy par
        # Recibir primero y luego mandar mensaje despues
        m = comm.recv(source = fuente)
        comm.send(s, dest = destino)
    print('Soy el proceso ' + str(rank) + ' el resultado es ' + str(len(m.x)) + ', ' + str(m.p))
#***************************************************************
