#***************************************************************
from aplicacion.modelos.usuario import Usuario
#---------------------------------------------------------------
# Este objeto es una interface
#---------------------------------------------------------------
class RepositorioDeUsuarios:
    def abrir(self) -> None:
        pass
    def guardar(self, usuario:Usuario) -> None:
        pass
    def cerrar(self) -> None:
        pass
#***************************************************************
