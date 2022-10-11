#!/bin/bash
#Creación de fichero donde se alojaran todas las descargas
mkdir DescargasDePaquetes
cd DescargasDePaquetes
#Paquete build-essential
wget http://archive.raspbian.org/raspbian/pool/main/b/build-essential/build-essential_12.9_armhf.deb
#Paqute dkms
wget http://archive.raspbian.org/raspbian/pool/main/d/dkms/dkms_2.3-2_all.deb
#Paquete raspbian-kernel 
wget https://archive.raspberrypi.org/debian/pool/main/r/raspberrypi-firmware/raspberrypi-kernel-headers_1.20220830-1_armhf.deb 
#Descarga de driver rtl8188fu obtenido de git del usuario kelebek333
git clone -b arm https://github.com/kelebek333/rtl8188fu rtl8188fu-arm
#Mueve el script instalador a la carpeta DescargasDePaquetes para que solo muevas esa carpeta
mv Instalador.sh DescargasDePaquetes/
