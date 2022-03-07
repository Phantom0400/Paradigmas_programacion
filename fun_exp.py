#***************************************************************
#---------------------------------------------------------------
#Función Exponencial 
#empaquetamiento como función
#---------------------------------------------------------------
def e(x):
    n = 100000
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
    return e #recordar siempre poner un valor de retorno si se quiere hacer recursiva
exponencial = e(e(e(-1)))
#***************************************************************
