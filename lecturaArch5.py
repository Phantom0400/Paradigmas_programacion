#************************************************************************
#------------------------------------------------------------------------
# Ingresando cosas en un archivo ya existente con el parametro 'a' o 'a+'
#------------------------------------------------------------------------
f = open('archvivo.txt', 'a+')
f.write('linea ingresada')
f.close()
f = open('arcvivo.txt', 'w') # Para ingresar multiples lineas con 'w'
lineas = ['Una linea mas\n', 'Otra linea mas\n']
f.writelines(lineas)
f.close()
f = open('archvivo.txt')
lin = f.read()
print(lin)
f.close()
#************************************************************************
