#********************************************************
"""la palabra reservada 'assert' nos permite ingresar 
captacion de errores en una función de python con condiciones
especificas, donde hay un mensaje de error en caso de no
cumplir dada condición"""
def aceleracion(d:float = 0, t:float = 0) -> float:
    assert t < 0, 'No existen tiempos negativos'
    return d/(t**2)
a = aceleracion(d = 10, t = 2)
print(a)
a_2 = aceleracion(d = 5, t =-1)
#********************************************************
