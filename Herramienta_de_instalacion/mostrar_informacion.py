"""
Ejecutando uname -a se puede obtener informacion de la distro y arquitectura 
Comprobar dependencias (Git,Wget)
Comprobar si cuenta con conexion de internet
Comprobar si ya se instalo en driver
Analisis(busqueda de archivos y carpeta en el directorio actual)
Mostrar informacion si los paquetes ya fueron previamente instalados
Verificar que la version del kernel sea compatible con el driver
"""
import os
import socket
import shutil
import descargador as dw
import subprocess
import mensajes as msg
BOLD="\033[1m"
NORMAL="\033[0m"
VERDE="\033[92m"
ROJO="\033[91m"
AMARILLO="\033[93m"
AZUL="\033[94m"
paquetes_requeridos=["build-essential","dkms","raspberrypi-kernel-headers"]
ruta_de_archivo_con_links="archivos_links.txt"

def verificar_si_el_programa_esta_instalado(programa):
    if(shutil.which(programa)==None):
        print(ROJO+"El Programa " + programa + " no esta instalado"+NORMAL)
        return False
    else:
        print(VERDE+"El Programa " + programa + " esta instalado"+NORMAL)
        return True

def obtener_links_de_descargas():
    print("Obteniendo links de descarga de los siguientes paquetes:",paquetes_requeridos)
    
    try:
        with open(ruta_de_archivo_con_links,'w') as archivo:

            for paquetes in paquetes_requeridos: 
                parametros_apt=["apt-get","download","--print-uris",paquetes]
                print(parametros_apt)
                datos_de_paquetes=subprocess.run(parametros_apt,capture_output=True,text=True)
                archivo.write(datos_de_paquetes.stdout)
            archivo.close
        print(VERDE+BOLD) 
        print("Archivo con los links generados")
        print("Ahora puedes ejecutar el script en la PC con acceso a internet")
        print(NORMAL)
    except FileNotFoundError:
        print("No se encontro el archivo")
    
def verificar_arquitectura():
    arquitectura=os.uname()[4]
    print(AZUL+"La arquitectura del host es " + arquitectura +NORMAL)
    es_arm=str(arquitectura).__contains__("arm")
    return es_arm

def verificar_kernel_compatible():
    kernel=os.uname()[2]
    print(AZUL+"La versión del kernel es " + kernel+NORMAL)
    kernel=str(kernel).split(".")
    kernel_version_mayor=int(kernel[0])
    kernel_version_menor=int(kernel[1])
    if (kernel_version_mayor>=4 or kernel_version_mayor<=6) or (kernel_version_mayor==6 and kernel_version_menor==0):
        print(VERDE+"La versión del kernel si es compatible con el driver"+NORMAL)
        return True
    else:
        print(ROJO+"La versión del kernel no es compatible con el driver"+NORMAL)
        return False

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
        return True
    else:
        print(ROJO+"Sin conexión a internet"+NORMAL)
        return False

def mostrar_informacion_host():
    status={"arquitectura":False,
            "kernel_compatible":False,
            "existe_git":False,
            "existe_apt":False,
            "existe_conexion_internet":False,
            "existe_paquetes_descargados":False,
            "existe_archivos_links":False,
            "existe_repositorio_driver":False
    }
    print(BOLD+"---Mostrando información del host---"+NORMAL)
    status["arquitectura"]=verificar_arquitectura()
    status["kernel_compatible"]=verificar_kernel_compatible()
    print(BOLD+"----Verificando dependencias---------"+NORMAL)
    status["existe_git"]=verificar_si_el_programa_esta_instalado("git")
    status["existe_apt"]=verificar_si_el_programa_esta_instalado("apt-get")
    print(BOLD+"----Comprobando conexión a Internet---------"+NORMAL)
    status["existe_conexion_internet"]=verificar_conexion_a_internet()
    print("-------------------------------------")
    print(BOLD+"-----Verificando si existen paquetes previamente descargados-------"+NORMAL)
    status["existe_paquetes_descargados"]=dw.verificando_existencia_de_paquetes("Descargas_de_paquetes")
    print(BOLD+"-----Verificando si existe archivo con la ruta de descarga de los paquetes------"+NORMAL)
    status["existe_archivos_links"]=dw.verificando_existencia_de_archivo("archivos_links.txt","No se encontro el archivo con links")
    print(BOLD+"-----Verificando si ya se encuentra descargado el repositorio git-----"+NORMAL)
    status["existe_repositorio_driver"]=dw.existe_repositorio_git_driver()
    return status

def mostrar_informacion_script():
    print(AMARILLO)
    print(msg.mensaje_bienvenida)
    print(msg.nota_distro_compatible)
    print(msg.version)
    print(NORMAL)

# Cambio de rama y commit debe de ser ejecutado en el disposito que cuenta internet

def cambio_de_rama_y_commit_repositorio_git(lista_resumen):
    if lista_resumen["existe_git"] and lista_resumen["existe_repositorio_driver"]:
        ubicacion_repositorio_rtl=os.getcwd()+"/"+"rtl8188fu"
        print(ubicacion_repositorio_rtl)
        subprocess.run(["git","-C",ubicacion_repositorio_rtl,"checkout","b037"])
    else:
        print("No se encontro el repositorio y/o no cuenta con git")

# TODO: Agregar algun tipo de verificacion al repositorio del driver, por que por el 
# momento solo verifica la existencia de la carpeta