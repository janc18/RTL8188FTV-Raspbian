"""
Ejecutando uname -a se puede obtener informacion de la distro y arquitectura 
Comprobar dependencias (Git,Wget)
Comprobar si cuenta con conexion de internet
Comprobar si ya se instalo en driver
Analisis(busqueda de archivos y carpeta en el directorio actual)
Mostrar informacion si los paquetes ya fueron previamente instalados
"""
import os
import socket
import shutil
BOLD="\033[1m"
NORMAL="\033[0m"
VERDE="\033[92m"
ROJO="\033[91m"
AZUL="\033[94m"
def verificar_si_el_programa_esta_instalado(programa):
    if(shutil.which(programa)==None):
        print(ROJO+"El Programa " + programa + " no esta instalado"+NORMAL)
        return programa
    else:
        print(VERDE+"El Programa " + programa + " esta instalado"+NORMAL)
        return "si "+programa

def verificar_arquitectura():
    arquitectura=os.uname()[4]
    print(AZUL+"La arquitectura del host es " + arquitectura +NORMAL)
    return arquitectura
def esta_conectado_a_internet():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        sock = socket.create_connection(("one.one.one.one",80))
        if sock is not None:
            sock.close
        return True
    except OSError:
        pass
    return False

def verificar_conexion_a_internet():
    if esta_conectado_a_internet():
        print(VERDE+"Con conexión a internet"+NORMAL)
        return "Con internet"
    else:
        print(ROJO+"Sin conexión a internet"+NORMAL)
        return "Sin internet"

def mostrar_informacion_host():
    status={}
    print(BOLD+"---Mostrando información del host---"+NORMAL)
    status[0]=verificar_arquitectura()
    print(BOLD+"----Verificando dependencias---------"+NORMAL)
    status[1]=verificar_si_el_programa_esta_instalado("git")
    status[2]=verificar_si_el_programa_esta_instalado("wget")
    print(BOLD+"----Comprobando conexión a Internet---------"+NORMAL)
    status[3]=verificar_conexion_a_internet()
    print("-------------------------------------")
    print(status)