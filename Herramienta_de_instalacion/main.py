"""
Este es un codigo para la descarga e instalacion de paquetes, para la compilacion
de un modulo del kernel de un WiFi-usb, este primero se ejecuta en la Raspberry pi
para obtener los links de descarga de los paquetes necesarios, para despues ejecutar
este mismo codigo pero ahora en la pc con conexion a internet, y asi descargar los 
paquetes
"""
import subprocess
import os
import shutil
import mostrar_informacion as st
import descargador as dw
import analisis as an

links_de_paquetes=[]
uris_de_paquetes=[]

def limpiar_terminal():
    clear = lambda : os.system('tput reset')
    clear()


def ejecutar_opcion(opcion):
    if opcion in ('R','r'):
        obtener_links_de_descargas()
    if opcion in ('P','p'):
        lista_formateada=formatear_archivo_links()
        descargar_archivos_deb(lista_formateada)
        verificando_integridad_sha256(lista_formateada)
        mover_descargas(".",ruta_de_carpeta_de_descargas)


limpiar_terminal()
status=st.mostrar_informacion_host()
print(st.BOLD+"Iniciando Analisis para ejecutar el procedimiento adecuado"+st.NORMAL)
if status["arquitectura"]:
    an.generar_txt_con_uris_de_paquetes(status)
else:
    if an.descargar_todos_los_componentes_necesarios(status):
        print(st.VERDE+st.BOLD)
        print("Todos los archivos necesarios se encuentran descargados")
        print("Ahora ejecuta el script en la aquitectura arm para la instalacion del driver")
        print(st.NORMAL)
#print(ejecutar_comando("ls .."))