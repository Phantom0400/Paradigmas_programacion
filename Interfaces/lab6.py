#**********************************************************************************+
#----------------------------------------------------------------------------------
# Del directorio aplicacion, subdirectorio repositorio
# El archivo basededatos,py: se importa el objeto Basededatos
#----------------------------------------------------------------------------------
from aplicacion.repositorio.basededatos import BaseDeDatos
#----------------------------------------------------------------------------------
# Del directorio aplicacion, subdirectorio repositorio, del archivo s3.py: 
# se importa el objeto S3
#----------------------------------------------------------------------------------
from aplicacion.repositorio.s3 import S3
#----------------------------------------------------------------------------------
# Del directorio aplicacion, subdirectorio repositorio, el archivo 
# sistemadearchivos.py: trae el objeto SistemaDeArchivos
#----------------------------------------------------------------------------------
from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos
#----------------------------------------------------------------------------------
# Del directorio aplicacion, subdirectorio modelos importa el archivo usuario.py
#----------------------------------------------------------------------------------
from aplicacion.modelos.usuario import Usuario
#----------------------------------------------------------------------------------
# Del directorio aplicaciono, subdirectorio negocios, archivo manejodeinscripciones
# importa el objeto ManejoDeInscripciones
#----------------------------------------------------------------------------------
from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones
#----------------------------------------------------------------------------------
# Crear el objeto Usuario
#----------------------------------------------------------------------------------
usuario = Usuario('Roberto', 'Jimenez', 18)
#----------------------------------------------------------------------------------
# Crear el objeto S3
#----------------------------------------------------------------------------------
repositorioS3 = S3('321321321', 'sdf324223', 'MiCubeta')
#----------------------------------------------------------------------------------
# Interface inscribirUsuario del objeto ManejoDeInscripciones
#----------------------------------------------------------------------------------
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioS3)
print('\n')
#---------------------------------------------------------------
# Crea el objeto sistemadearchivos
#---------------------------------------------------------------
repositorioSistemaDeArchivos = SistemaDeArchivos('home/users')
#---------------------------------------------------------------
# Interface inscribirUsuario del objeto ManjoDeInscripciones
#---------------------------------------------------------------
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioSistemaDeArchivos)
print('\n')
#---------------------------------------------------------------
# Crea el objeto base de datos
#---------------------------------------------------------------
repositorioBaseDeDatos = BaseDeDatos('localhost', 'admin', 'admin123')
#---------------------------------------------------------------
# Inteface inscribirUsuario del objeto ManejoDeInscripiciones
#---------------------------------------------------------------
ManejoDeInscripciones.inscribirUsuario(usuario, repositorioBaseDeDatos)
print('\n')
#***************************************************************
