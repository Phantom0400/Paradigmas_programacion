#**********************************************************
#----------------------------------------------------------
# Escritura de archivos binarios
# 'b' es para abrir un archivo binario
# 'rb' es para crear un archivo binario para lectura
# 'wb' para abrir un archivo para escritura
#----------------------------------------------------------
g = open('num.bin', 'wb')
num = [1, 2, 3, 4, 5]
arreglo = bytearray(num)
g.write(arreglo)
g.close()
g = open('num.bin', 'rb')
bi = g.read()
print(bi)
g.close()
#**********************************************************
