"""Este es un supercomentario de inicio para el resumen"""
#**************************************************************
#--------------------------------------------------------------
#Operaciones basicas
#--------------------------------------------------------------
print(2+3)  #SUMA DE ENTEROS
print(2*3)  #MULTIPLICACION
print(2/3)  #DIVISION
print(2**10)#POTENCIACION
print(2**0.5)#RAIZ CUADARADA
print(10%2) #MODULO
print(10%0.1)#MODULO FRACCIONARIO
#--------------------------------------------------------------
#Para saber el tipo de objeto se usa la palabra reservada "type"
#--------------------------------------------------------------
t = 0 #Asignacion de objeto
print(type(t))#Tipo de Objeto entero
t = 3.6
print(type(t))#Tipo de Objeto float
t = True 
print(type(t))#Tipo de Objeto booleano
#--------------------------------------------------------------
#Mensajes a la pantalla 
#--------------------------------------------------------------
print("Este es un comentario de Python3. ", "Este es otro enunciado", t)#Se pueden dar tabulciones separando el texto con comas por afuera de las comillas 
print('id: ', 1) #Se pueden colocar directamente los numeros para que los impriman
print('First Name: ', 'Bosco')#Tambien se pueden usar las comillas simples para encerrar texto
print('Last Name: ', 'Ortiz')
print('Vamos a sumar esto' + 'con esto otro') #Se pueden sumar las cadenas de caracteres en la funcion print()
#--------------------------------------------------------------
#Continuar una instruccion en varios renglones
#--------------------------------------------------------------
if 100 > 99 and \
200 <= 300 and \
True != False:
         print('Esto deberia aparecer siempre')
#--------------------------------------------------------------
#Comandos en una misma linea
#--------------------------------------------------------------
print('Hola '); print(' tu !!') #Se considera una mala practica
#--------------------------------------------------------------
#Usando parentesis rendondos, cuadrados o llaves 
#se puede escribir en varios renglones
#--------------------------------------------------------------
list = [1, 2, 3, 4, 
        5, 6, 7, 8, 
        9, 10, 11, 12]
matriz = [[1, 2, 3, 4],[5 ,6 ,7 ,8],[9, 10, 11, 12]]
print(list)
print(matriz)
#--------------------------------------------------------------
#Indetacion Estricta para los procesos dependientes de ':' (Dos puntos)
#--------------------------------------------------------------
if 10 > 5:
    print("Diez mayor a cinco")
    print("otra identacion")
for i in list:
    print(i)
    print('ok')
if 10 > 5:
    print('verdadero')
    if 10 < 20:
        print('verdadero')
elif 5 > 3:# El elif tiene que llevar una condicion logica
    print('Nunca se va a imprimir') 
else:
    print('Aqui tampoco va a llegar')
#--------------------------------------------------------------
#Fucniones 
#--------------------------------------------------------------
def say_hello(name):
    print('Hello ', name)
    print('Welcome to Python Tutorials')
say_hello('Bosco') #Se llama a la funcion 
#--------------------------------------------------------------
#Aqui inicia la segunda parte de la introduccion a python
#input() permite obtener datos del usuario directo desde el prompter
#--------------------------------------------------------------
nombre = input('Dame un nombre: ')
print('Hola como estas ', nombre, '?')
#--------------------------------------------------------------
#Los enteros son de precicion ilimitada
#--------------------------------------------------------------
y = -50701000000002000090080000400007001
print(y)
#--------------------------------------------------------------
#Se pueden delimitar numeros con un gion bajo pero no con coma
#--------------------------------------------------------------
y = 5_000_000_000
print(y)
#--------------------------------------------------------------
#La funcion int() cambia strings y floats a enteros 
#--------------------------------------------------------------
numero = int(input("Dame tu edad: "))
print(type(numero))
#--------------------------------------------------------------
#La notacion cientifica de flotantes utiliza 'e' o 'E'
#--------------------------------------------------------------
#1.2 x 10^{-9}
#--------------------------------------------------------------
y = 1.2e-09
print(y)
#--------------------------------------------------------------
#Los complejos se escriben con la raiz de menos uno
#Con 'j' siempre con algun numero de prefijo como multiplo
#No acepta la j unica
#--------------------------------------------------------------
z = 1+1j
print(z)
#suma '+'
#resta '-'
#multiplicaion '*'
#division '/'
#modulo '%'
#exponente '**'
#funcion piso '//'
#Funciones para transformar numeros int(), float(), complex()
#Operaciones abs(), round(), pow()
print(round(3.14159, 4))
print(abs(-1.2))
print(pow(5, 6))
#--------------------------------------------------------------
#Strings de varias lineas
#--------------------------------------------------------------
parrafo = """En el bosque de la china
 la chinita se perdio""" #Se usan las tres comillas para dividir entre lineas una cadena de caracteres 
print(parrafo)
#--------------------------------------------------------------
#La funcion len() obtiene el tamaño del string
#--------------------------------------------------------------
n = len(parrafo)
print(n)
#--------------------------------------------------------------
#Las letras en un string ocupan lugares como en un arreglo
#(Tambien de atras para delante comenzando con -1 como el ultimo)
#--------------------------------------------------------------
palabra = 'Hola'
print(palabra[0]) #Se accede a las pociciones de una lista con los corchetes '[]'
print(palabra[-1])
#**************************************************************
