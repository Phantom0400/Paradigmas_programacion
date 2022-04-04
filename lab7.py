#***************************************************************
from aplicacion.banco.cliente_bancario import ClienteBancario
#---------------------------------------------------------------
# try: intenta (correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#---------------------------------------------------------------
# Error por sacar mas dinero del que tiene 
#---------------------------------------------------------------
try: 
    cliente = ClienteBancario('Jaime Andrade', 'Hernandez Sánchez', 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())
#---------------------------------------------------------------
# Exception es el objeto mas general de error
#---------------------------------------------------------------
except Exception as e:
    print('Error: ' + str(e))
try:
    print(cliente.__nombres)
except Exception as ex:
    print('Error: ' + str(ex))
#---------------------------------------------------------------
# Forma Correcta
#---------------------------------------------------------------
print(cliente.nombres)
#***************************************************************
