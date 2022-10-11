# Guía para instalar el driver(RTL8188FTV) en Raspbian
* Esta guía tiene como objetivo instalar el driver, pero en casos cuando no es posible conectarla
usando un cable LAN.

* Debido a que es necesario construir este [driver](https://github.com/kelebek333/rtl8188fu/tree/arm#how-to-install-for-arm-devices),
se ocupan varios paquetes como lo son:

1. dkms

2. build-essential

3. linux-headers

## Proceso a ejecutar en la computadora linux con acceso a internet
Paquetes necesarios
`sudo apt install wget git`
Darle permisos al script de descargas
`sudo chmod +x Descargas.sh`
`./Descargas.sh`
Copiar la nueva carpeta generada "DescargasDePaquetes" a una memoría USB

## Proceso a ejecutar en la Raspberry Pi
Entrar a la carpeta DescargasDePaquetes y ejecutar:
`sudo chmod +x Instalador.sh`
`./Instalador.sh`

* Ahora ya debería posible ejecutar la herramienta de Raspbian para conectarte a la red
`sudo raspi-config `System Options` -> `Wireless LAN`

