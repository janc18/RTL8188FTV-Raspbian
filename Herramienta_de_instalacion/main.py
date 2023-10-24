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

limpiar_terminal()
st.mostrar_informacion_script()
status=st.mostrar_informacion_host()
print(st.BOLD+"Iniciando Analisis para ejecutar el procedimiento adecuado"+st.NORMAL)
if status["arquitectura"]:
    an.generar_txt_con_uris_de_paquetes(status)
if status["existe_paquetes_descargados"] and status["existe_repositorio_driver"] and status["arquitectura"]: 
    print("""Ya puedes ejecutar el script Instalador.sh,recuerda darle permiso usando\n
            \"chmod +x Instalador.sh\"
            """)
else:
    if an.descargar_todos_los_componentes_necesarios(status):
        print(st.VERDE+st.BOLD)
        print("Todos los archivos necesarios se encuentran descargados")
        print("Ahora ejecuta el script en la aquitectura arm para la instalacion del driver")
        print(st.NORMAL)
#print(ejecutar_comando("ls .."))