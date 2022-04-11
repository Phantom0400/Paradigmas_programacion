#*************************************************************
#-------------------------------------------------------------
# Lectura de archivos con iteracion por lineas sin necesidad 
# de marcar caracteres
#-------------------------------------------------------------
b = open('archvivo.txt')
while True:
    try:
        line = next(b) # asigna una linea de texto
        print(line) # la imprime y pasa a la siguiente iteracion
    except StopIteration: #Hasta que topa con la ultima linea 
        break
b.close()
#-------------------------------------------------------------
# otra forma con un ciclo for
#------------------------------------------------------------
print('imprime otro archivo .txt')
c = open('otro.txt')
for line in c:
    print(line)
c.close()
#*************************************************************
