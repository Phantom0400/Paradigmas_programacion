#***************************************************#---------------------------------------------------
#5  Laboratorio de de paradigmas de programacion
#Paradigma de programacion Orientada a Objetos
#--------------------------------------------------
# Una 'clase' es un objeto vacio, aun asi requiere
# la palabra reservada "pass" para se detectado 
# como objeto
#-------------------------------------------------
class ObjetoVacio:
    pass
#-------------------------------------------------
# nada es un ojeto vacio
#-------------------------------------------------
nada = ObjetoVacio()
print(nada)
print(type(nada))
#-------------------------------------------------
# La clase Lanta
#-------------------------------------------------
class Llanta():
    #---------------------------------------------
    # Variable cuenta es para toda la clase
    #---------------------------------------------
    cuenta = 0
    #---------------------------------------------
    # Funcion constructora de identidad
    # __init__ es una funcion reservada en el estandar 
    #de python comienza con el objeto mismo 'self'
    # que no es palabra reservada puede cambiarse 
    # de otra manera, parametros de entrada = default
    def __init__(self, radio = 50, ancho = 30, presion =1.5):
        #variable de la estructura completa de Llanta
        Llanta.cuenta += 1
        #Variables exclusivas de cada objeto
        self.radio = radio
        self.ancho = ancho
        self.presion = presion
#--------------------------------------------------
#Objetos instanciados
#--------------------------------------------------
llanta1 = Llanta(50, 30, 1.5)
llanta2 = Llanta(presion = 1.2)
llanta3 = Llanta()
llanta4 = Llanta(40, 30, 1.6)
#--------------------------------------------------
#Objeto que contiene a otros objetos
#--------------------------------------------------
class Coche:
    def __init__(self, ll1, ll2, ll3, ll4):
        self.llanta1 = ll1
        self.llanta2 = ll2
        self.llanta3 = ll3
        self.llanta4 = ll4
mi_coche = Coche(llanta1, llanta2, llanta3, llanta4)
print('Total de llantas: ', Llanta.cuenta) #Variable global de la clase
print('Presion de la llanta 4 : ', llanta4.presion)
print('Radio de la llanta 4: ', llanta4.radio) #Presion de la llanta 4
print('Radio de la llanta 3: ', llanta3.radio)
print('Presion de la llanta 1 de mi coche: ',mi_coche.llanta1.presion)
#--------------------------------------------------
# Encapsulamiento
# Uso de la funcion de python property para poner
# y obtener atributos
#--------------------------------------------------
class Estudiante:
    def __init__(self):
        self.__nombre = ''
    def ponerme_nombre(self, nombre):
        print('Se llamo a ponerme_nombre')
        self.__nombre = nombre
    def obtener_nombre(self):
        print('Se llamo a obtener nombre')
        return self.__nombre
    nombre = property(obtener_nombre, ponerme_nombre)
#--------------------------------------------------
# Crear objeto estudiante
#--------------------------------------------------
estudiante = Estudiante()
#--------------------------------------------------
# Poner nombre usando la propiedad nombre y el 
# metodo ponerme_nombre (sin tener que llamar 
# de manera explicita a la funcion)
#--------------------------------------------------
estudiante.nombre = 'Juan'
#--------------------------------------------------
#Obtener el nombre con el metodo obtener_nombre 
#__nombre es una variable encapsulada (no visible 
# desde afuera)
# sin tener que llamar explicitamente la funcion
# Obtener nombre
#--------------------------------------------------
print(estudiante.nombre)
#Esto no funciona:
#print(estudiante.__nombre)
#--------------------------------------------------
#Herencia de clases
#--------------------------------------------------
class Cuadrilatero:
    def __init__(self, a, b, c, d):
        self.lado1 = a
        self.lado2 = b
        self.lado3 = c
        self.lado4 = d
    def perimetro(self):
        per = self.lado1 + self.lado2 + self.lado3 + self.lado4
        print('perimetro = ', per)
        return per
#---------------------------------------------------
# Su Hijo rectangulo
# Rectangulo es hijo de cuadrilatero
# Rectangulo(Cuadrilatero)
#--------------------------------------------------
class Rectangulo(Cuadrilatero):
    def __init__(self, a, b):
        #------------------------------------------
        #Constructor de su madre (Cuadrilatero)
        #------------------------------------------
        super().__init__(a, b, a, b)
#--------------------------------------------------
#Su nieto Cuadrado
#Hijo de rectangulo
#--------------------------------------------------
class Cuadrado(Rectangulo):
    def __init__(self, a):
        super().__init__(a, a)
    def area(self):
        area = self.lado1**2
        return area
    def perimetro(self):
        per = 4*self.lado1
        print('Perimetro = ', per)
        return per
#--------------------------------------------------
# Crear un Cuadrado
#--------------------------------------------------
cuadrado1 = Cuadrado(5)
#--------------------------------------------------
# LLamar al metodo perimetro de su abuelo Cuadrilatero
#--------------------------------------------------
perimetro1 = cuadrado1.perimetro()
#--------------------------------------------------
#Llamar a su propio metodo 'area'
#--------------------------------------------------4
area1 = cuadrado1.area()
print('Perimetro = ', perimetro1)
print('Area = ', area1)
#--------------------------------------------------
#Sobreescribir un metodo de su madre o abuela es 
#volver a definir una funicion ya existente
#--------------------------------------------------
# La clase  A tiene tres numeros reales
#--------------------------------------------------
class A:
    __a = 0.0
    __b = 0.0
    __c = 0.0
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c
#--------------------------------------------------
# La clase B tiene 2 numeros reales 
#--------------------------------------------------
class B:
    __d = 0.0
    __e = 0.0
    def __init__(self, d:float, e:float):
        self.d = d
        self.e = e
    #----------------------------------------------
    #Metodo suamr_todo (internos + externos)
    #----------------------------------------------
    def sumar_todo(self, aa:float, bb:float):
        x:float = self.d + self.e + aa + bb
        return x
#--------------------------------------------------
# ASOCIACION
#--------------------------------------------------
#Usando objetos independientes
objetoA = A(1.0, 2.0, 3.0)
objetoB = B(4.0, 5.0)
print('Suma entre elementos de objetos: ',objetoB.sumar_todo(objetoA.a, objetoA.b))
#--------------------------------------------------
#El Objeto C tiene dos reales y un objeto A
# El objeto A se instancia dentro de C
#--------------------------------------------------
class C:
    __f:float = 0.0
    __g:float = 0.0
    __Aa:A=None
    def __init__(self, f:float, g:float):
        self.f = f
        self.g = g
        #A esta instanciado dentro de C
        self.Aa = A(1.0, 2.0, 3.0)
    def sumar_todo(self):
        x:float = self.f + self.g + self.Aa.a + self.Aa.b + self.Aa.c
        return x
#--------------------------------------------------
#COMPOCICION
#--------------------------------------------------
objetoC = C(4.0, 5.0)
print('suma de todos los elementos del objeto C: ', objetoC.sumar_todo())
#--------------------------------------------------
#Objeto D tienen dos reales y un objeto A
#definiendo A desde afuera
#--------------------------------------------------
class D:
    __h = 0.0
    __i = 0.0
    __Bb = None
    def __init__(self, h:float, i:float, Bb = A):
        self.h = h
        self.i = i
        self.Bb = Bb
    def sumar_todo(self):
        x:float = self.h + self.i + self.Bb.a + self.Bb.b + self.Bb.c
        return x
#--------------------------------------------------
#AGREGACION
#Construye el objeto agregado por fuera
#--------------------------------------------------
objetoD = D(6.0, 5.0, objetoA)
print('Suma de los elementos de D = ', objetoD.sumar_todo())
