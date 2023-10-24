# Guía para instalar el driver(RTL8188FTV) en Raspbian

## Status(Estado actual del proyecto)

![status](https://badgen.net/badge/Estado/Aun%20en%20desarrollo(python)/yellow)

## Pasos para instalar una versión de Raspbian compatible al final

## Nota: Para usar este driver, como es mencionado en el repositorio del driver, este solo tiene soporte para el kernel 4.15.x ~ 6.0.x

- Por ende, si es descargada la versión más actual de Raspbian no será posible usar este driver

## Pasos a seguir

* Esta guía tiene como objetivo instalar el driver, pero en casos cuando no es posible conectarla
usando un cable LAN.

* Debido a que es necesario construir este [driver](https://github.com/kelebek333/rtl8188fu/tree/arm#how-to-install-for-arm-devices),
se ocupan varios paquetes como lo son:

1. dkms

2. build-essential

3. linux-headers

## Depencias necesarias en la computadora con linux con acceso a internet

- Git
- Wget
- python

## 1.En la computadora con internet

1. Se descarga el repositorio con el driver:

```sh
git clone -b arm https://github.com/kelebek333/rtl8188fu rtl8188fu-arm
```
2. Se descarga este repositorio

```sh
git clone https://github.com/janc18/RTL8188FTV-Raspbian
```
3. Mueve la carpeta rtl18188fu-arm generada por el paso 1 a RLL8188FTV-Raspbian 

En el directorio donde ejecutaste el paso 1 y 2 ejecutas lo siguiente

```sh
mv rtl18188fu-arm RTL8188FTV-Raspbian
```

1. Se pasa esta carpeta actual (RTL8188FTV-Raspbian) a una memoria USB

## 2.Proceso a ejecutar en la Raspberry Pi


1. Se monta la memoria USB 

2. Ejecutar el instalador en la carpeta del repositorio (RTL8188FTV-Raspbian) 

```sh
python3.9 Instalador_python.py
```
3. Elegir la opcion r o R (opción correspondiente a la Raspberry pi)
	Se generara un archivo txt automático con las urls de los paquetes 

4. Se desmonta la memoria


## 3.Proceso a ejecutar en la computadora linux con acceso a internet

1. Se monta de nuevo la memoria

2. Se navega al repositorio (RTL8188FTV-Raspbian)

3. Ejecutar el instalador

```sh
python3.9 Instalador_python.py
```

4. Elegir la opcion p o P (opción correspondiente a la PC)
	Esto descargara los paquetes necesarios en la carpeta "Descargas_de_paquetes"

5. Se mueven la carpeta rtl8188fu-arm (esta se genero al realizar el paso uno)
```sh
mv rtl** Descargas_de_paquetes
```
6. Desmontar la memoria

## 4. Instalacion en la Raspberry pi

1. Se monta la memoria en la Raspberry pi

2. Se navega al repositorio (RTL8188FTV-Raspbian)

3. Se mueve el archivo "Instalador.sh" a la carpeta de Descagas_de_paquetes

```sh
mv Instalador.sh Descagas_de_paquetes
```

4. Se le da permisos de ejecucion al instalador

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

Mejoras de script de Python

- Detección automatica de donde se ejecuta el script Raspberry Pi o PC 
- Verificar si la PC se encuentra con internet
- Verificar al final si la instalación del driver fue correcta
- Mostrar con colores un informacion del host siempre que se ejecute
