#***************************************************************
#---------------------------------------------------------------
#Tercer laboratorio por Ortiz Ortiz Bosco
#Tercer intento de programacion de la funcion 
#           EXPONENCIAL
#Con la factorizacion de los productos
#---------------------------------------------------------------
n = 100000
x = float(input('Ingresa un exponente: '))
xx = x
if x < 0:
    flag = True
    x = -x
e = 1
s = 1
for i in range(n, 0, -1):
    s *= x/float(i)
    s += 1
if xx < 0:
    e = 1/s
else:
    e = s
print('e^',xx ,' = ',e)
#Este programa solo calcula expoenetes mayores o iguales que -17
#Con una computadora con AMD ryzen 5 3600
#***************************************************************
