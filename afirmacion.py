#********************************************************
"""la palabra reservada 'assert' nos permite ingresar 
captacion de errores en una función de python con condiciones
especificas, donde hay un mensaje de error en caso de no
cumplir dada condición"""
def aceleracion(d:float = 0, t:float = 1) -> float:
    assert t>= 0, "Siempre los tiempos son mayor o igual a cero"                        
    return d/(t**2)
a = aceleracion(d = 10, t = 2)
print('aceleracion(d = 10 [m], 2 [s]) = '+ str(a) + '[m/s²]')
a_2 = aceleracion(d = 5, t =-1)
print(a_2)
#********************************************************
