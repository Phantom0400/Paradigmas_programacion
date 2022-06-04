#***************************************************************
#---------------------------------------------------------------
#Conjunto en Python 
#---------------------------------------------------------------
even_nums = {2, 4, 6, 8, 10} #Un Conjunto de numeros pares 
print(even_nums)
#Conjunto de diferentes objetos
emp = {1, 'Martin', 10.85, True} #El tipo bool no se procesa
print(emp)
nums = {1, 2, 2, 3, 4, 4, 5, 5} #Como en logica de conjuntos se omiten los elementos repetidos
print(nums)
#---------------------------------------------------------------
#Convertir una secuencia de caracteres a un conjunto con set()
#No genera un Orden predeterminado
#---------------------------------------------------------------
s = set('Hola')
print(s)
#---------------------------------------------------------------
#Conversion de diccionario a conjunto con llaves 
#---------------------------------------------------------------
d = {1:'Uno', 2: 'Dos'} #Fija pociciones del conjunto
s = set(d) 
print(s)
#---------------------------------------------------------------
s.add(100) #Funcion de adicion del objeto lista o en este caso en conjuntos
print(s)
#---------------------------------------------------------------
s.update(nums) #Agrega elementos de otras listas en el conjunto solicitante con la funcion update
print(s)
#---------------------------------------------------------------
s.remove(100) #Quita el elemento '100' del conjunto con la funcion remove
print(s)
#---------------------------------------------------------------
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
su = s1|s2 #Union de conjuntos con el '|'
print(su)
si = s1&s2 #Interseccio de conjuntos con '&'
print(si)
sr = s1 - s2 #Diferencia de conjuntos con '-'
print(sr)
sp = s2 - s1
print(sp)
ss = s1^s2 #Diferencia simetrica, es decir la union menos la interseccion 
print(ss)
#---------------------------------------------------------------
#Uso de diccionarios
#---------------------------------------------------------------
capitals = {"USA": "Washington D.C.", "France": "Paris", "India": "New Dehli"}
print(capitals)
#---------------------------------------------------------------
#se usa el siguiente formato:
#       key : data ||||||| llave primaria : dato
#---------------------------------------------------------------
d = {} #Diccionario Vacio
numNmaes = {1: "Uno", 2: "Dos", 3:"Tres"} #Llave entera: valor string
decNames = {1.5: "Uno punto cinco", 2.5: "Dos punto cinco", 3.5:"Tres punto cinco"} #Llave decimal: valor string
items = {("Parker", "Reynolds", "Camlin"): "pen", ("LG", "Whirpoll", "Samsung"): "Fridge"} #Llave tupla, dato string
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}
print(romanNums)
print(romanNums['I']) #Ubicacionde datos por llave primaria
print(capitals.get("India")) #Busqueda en el diccionario
print(capitals.get("india")) #Sensible al cambio de caracteres, es decir lo guardado es inmutable hasta cambio determinado por el usuario
#Reportar llave y valor
for k in capitals:
    print("key = " + k + ", Value = " + capitals[k])
#Insertar datos para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)
#Borrar dato del diccionario
del capitals["USA"]
print(capitals)
#Borrar todo el diccionario
del capitals
#Reportar llaves 
print(romanNums.keys())
#Reportar valores
print(romanNums.values())
#Juicio de llave (esta o no esta en el diccionario)
print("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)
#---------------------------------------------------------------
#Listas en Python
#Las listas pueden ser de diversos objetos
#---------------------------------------------------------------
miprimeralista = [] # Lista Vacia
print(miprimeralista)
#---------------------------------------------------------------
#Llenando la primera lista
#---------------------------------------------------------------
miprimeralista = [1, "Javier", 1.35, "Bosco", "Angel", "Abigail", True]
print(miprimeralista)
#---------------------------------------------------------------
#list : crear una lista
#range(i, j) secuencia de i hasta j-1
#--------------------------------------------------------------
nums = list(range(1,61))
print(nums)
for i in nums:
    print(i)
#Incluir elementos en la lista
nums.append(61)
nums.append(62)
nums.append(61)
print(nums)
#---------------------------------------------------------------
#Quitar elementos de la lista 
#---------------------------------------------------------------
nums.remove(61)
print(nums)
#---------------------------------------------------------------
#Quitar elemento j-eismo
#---------------------------------------------------------------
j = 61
del nums[61]
print(nums)
#---------------------------------------------------------------
#Borrar lista
#---------------------------------------------------------------
del nums
#print(nums) Ya no existe nums
#---------------------------------------------------------------
#Sumar listas 
#---------------------------------------------------------------
L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(L1 + L2)
#---------------------------------------------------------------
#Llenado a mano
#---------------------------------------------------------------
potencial = []
for i in range(0, 10000):
    potencial.append(float(i))
print(potencial[100])
#---------------------------------------------------------------
#Geenrar un tupla con una lista
#---------------------------------------------------------------
potencial = tuple(potencial)
print(potencial[100])
#***************************************************************
