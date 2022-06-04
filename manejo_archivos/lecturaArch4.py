#**************************************************************
#--------------------------------------------------------------
# Escribiendo un archivo con el parametro 'r' de la funcion
# open()
#--------------------------------------------------------------
e = open('otro2.txt', 'w')
e.write('Este es otro archivo')
e.close()
e = open('otro2.txt')
lin = e.read()
print(lin)
e.close()
#**************************************************************
