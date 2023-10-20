"""
Aqui se diseña una funcion para la descarga de los paquetes .deb
ademas de conocer si ya fueron previamente descargados los paquetes
"""
import requests
import os
import shutil

def descargar_archivos_deb_con_requests(matriz_de_links):
    print("Estos son los paquetes que se descargaran")
    for paquetes in matriz_de_links:
        print(paquetes[1])

    for paquetes in matriz_de_links:
        nombre_archivo=paquetes[1]
        archivo=requests.get(paquetes[0])
        open(os.getcwd()+"/"+nombre_archivo,"wb").write(archivo.content)
        print("Descarga de paquete",nombre_archivo,"completa",)

def mover_descargas_deb_a_directorio(directorio_origen,carpeta_destino):
    print("Moviendo archivos .deb a la carpeta \"Descargas_de_paquetes\"")
    os.makedirs(carpeta_destino, exist_ok=True)

    for nombre_archivo in os.listdir(directorio_origen):
        ruta_archivo = os.path.join(directorio_origen, nombre_archivo)

        if nombre_archivo.endswith('.deb') and os.path.isfile(ruta_archivo):
            archivo_destino = os.path.join(carpeta_destino, nombre_archivo)
            shutil.move(ruta_archivo, archivo_destino)

def verificando_existencia_de_paquetes(carpeta_paquetes_deb):
    #Conocer si la carpeta de Descargas_de_paquetes existe
    #Listar paquetes .deb
    #Si se encuentran no iniciar descargas
    try:
        os.makedirs(carpeta_paquetes_deb,exist_ok=False)
    except FileExistsError:
        print("Carpeta de Descarga de paquetes encontrada")
        print("Buscando paquetes deb")
        lista_de_paquetes=[]
        for nombre_de_paquete in os.listdir(carpeta_paquetes_deb):
            if nombre_de_paquete.endswith('.deb'):
                lista_de_paquetes.append(nombre_de_paquete)
        if len(lista_de_paquetes)==0:
            print("No se encontro ningun paquete")
            #iniciar descargas
        else:
            print("Se encontraron los siguientes paquetes ")
            for paquete in lista_de_paquetes:
                print(paquete)
def verificando_existencia_de_archivo(ruta_de_archivo_con_links):
    try:
        open(ruta_de_archivo_con_links,"r")
        print("El archivo "+ruta_de_archivo_con_links+" se encontro")
    except FileNotFoundError:
        print("no existe el archivo con los links de descargas")