# Proyecto03-EsqShamir

*Aplicación en la línea de comandos para cifrar o decifrar archivos utilizando el esquema de secreto compartido de Shamir.*

### Prerequisitos

-  Python3
-  PyPI - 

Asegúrese de de tener `python3` y `pip` en su computadora:

```sh
$ sudo apt-get install python3-pip
```

Luego, debe instalar las siguientes paqueterías:

```sh
$ 
```
```sh
$ pip install pycryptodomex
```
```sh
$ pip install mod
```

### Ejecutar el Programa

Para ejecutar el programa sólo debe escribir en la línea de comandos:

```sh
$ python3 src/main/myp/shamir.py
```

Seguido de la opción **c** para cifrar, 
* el nombre donde se guardará el archivo con las n evaluaciones,
* el número de avaluaciones requeridas (n > 2) 
* el mínimo número de evaluaciones para descifrar (1 < t ≤ n) 
* el nombre del archivo con el texto claro.
```sh
$ python3 src/main/myp/esteganografia.py h archivo_ocultar imagen_ocultar nombre_destino
```

O bien, la opción **d** para descifrar, 
* el nombre del archivo con al menos t evaluaciones del polinomio,
* el nombre del archivo con el texto cifrado.
```sh
$ python3 src/main/myp/esteganografia.py u imagen_develar nombre_destino
```

### Ejemplo
- Cifrar
```sh
$ python3 src/main/myp/esteganografia.py c nombre 5 3 archivo
Evaluaciones generadas:  src/data/ev.frg
Mensaje cifrado exitosamente:  src/data/ejemplo.aes
```
- Develar
```sh
$ python3 src/main/myp/esteganografia.py d evaluaciones archivo
Mensaje obtenido en:  src/data/ejemplo.txt
```

### Pruebas Unitarias

Para ejecutar los test del programa sólo debe escribir en la línea de comandos:

```sh
$ python3 -m unittest discover src/test/ -p "*.py"
```
