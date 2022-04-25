#****************************************************************
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario
#----------------------------------------------------------------
# S3 es hijo de RepositorioDeUsuarios 
#----------------------------------------------------------------
class S3(RepositorioDeUsuarios):
    __clientId: str
    __secretKey: str
    __bucket: str
    def __init__(self, clientId: str, secretKey: str, bucket: str):
        self.__clientId = clientId
        self.__secretKey = secretKey
        self.__bucket = bucket
    def abrir(self) -> None:
        print(f"Estableciendo conexión a AWS S3 {self.__clientId}")
    def guardar(self, usuario: Usuario) -> None:
        userData = {"nombre":usuario.getNombre(), "apellido":usuario.getApellido(), "edad":usuario.getEdad()}
        print(f"Guardando usuario de la bandeja: {self.__bucket}:{userData}")
    def cerrar(self) -> None:
        print('Cerrando conexión AWS S3')
#****************************************************************
