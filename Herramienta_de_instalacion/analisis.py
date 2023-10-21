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
2.descargar los paquetes en base en el archivo generado en la raspberry con los links de los paquetes
3.verificar que los paquetes hayan sidos descargados
4.descargar el repositorio del driver con git clone
5.hacer checkout al ultimo commit con soporte a la version arm
---ARM-----
1.instalar los paquetes deb previamentes descargados en la pc
2.Ejecutar las instrucciones para la instalacion de la version arm
"""


import mostrar_informacion as st #st= status

def analisis(lista_resumen):
    st.mostrar_informacion_host(lista_resumen)