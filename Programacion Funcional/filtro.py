#*****************************************************
"""
------------------------------------------------------
Uso de filtros
Hacer una lista de los números por arriba del promedio
por el modulo de estadística
------------------------------------------------------
"""
import statistics as st
bigdata = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
promedio = st.mean(bigdata)
print(promedio)
"""
------------------------------------------------------
Se hace una lista que tiene los elementos que cumplen 
la condición x > promedio; 'filter(condición, datos)'
------------------------------------------------------
"""
print(list(filter(lambda x: x > promedio, bigdata)))
# Limpiar los datos
paises = ['', 'Argentina', '', 'Brasil', '', 'Chile', 'México', '', 'Colombia', '', '', 'Cuba', 'Venezuela']
# Filttra los que no contiene nada
print(list(filter(None, paises)))
#*****************************************************
