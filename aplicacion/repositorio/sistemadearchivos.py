#***************************************************************
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import modelos
#---------------------------------------------------------------
# Inplementa la interface RepositorioDeUsuarios
#---------------------------------------------------------------
class SistemaDeArchivos(RepositorioDeUsuarios):
    __directorio: str
    def __init__(self, directorio:str):
        self.__directorio = directorio
    def abrir(self) -> None:
        print(f'Abrir derectorio: {self.__directorio}')
    def guardar(self, usuario:Usuario) -> None:
        xml = f"</root></name>{usuario.getNombre()}</lastName>{usuario.getApellido()}</lastName></age>{usuario.getEdad()}</age></root>"
        print(f"Guardando usuario en el archivos: {self.__directorio}/{usuario.getNombre()}")
        print(xml)
    def cerrar(self) -> None:
        print('cerrando el archivo')
#***************************************************************
