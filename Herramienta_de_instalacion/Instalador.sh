#!/bin/bash
#Instalación de todos los paquetes necesarios .deb
sudo dpkg -i Descargas_de_paquetes/**.deb
#Hacer checkout al ultimo commit donde tenia soporte la arquitectura arm
cd rtl8188fu
git checkout b037
git checkout arm
cd ..
#Instalación del driver
sudo ln -s /lib/modules/$(uname -r)/build/arch/arm /lib/modules/$(uname -r)/build/arch/armv7l
sudo dkms add ./rtl8188fu
sudo dkms build rtl8188fu/1.0
sudo dkms install rtl8188fu/1.0
sudo cp ./rtl8188fu-arm/firmware/rtl8188fufw.bin /lib/firmware/rtlwifi/
sudo mkdir -p /etc/modprobe.d/
sudo touch /etc/modprobe.d/rtl8188fu.conf
echo "options rtl8188fu rtw_power_mgnt=0 rtw_enusbss=0" | sudo tee /etc/modprobe.d/rtl8188fu.conf
echo 'alias usb:v0BDApF179d*dc*dsc*dp*icFFiscFFipFFin* rtl8188fu' | sudo tee /etc/modprobe.d/r8188eu-blacklist.conf

