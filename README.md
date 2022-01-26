# Proyecto03-EsqShamir

*Aplicación en la línea de comandos para cifrar o descifrar archivos utilizando el esquema de secreto compartido de Shamir.*

### Prerequisitos

-  Python3
-  PyPI - hashlib, getpass, pycryptodome

Asegúrese de de tener `python3` y `pip` en su computadora:

```sh
$ sudo apt-get install python3-pip
```

Luego, debe instalar las siguientes paqueterías:

```sh
$ pip install hashlib
```
```sh
$ pip install getpass
```
```sh
$ pip install pycryptodome
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
$ python3 src/main/myp/shamir.py c evaluaciones.txt n t archivoc.txt
```

O bien, la opción **d** para descifrar, 
* el nombre del archivo con al menos t evaluaciones del polinomio (.frg),
* el nombre del archivo con el texto cifrado (.aes).
```sh
$ python3 src/main/myp/shamir.py d evaluaciones.frg archivoc.txt.aes
```

### Ejemplo
- Cifrar
```sh
$ python3 src/main/myp/shamir.py c src/data/ev.txt 5 3 src/data/msj.txt
Contraseña: 
Se obtuvieron las evaluaciones en: src/data/ev.frg
Archivo cifrado exitosamente en: src/data/msj.txt.aes
```
- Develar
```sh
$ python3 src/main/myp/shamir.py d src/data/ev.frg src/data/msj.txt.aes
Archivo descifrado exitosamente en:  src/data/msj.txt
```

### Pruebas Unitarias

Para ejecutar los test del programa sólo debe escribir en la línea de comandos:

```sh
$ python3 -m unittest discover src/test/ -p "*.py"
```
