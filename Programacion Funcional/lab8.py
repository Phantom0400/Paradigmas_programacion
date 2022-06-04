#**********************************************************
#----------------------------------------------------------
#Programación Funcional
# Recursividad y memoización
# Con herramientas para la memoización
#----------------------------------------------------------
from functools import lru_cache
def fibonacci_lento(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)
print('Aqui empieza fibonacci_lento')
for i in range(1, 36):
    print(str(i) + ':', fibonacci_lento(i))
print('Aquí termina fibonacci_lento')
#----------------------------------------------------------
# OPTIMIZACION: Uso de conjuntos para guardar valores
# CONJUNTO DE FIBONACCIs
#----------------------------------------------------------
fibonaccis = {}
def fibonacci_2(n):
    #------------------------------------------------------
    #Revisa si ya existe y retorna el valor
    #------------------------------------------------------
    if n in fibonaccis:
        return fibonaccis[n]
    if n == 1:
        valor = 1
    elif n == 2:
        valor = 1
    elif n > 2:
        valor = fibonacci_2(n - 1) + fibonacci_2(n - 2)
    #------------------------------------------------------
    # Guarda el valor
    #------------------------------------------------------
    fibonaccis[n] = valor
    return valor
print('Aquí empieza fibonacci con memoizacion')
for i in range(1, 10001):
    print(str(i) + ':', fibonacci_2(i))
print('Aquí termina fibonacci con memoización')
#----------------------------------------------------------
# Uso de decoradores para la mamoización 
# maxsize: cuantos de los anteriores quieres que guarde
#----------------------------------------------------------
@lru_cache(maxsize = 3)
def fibonacci_cache(n):
    if type(n) != int:
        raise TypeError('n debe ser entero positivo')
    if n < 1:
        raise ValueError('n debe ser entero postivo')
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_cache(n - 1) + fibonacci_cache(n - 2)
print('fibonacci decorador init')
for i in range(1, 10001):
    print(str(i) + ':', fibonacci_cache(i))
print('fibonacci decorador end')
#**********************************************************
