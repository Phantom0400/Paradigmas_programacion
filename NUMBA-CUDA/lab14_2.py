#**************************************************************
""" Ejemplo de comuncacion bloqueada al mismo valor compartido"""
from multiprocessing import Process, Value, Lock
import time
def sumale100(numero, candado):
    for i in range(100):
        time.sleep(0.01)
        # Poner el candado
        candado.acquire()
        # hacer la operacion
        numero.value += 1
        # Quitar el candado
        candado.release()
if __name__ == "__main__":
    # Candado para evitar que los procesos se empalmen 
    candado = Lock()
    """Número comun a los procesos, i de entero, comienza siendo 0
    Value es un objeto compartido"""
    numero_compartido = Value('i', 0)
    print('Al principio value = ' + str(numero_compartido.value))
    p1 = Process(target = sumale100, args = (numero_compartido, candado))
    p2 = Process(target = sumale100, args = (numero_compartido, candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('Al final value = ' + str(numero_compartido.value))
#**************************************************************
