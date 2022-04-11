#*****************************************************************
#-----------------------------------------------------------------
# open() es la funcion para abrir un archivo, python admite el 
# manejo de archivos binarios brutos y archivos binarios de salida
# la funcion read() es la manera de leer el archivo de texto hasta 
# el final del archivo, salvo que este tenga argumento que es 
# la cantidad de caracteres leidos, por tanto, se asigna como una 
# cadena de  caracteres str()
#-----------------------------------------------------------------
a = open('archvivo.txt')
linea1 = a.readline()
linea2 = a.readline()
linea3 = a.read(4) # solo va a leer 4 caracteres de la tercera linea
#-----------------------------------------------------------------
# la funcion readline() lee linea  a linea un archivo de texto
# y al poner algun otro funcion de lectura continuara desde la 
# útlima linea de lectura con respecto a las demas funciones de 
# lectura
#-----------------------------------------------------------------
print('aqui se imprimen las primeras lineas:\n', linea1, linea2, linea3)
lineas = a.readlines()
print('aqui se escribe el texto completo\n', lineas)
a.close()
#-----------------------------------------------------------------
# La función close() sirve para cerrar el archivo de lectura
#-----------------------------------------------------------------
#*****************************************************************
