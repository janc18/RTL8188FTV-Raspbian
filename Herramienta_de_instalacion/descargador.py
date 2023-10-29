"""
Aqui se diseña una funcion para la descarga de los paquetes .deb
ademas de conocer si ya fueron previamente descargados los paquetes
"""
import requests
import os
import shutil
import subprocess
import mostrar_informacion as sw
import hashlib

ruta_de_archivo_con_links="archivos_links.txt"
ruta_de_carpeta_de_descargas="Descargas_de_paquetes"
url_repositorio_git_driver="https://github.com/kelebek333/rtl8188fu"

def descargar_archivos_deb_con_requests(matriz_de_links):
    print("Estos son los paquetes que se descargaran")
    for paquetes in matriz_de_links:
        print(paquetes[1])

    for paquetes in matriz_de_links:
        nombre_archivo=paquetes[1]
        archivo=requests.get(paquetes[0])
        open(os.getcwd()+"/"+nombre_archivo,"wb").write(archivo.content)
        print("Descarga de paquete ",nombre_archivo," completa",)

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
        print(sw.VERDE+"Carpeta de Descarga de paquetes encontrada"+sw.NORMAL)
        print(sw.AZUL+"Buscando paquetes deb"+sw.NORMAL)
        lista_de_paquetes=[]
        for nombre_de_paquete in os.listdir(carpeta_paquetes_deb):
            if nombre_de_paquete.endswith('.deb'):
                lista_de_paquetes.append(nombre_de_paquete)
        if len(lista_de_paquetes)==0:
            print(sw.ROJO+"No se encontro ningun paquete"+sw.NORMAL)
            return False
        else:
            print(sw.AZUL+sw.BOLD+"Se encontraron los siguientes paquetes "+sw.NORMAL)
            for paquete in lista_de_paquetes:
                print(sw.AMARILLO+paquete+sw.NORMAL)
            return lista_de_paquetes


def verificando_existencia_de_archivo(ruta_de_archivos,mensaje_error):
    try:
        open(ruta_de_archivos,"r")
        return True
    except FileNotFoundError:
        print(sw.ROJO+mensaje_error+sw.NORMAL)
        return False

def descargar_repositorio_git(url,status):
    git_presente=status["existe_git"]
    if git_presente:
        print(sw.AZUL+sw.BOLD+"Descargando repositorio de driver"+sw.NORMAL)
        parametros_git=["git","clone",url]
        subprocess.run(parametros_git)
        print(sw.VERDE+"Descarga completa"+sw.NORMAL)
    else:
        print(sw.ROJO+"No se encontro git\nCerrando script"+sw.NORMAL)
        exit()

def existe_repositorio_git_driver():
    try:
        os.makedirs("rtl8188fu",exist_ok=False)
        print(sw.ROJO+"No se encontro repositorio con el driver"+sw.NORMAL)
        os.rmdir("rtl8188fu")
        return False
    except FileExistsError:
        print(sw.VERDE+"El repositorio ya se encuentra descargado"+sw.NORMAL)
        return True

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
        return lista_formateada
    except FileNotFoundError:
        print("No se encontro el archivo")

def verificando_integridad_sha256(lista_formateada):
    sha256_paquete_txt=""
    lista_paquete_corrupto=[]
    for paquete in lista_formateada:
        ruta_de_archivo=os.getcwd()+"/"+ruta_de_carpeta_de_descargas+"/"+paquete[1]
        print("Verificando el SUM256 del paquete: " + sw.BOLD + paquete[1] + sw.NORMAL,end='')
        sha256_paquete_txt=paquete[3]
        sha256_paquete_txt=sha256_paquete_txt.replace("SHA256:","")
        if verificando_existencia_de_archivo(ruta_de_archivo," No se encontro el paquete: "+paquete[1]):
            if sha256_paquete_txt==comparar_sha256(ruta_de_archivo):
                print(sw.VERDE + " OK"+sw.NORMAL)
            else:
                print(sw.ROJO+" ERROR"+sw.NORMAL)
                lista_paquete_corrupto.append(paquete)           
        else:
            lista_paquete_corrupto.append(paquete)           
    return lista_paquete_corrupto

def eliminar_paquetes_deb_corruptos(lista_formateada):
    #os.remove
    for paquete in lista_formateada:
        ruta_de_paquete=os.getcwd() + "/"+ruta_de_carpeta_de_descargas + "/" + paquete[1]
        if verificando_existencia_de_archivo(ruta_de_paquete,"EL paquete " + paquete[1] + " ya se encuentra eliminado"):
            os.remove(ruta_de_paquete)
            print(sw.AMARILLO + sw.BOLD + "Paquete corrupto eliminado: "+paquete[1] + sw.NORMAL)