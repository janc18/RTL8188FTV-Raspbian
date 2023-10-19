"""
Este es un codigo para la descarga e instalacion de paquetes, para la compilacion
de un modulo del kernel de un WiFi-usb, este primero se ejecuta en la Raspberry pi
para obtener los links de descarga de los paquetes necesarios, para despues ejecutar
este mismo codigo pero ahora en la pc con conexion a internet, y asi descargar los 
paquetes
"""
import hashlib
import subprocess
import os
import shutil
import descargador
import mostrar_informacion as st
paquetes_requeridos=["build-essential","dkms","raspberrypi-kernel-headers"]
links_de_paquetes=[]
uris_de_paquetes=[]
ruta_de_archivo_con_links="archivos_links.txt"
ruta_de_carpeta_de_descargas="Descargas_de_paquetes"
# Preguntarle al usuario si se encuentra en la Raspberry pi o en la Pc
"""
host=input("¿En donde se encuentras en la Pc o en la Raspberry pi?\n"
           "Presione la opción correspondiente:\n"
           "R:\tRaspberry pi\n"
           "P:\tPC\n")
# Verificar si la opcion es valida
if host not in ('R','P','r','p'):
    print("Opción Invalida")
    exit()

"""
def descargar_archivos_deb(matriz_de_links):
    print("Estos son los paquetes que se descargaran")
    for paquetes in matriz_de_links:
        print(paquetes[1])

    for paquetes in matriz_de_links:
        nombre_archivo=paquetes[1]
        parametros_wget=["wget","--no-check-certificate",paquetes[0],"-O",nombre_archivo]
        subprocess.run(parametros_wget,capture_output=True)
        print("Descarga de paquete",nombre_archivo,"completa",)

# Si te encuentras en la pc verifica si existe el archivo de texto con los links de 
# descarga de los paquetes requeridos 
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
    except FileNotFoundError:
        print("No se encotro el archivo")

def comparar_sha256(ruta):
    sha256 = hashlib.sha256()
    with open(ruta, 'rb') as archivo:
        for bloque in iter(lambda: archivo.read(4096), b''):
            sha256.update(bloque)
    return sha256.hexdigest()


def formatear_archivo_links():
    lista_formateada =[]
    
    try:
        with open(ruta_de_archivo_con_links,'r') as archivo:
            for linea in archivo:
                linea_sin_n=linea.replace("'","")
                linea_sin_n=linea_sin_n.strip()
                linea_sin_n=linea_sin_n.split()
                lista_formateada.append(linea_sin_n)
        archivo.close
        print("Formateando archivo para su proceso")

        return lista_formateada
    except FileNotFoundError:
        print("No se encontro el archivo")

def verificando_integridad_sha256(lista_formateada):
    #sha256_paquete=""
    sha256_paquete_txt=""
    for paquete in lista_formateada:
        print("Verificando el paquete",paquete[1])
        sha256_paquete_txt=paquete[3]
        sha256_paquete_txt=sha256_paquete_txt.replace("SHA256:","")
        if sha256_paquete_txt==comparar_sha256(paquete[1]):
            print("Comprobacion exitosa de ",paquete[1])
        else:
            print("Error en la comprobacion")


def mover_descargas(directorio_origen,carpeta_destino):
    print("Moviendo archivos .deb")
    os.makedirs(carpeta_destino, exist_ok=True)

    for nombre_archivo in os.listdir(directorio_origen):
        ruta_archivo = os.path.join(directorio_origen, nombre_archivo)

        if nombre_archivo.endswith('.deb') and os.path.isfile(ruta_archivo):
            archivo_destino = os.path.join(carpeta_destino, nombre_archivo)
            shutil.move(ruta_archivo, archivo_destino)

def ejecutar_opcion(opcion):
    if opcion in ('R','r'):
        obtener_links_de_descargas()
    if opcion in ('P','p'):
        lista_formateada=formatear_archivo_links()
        descargar_archivos_deb(lista_formateada)
        verificando_integridad_sha256(lista_formateada)
        mover_descargas(".",ruta_de_carpeta_de_descargas)
#ejecutar_opcion(host)

def ejecutar_comando(comando):
    lista=[]
    lista=comando.split()
#    output=subprocess.run(lista,capture_output=False,shell=True)
    output=subprocess.run(lista)
    return output



st.mostrar_informacion_host()
#print(ejecutar_comando("ls .."))