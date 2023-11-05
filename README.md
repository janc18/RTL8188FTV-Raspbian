# Guía para instalar el driver(RTL8188FTV) en Raspbian

## Status(Estado actual del proyecto)

![status](https://badgen.net/badge/Estado/testing/orange)
*Por el momento tengo problemas con obtener la version de raspberrypi-kernel-headers correspondiente con el kernel instalado,
ya que por alguna razon se descarga la vesion 6.0, probare instalando la version mas reciente a de Raspbian*

## Pasos para instalar una versión de Raspbian compatible al final

## Nota: Para usar este driver, como es mencionado en el repositorio del driver, este solo tiene soporte para el kernel 4.15.x ~ 6.0.x

Ejecuta el siguiente script de python en el siguiente orden:

*Ejemplo de ejecucion de script de python*
En la siguiente ruta:_RTL8188FTV-Raspbian/Herramienta_de_instalacion/_

```sh 
python main.py
```
*Recomiendo ejecutar este script en la memoria usb*

1. Raspberry pi de arquitectura arm

2. Pc con acceso a internet

## Instalacion del driver 

1. Se monta la memoria en la Raspberry pi

2. Se navega al repositorio (RTL8188FTV-Raspbian/Herramienta_de_instalacion)

3. Se le da permisos de ejecucion al instalador

```sh
chmod +x Instalador.sh
./Instalador.sh
```
## Pasos para instalar un kernel compatible con el driver de wifi

**Advertencia: Ten en cuenta que no se podran aplicar parches de seguridad del kernel**

1. Nos dirigimos a la siguiente [URL](https://www.raspberrypi.com/software/operating-systems/) 

![Screenshot_20230518_194258](https://github.com/janc18/RTL8188FTV-Raspbian/assets/43817922/ee038930-51ab-4601-97f1-f7abe256b03d)

Descargamos la versión que necesitemos en mi caso yo elegí la version Lite
Elegimos la opcion **archive**

2. Buscamos la versión mas reciente del kernel anterior a la 6.0.x

![Screenshot_20230518_194426](https://github.com/janc18/RTL8188FTV-Raspbian/assets/43817922/a564f8fc-46e1-4e9e-ae9e-f70582963a41)

3. Descargamos la imagen iso

![Screenshot_20230518_194633](https://github.com/janc18/RTL8188FTV-Raspbian/assets/43817922/19bc0501-cf8e-4b89-8a9f-80d70f3097f3)

Si vemos el archivo .info que se encuentra al final se vera lo siguiente

![Screenshot_20230518_194711](https://github.com/janc18/RTL8188FTV-Raspbian/assets/43817922/e227ed7a-93ab-48a6-ae5c-fcc7c31e0080)

Ahí podemos comprobar que el campo **Uname string** se muestra que el kernel que tiene es el **5.15.84** por lo cual es compatible con el driver

4. Para que no se actualize el kernel al momento de ejecutar un upgrade, tenemos que ejecutar lo siguiente
```sh
sudo apt-mark hold raspberrypi-kernel
sudo apt-mark hold raspberrypi-kernel-headers
```

### Si existe cualquier problema no dudes en crear un Issue
