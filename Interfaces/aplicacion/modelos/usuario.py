#***************************************************************
#---------------------------------------------------------------
# CLase Usuario
#---------------------------------------------------------------
class Usuario:
    __nombre:str
    __apellido:str
    __edad:int
    #-----------------------------------------------------------
    #Constructor
    #-----------------------------------------------------------
    def __init__(self, nombre:str, apellido:str, edad:int):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    #getters
    def getNombre(self) -> str:
        return self.__nombre
    def getApellido(self) -> str:
        return self.__apellido
    def getEdad(self) -> str:
        return self.__edad

#***************************************************************
