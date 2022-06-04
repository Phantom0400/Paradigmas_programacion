#*********************************************************
#---------------------------------------------------------
# FUNCIÓN PURA x**2
#---------------------------------------------------------
def alcuadrado(x):
    return x*x
#---------------------------------------------------------
# FUNCIÓN PURA PARA x**3
#---------------------------------------------------------
def alcubo(x):
    return x*x*x
#---------------------------------------------------------
# Mapeo de una función pura
#---------------------------------------------------------
def mapeo(func, lista_numeros):
    resultado = []
    for i in lista_numeros:
        resultado.append(func(i))
    return resultado
cuadrados = mapeo(alcuadrado, [1, 2j, 2.2,10])
cubos = mapeo(alcubo, [1, 3j, 4.21 , 10])
print(cuadrados, cubos)
#---------------------------------------------------------
#FUNCIONES DENTRO DE FUNCIONES
#---------------------------------------------------------
def en_mayusculas(texto):
    return texto.upper()
def en_minusculas(texto):
    return texto.lower()
def saludar(func):
    saludo = func('Hola ¿qué tal?')
    print(saludo)
#---------------------------------------------------------
# Con cadenas de caracteres
#---------------------------------------------------------
saludar(en_mayusculas)
saludar(en_minusculas)
#---------------------------------------------------------
# Funciones abstractas dentro de otras funciones, su 
# resultado es otra funcion
#---------------------------------------------------------
def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo
division = divisor(3)
for i in range(1, 10):
    print(division(i))
#---------------------------------------------------------
# USO DE LA FUNCION 'map' EN UNA LISTA
# Lista de ciudades y su temperatura
#---------------------------------------------------------
temps = [('Berlín', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokyo', 27), ('Nueva York', 28), ('Pekín', 32), ('México Tenochtitlan', 32)]
C_a_F = lambda datos: (datos[0], (9/5)*datos[1] + 32)
print(list(map(C_a_F, temps)))
#*********************************************************
