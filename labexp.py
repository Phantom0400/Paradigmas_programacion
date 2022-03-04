#***************************************************************
#---------------------------------------------------------------
#Programa por Ortiz Ortiz Bosco
#Practica 1: 
#Calcular e
#d(e^x)/dx = e^x = 1 + x + x^2/2 + x^3/6 + ... + x^n/n! + ...
#          = 1 + x(1 + x/2 (1 + x/3 (1 + x/4 (1 + x/5(1 + ...)))))
#Simplificacion del caluclo
#---------------------------------------------------------------
n = 100000
fact = 1.0
e = 1.0
x = 1.0 
xx = 1.0
for i in range(1, n):
    xx *= x
    fact *= float(i)
    s = xx/fact
    e += s
print(e)
print('Este algoritmo solo calcula e^1 y e^-1')
#---------------------------------------------------------------
#fuera de los numeros entre -1 y 1 el algoritmo no calcula e^x ya que retorna nan
#---------------------------------------------------------------
#***************************************************************
