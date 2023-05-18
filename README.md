# Guía para instalar el driver(RTL8188FTV) en Raspbian

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


## 1.En la computadora con internet

1. Se descarga el repositorio con el driver:

```sh
git clone https://github.com/kelebek333/rtl8188fu/
```

2. Se pasa esta carpeta actual a una memoria USB

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
	Esto descargara los paquetes necesarios en la carpeta "Descagas_de_paquetes"

5. Se mueven la carpeta rtl8188fu-arm (esta se genero al realizar el paso uno)
```sh
mv rtl** Descagas_de_paquetes
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

### Si existe cualquier problema no dudes en crear un issue

