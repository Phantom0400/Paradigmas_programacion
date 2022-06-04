#***************************************************************
from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
#---------------------------------------------------------------
# Clase storemanager
# NO TIENE VARIABLES
#---------------------------------------------------------------
class ManejoDeInscripciones:
    """ decorados staticmethod
    el objeto solo tiene la funcion de inscribirUsuario
    envuelve la funcion sin llamar variables locales 
    el objeto ManejoDe inscripciones es la interface intercambiable
    """
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositorioDeUsuarios:RepositorioDeUsuarios) -> None:
        print('-------------------> Guardando Usuario...\n')
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
#***************************************************************
