#***************************************************************
"""calculo de polinomios en paralelo con multiprocessing y numpy"""
import multiprocessing as mp
import numpy as np
import time
def mi_funcion(i, param1, param2, param3):
    #Cálcula un polinomio
    result = param**2 + param2 + pram3
    #Se toma 2 segundos 
    time.sleep(2)
    return (i, result)
def get_result(result):
    # se inscribn en la lista global
    # (mal estilo de programacion
    global results
    results.append(result)
""" Programa Principal """
if __name__ == "__main__":
    # Matriz de 10x3 números la azar
    params = np.random.random((10,3))*100
    results = []
    ts = time.time()
    #un grupo de procesos
    pool = mp.Pool(mp.cpu_count())
    #loop de primera dimension del arreglo 
    for i in range(0, params.shape[0]):
        # Correr asincronamente mi_funcion con argumentos args 
        # y al termnar recoge el resultado son get_result
        pool.apply_async(mi_funcion, args = (i, params[i, 0], params[i, 1], params[i, 2]), callback = get_result)
    # Cerrar el grupo
    pool.close()
    # Esperar que termine el grupo
    pool.join()
    print('Tiempo en paralelo: ' + str(time.time() - ts))
    print(results)
#***************************************************************
