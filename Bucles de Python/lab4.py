#***************************************************************
#---------------------------------------------------------------
#3er laboratorio de Paradigmas de programacion
#Por Ortiz Ortiz Bosco
#Aquí inician los ejemlos de bucles
#---------------------------------------------------------------
precio = int(input("Dame un precio "))
#---------------------------------------------------------------
#Condicional si
#---------------------------------------------------------------
if precio < 50:
    print("El precio es menor que 50")
#SI no pasa esto pasa lo otro
elif precio > 50:
    print("El precio es mayor a 50")
#De no cumplirse ninguna de las anteriores 
else:
    print("El precio es 50")
cantidad = int(input("Dame una cantidad "))
total = precio*cantidad
#---------------------------------------------------------------
#Condicionales anidados
#---------------------------------------------------------------
if total > 100:
    if total > 500:
        print("Total es mayor a 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 y mayor a 400")
        elif total < 500 and total > 300:
            print("Total es menora a 500 y mayor a 300")
        else:
            print("Total entre 100 y 300")
#---------------------------------------------------------------
#Condicional de igualdad es '=='
#---------------------------------------------------------------
elif total == 100:
    print("Total es 100")
else:
    print("total es menor que 100")
#---------------------------------------------------------------
#Bucle 'MIENTRAS' se sigue siempre y cuando la condicion sea verdadera
#---------------------------------------------------------------
num = 0
while num < 5:
    num = num + 1
    print('num = ', num)

print('Aqui inicia un nucle con break')
num = 0
while num < 5:
    num += 1 # num += 1 es equivalente a num = num + 1
    print('num = ', num)
    if num == 3: #Condicion para salir del bucle
        break  #'break' es instrucciobn para parar cualquier bucle
print('Aqui inicia un bucle con continue')
num = 0
while num < 5:
    num += 1
    if num > 3:
        continue #'continue' es para segui a la instruccion que sigue en un bucle
    print('num = ', num)
#---------------------------------------------------------------
#Bucle sobre una lista de objetos
#---------------------------------------------------------------
nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)
#---------------------------------------------------------------
#Bucle en una cadena da caracteres
#---------------------------------------------------------------
for char in 'Hello':
    print(char)
#---------------------------------------------------------------
#Bucle sobre un diccionario
# items == elementos
#---------------------------------------------------------------
numNames = {1:'One', 2:'Two', 3:'Three'}
for pair in numNames.items():
    print(pair)
#---------------------------------------------------------------
#Bucle sobre un diccionario
# key == Llave primaria
# value == dato
#---------------------------------------------------------------
for i, j in numNames.items():
    print('Key = ', i, 'Value = ', j)
#---------------------------------------------------------------
#Aqui inician las funciones
#Primera funcion
#---------------------------------------------------------------
def saludo():
    #-----------------------------------------------------------
    #Documentacion rapida de la funcion
    #-----------------------------------------------------------
    """Esta funcion saluda"""
    print('¡Hola!, ¿Comó estas?')
saludo() #Llamado de la funcion
#---------------------------------------------------------------
#Se ejecuta pero asigna None o vacio
#---------------------------------------------------------------
salida = saludo()
print('impresion de la salida de la funcion', salida)
#Mostrar la documentacion --------------------------------------
help(saludo)
#---------------------------------------------------------------
#Funcion con argumento
#---------------------------------------------------------------
def salu2(nombre):
    """Esta funcion saluda por tu nombre"""
    print('¡Que paso ', nombre, '!')
salu2('Bosco')
salu2('Julian')
#---------------------------------------------------------------
#Ahorrar el trabajo del interprete
# nombre:str le dice que entra una varible tipo string (str)
#---------------------------------------------------------------
def saludos(nombre:str):
    """Esta funcion te saluda por tu nombre estrictamente"""
    print('Qué onda ese ', nombre, '!')
saludos('Bosco')
a = 123
print(type(a))
saludos(a)
#----------------------------------------------------------------
#Función con multiples argumentos
#----------------------------------------------------------------
def saludos_mul(nombre1, nombre2, nombre3):
    """Esta funcion saluda a 3 personas al mismo tiempo"""
    print('Hola ', nombre1, ",", nombre2, "y", nombre3)
saludos_mul('Hugo', 'Paco', 'Luis')
#---------------------------------------------------------------
#Función con un numero indeterminado de argumentos
#---------------------------------------------------------------
def muchos_saludos(*nombres):
    """Esta funcion saluda a todos los que quieras"""
    i = 0
    #end = es para ponerlo de manera continua
    print('Hola, ', end='')
    while len(nombres) > i:
        #Último nombre
        if (i == len(nombres) - 1):
            print(nombres[i])
        else:
            print(nombres[i], end=', ')
        i += 1
muchos_saludos('Bosco', 'Angel', 'Tamara', 'Mili', 'Edwin', 'Lev', 'Luis', 'Abigail')
def greet(firstname, lastname):
    print('Hello', firstname, lastname)
#Se pueden llamar los argumentos en desorden
greet(lastname = 'Jobs', firstname = 'Steve')
#---------------------------------------------------------------
#Función con argumentos escondidos
#---------------------------------------------------------------
def greet2(**person):
    #Persona tiene 2 elementos firstname y lastname
    print('Hello', person['firstname'], person['lastname'])
print('Segunda funcion con argumentos ocultos : ')
greet2(firstname = 'Steve', lastname = 'Jobs')
greet2(firstname = 'Bill',lastname =  'Gates', age = '55')
#Se pueden agregar argumentos extras pero no los usa
#---------------------------------------------------------------
#Función con valores por defecto
#---------------------------------------------------------------
def greet3(name = 'Guest'):
    print('Hello, ', name)
print('funcion con valores por defecto')
greet3()
print('funcion con valores definidos')
greet3('Steve')
#---------------------------------------------------------------
#Funión con resultado
#---------------------------------------------------------------
def suma(a, b):
    return a + b
print(suma(2, 5))
#---------------------------------------------------------------
#Programacion funcional
# Se pueden llamar funciones en funciones
#---------------------------------------------------------------
total = suma(5, suma(4, 6))
print(total)
#---------------------------------------------------------------
#Cálculo Lambda
# Nombre_de_funcion = lambda variable : funcion 
x_cuadrada = lambda x: x * x
a1 = x_cuadrada(5)
print(a1)
#---------------------------------------------------------------
#Labda con varias variables
#---------------------------------------------------------------
suma = lambda x1, x2, x3: x1 + x2 + x3
a2 = suma(1, 2, 3)
print(a2)
#---------------------------------------------------------------
#Lambda con un numero mas grande de variables
#---------------------------------------------------------------
sumas = lambda *x: x[0] + x[1] + x[2] + x[3]
print(sumas(100, 200, 300, 400))
#---------------------------------------------------------------
#El uso de una funcion anonima
#---------------------------------------------------------------
print((lambda x : x * x)(6))
#---------------------------------------------------------------
#Funcion con vaiable global
# ¡Evite el exceso!
#---------------------------------------------------------------
name = 'Steve'
def greet4():
    global name #Para usar una variable global (que viene fuera del bloque de código de la función)
    print('Hello', name)
greet4()

