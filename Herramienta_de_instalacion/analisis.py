"""
Despues de recabar toda la informacion ejecutada en el modulo de mostrar información esta genera una lista
con un resumen de datos como: conexion de internet, arquitectura, y depencias encontradas
"""


"""
---ARM-----
1.comprobar que la version del kernel sea compatible con el del driver
2.obtener las uris de los paquetes generando los archivos
---PC------
1.comprobar conexion a internet y depencia (git)
2.descargar los paquetes en base en el archivo generado en la raspberry con los links de los paquetes en el caso de que no se descargaron previamente
3.verificar que los paquetes hayan sidos descargados
4.descargar el repositorio del driver con git clone
5.hacer checkout al ultimo commit con soporte a la version arm
---ARM-----
1.instalar los paquetes deb previamentes descargados en la pc
2.Ejecutar las instrucciones para la instalacion de la version arm
"""


import mostrar_informacion as st #st= status

def generar_txt_con_uris_de_paquetes(lista_resumen):#Esta funcion solo se debe de ejecutar en el dispositivo con arquitectura ARM
    arquitectura_arm=lista_resumen[0]
    kernel_compatible=lista_resumen[1]
    cuenta_con_apt=lista_resumen[3]
    existe_el_archivo_con_links=lista_resumen[6]
    mensajes_de_errores=[
        "La arquitectura no es ARM",
        "La versión del Kernel no es compatible con el driver",
        "No cuenta con el paquete apt",
        "Ya existe el archivo de texto con los links de los paquetes a descargar",
    ]
    mascara_booleana_de_resumen=[
        arquitectura_arm,
        kernel_compatible,
        cuenta_con_apt,
        existe_el_archivo_con_links
    ]
    

    if arquitectura_arm and kernel_compatible and cuenta_con_apt and not existe_el_archivo_con_links:
        st.obtener_links_de_descargas
    elif  arquitectura_arm and kernel_compatible and cuenta_con_apt and existe_el_archivo_con_links:
        generar_links_de_descargas=input("Ya se cuenta con el archivo de links, quieres usar ese archivo o generar uno nuevo\n[s/S] [n/N]")
        if generar_links_de_descargas in ("S","s"):
            st.main.obtener_links_de_descargas
        elif generar_links_de_descargas in ("N","n"):
            print("Usando archivo antiguo")
        else:
            print("Opción incorrecta")
    else:
        for error in range(len(mensajes_de_errores)):
            if mascara_booleana_de_resumen[error]==False:
                print(st.ROJO,end="")
                print(mensajes_de_errores[error])
                print(st.NORMAL,end="")

def descargar_todos_los_componentes_necesarios(lista_resumen):
    if lista_resumen[4]==False:
        print("No se cuenta con internet para realizar el proceso")
