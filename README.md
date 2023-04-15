# SDC-TP2

# Introduccion

En el presente trabajo práctico, se diseña e implementa una calculadora de cotizacion de criptomonedas. Por un lado, se obtiene la cotizacion de las criptomonedas a través de la API que provee la página www.alphavantage.co y luego los datos son entregados a un programa en C, el cuál convoca rutinas en assembler para realizar los calculos de conversion. El resultado son las cotizaciones en pesos, dólares y euros.

# Estructura del proyecto

Se utilizaron 3 lenguajes de programación: python, C y assembler. Las carpetas [inc](https://github.com/ginos1998/SDC-TP2/tree/main/inc) y [src](https://github.com/ginos1998/SDC-TP2/tree/main/src) contienen el desarrollo en C y assembler y, en la carpeta [api](https://github.com/ginos1998/SDC-TP2/tree/main/api) se encuentra el código en python.

## python

En python se creo un simple programa que le consulta al usuario que valor de criptomoneda desea convertir. Las opciones son [BTC](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT) (bitcoin) y [ETH](https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=ETH&to_currency=USD&apikey=9N3E66AEYSMKXXHT) (etherum). Luego, según la opción elegida, consulta a la API y obtiene el valor. Por último, obtenemos los valores de cotizacion del peso, dolar y euro para enviarselos al programa en C, junto con la moneda elegida por el usuario.

## C

El programa en C también es muy sencillo; recibe los valores mencionados anteriormente y se comunica con assembler para realizar la conversión. Una vez obtenido el resultado, lo imprime en pantalla.

## Assembler

El código de assembler recibe 2 floats como parámetro. Una vez ingresado a la rutina se crea el stack frame con el comando “enter”, al no haber variables locales no se requiere reservar más espacio en la pila. Una vez creado el stack frame se puede referenciar los parámetros usando el registro ebp.

[ebp + 8] = primer parámetro
[ebp + 12] = segundo parámetro

La tarea a ejecutar es muy simple, solamente se coloca el primer parámetro en el registro para operaciones de punto flotante y luego se lo multiplica por el segundo parámetro.

Utilizando el comando “leave” restauramos el registro ebp y salimos del stack frame. Se retorna el valor en el registro de punto flotante por convención de llamada al ejecutar “return”

# Guia de usuario

1. Para descargar el repositorio ejecutamos

```bash
git clone https://github.com/ginos1998/SDC-TP2.git
```
2. Compilar programa en C y assembler, abrimos una terminal en la carpeta clonada y ejecutamos

```bash
make
```
3. En la misma terminal que abrimos, nos movemos a la carpeta api
``` bash
cd api
```
5. Ejecutamos el programa en python
```bash
python3 crypto_calc.py
```

### IMPORTANTE

Para python, es necesario instalar la libreria _requests_

```bash
pip install requests
```

Para C, necesitamos el compilador _gcc_

```bash
sudo apt install build-essential
```

Para assembler necesitamos el compilador nasm

```bash
sudo apt-get install nasm
```
# Demo

![texto de prueba](/img/how_to_run_py.png)
