#*********************************************
"""Ejemplo de función zip junto con 
filtración de informacion 
notacion de lista en una sola linea:
    [var for var in 'objeto' if 'condición'"""
mi_lista = [1, 2, 3]
tu_lista = (10, 20, 300)
su_lista = (40, 50, 100)
def multiplicar_po2(elemento):
    return elemento*2
def solo_impar(elemento):
    return elemento % 2 != 0
# Lista de pares de datos de las dos listas
print(list(zip(mi_lista, tu_lista, su_lista)))
una_lista = ['a', 'b', 'c', 'b' ,'d', 'm', 'n', 'n']
duplicados = set([x for x in una_lista if una_lista.count(x) > 1])
print(duplicados)
#Expresión genradora
cuadrados = (x*x for x in range(5))
print('impresión de función generadora')
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print(next(cuadrados))
print('fin de impresión')
#Pasar una función generadora
import math as mt
print('suma de cuadrados: ' + str(sum(x*x for x in range(5))))
#Lista de comprhesión pasada como función
numeros_pares = [x for x in range(21) if x%2 == 0]
print('pasar la lista: ' + str([x for x in range(21) if x%2 == 0]))
print('Solo la lista: ' + str(numeros_pares))
#*********************************************
