#****************************************************
"""Quad tortuga"""
import turtle
tortuga = turtle.Turtle()
tortuga.left(90) #Giro de velocidad
tortuga.speed(500) #Velocidad de Torutga
angulo:float = 30 # -depende del angulo de el tipo de arbol
def arbol(i:float, angulo:float):
    if i < 10.0:
        return None
    else:
        tortuga.forward(i) #camina i
        tortuga.left(angulo) # Gira a la derecha
        arbol(3.0*i/4.25, angulo) # Pide otro arbol y cambia  la longitud del paso
        tortuga.right(2*angulo) # Gira a la derecha 180°
        arbol(3.0*i/4.25, angulo)
        tortuga.left(angulo)
        tortuga.backward(i)
arbol(100, angulo)
turtle.done()
#****************************************************
