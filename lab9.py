#***************************************************
"""Funcion Generadora """
def migenerador():
    print('Primero')
    yield 10 # Palabra reservada yield como algo a retener
    print('Segundo')
    yield 20
    print('tercero')
    yield 30
gen = migenerador() #Encapsulamiento de una función
val1 = next(gen)
"""Itera valores por iteración es decir, por ejecucion
pasa al siguiente valor"""
print(val1)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)
#***************************************************
