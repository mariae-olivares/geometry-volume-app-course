# Calculadora de volúmenes

## Descripción del proyecto
Este proyecto consiste en una aplicación en Python para calcular el volumen de diversas figuras geométricas. En específico, se implementa el cálculo del volumen para: cajas, conos, cilindros y esferas. Además de la documentación completa para los cálculos ya mencionados, el proyecto cuenta con pruebas unitarias para cada figura geométrica utilizando pytest, con el fin de verificar la correcta funcionalidad de cada función.

## Estructura del Proyecto
### geometry-volume-app-course/  
#### |-- geometry/  
| |-- init.py  
| |-- box.py # Cálculo de volumen de caja  
| |-- cone.py # Cálculo de volumen de cono  
| |-- cylinder.py # Cálculo de volumen de cilindro  
| |-- sphere.py # Cálculo de volumen de esfera  
| |-- main.py  
#### |-- tests/   
| |-- init.py  
| |-- test_box.py # Pruebas para box.py  
| |-- test_cone.py # Pruebas para cone.py  
| |-- test_cylinder.py # Pruebas para cylinder.py  
| |-- test_sphere.py # Pruebas para sphere.py  
#### |-- requirements.txt   
#### |-- README.md  
#### |-- .gitignore

## Cómo ejecutar main.py
1. Después de realizar el fork a tu cuenta de GitHub, clona el repositorio en tu computadora:  
_git clone <link_del_repositorio>_  
  Para obtener el link, entra a tu repositorio en GitHub y cópialo desde la sección Code.    
2. Instala las dependencias del proyecto:  
_pip install -r requirements.txt_  
3. Ejecuta el archivo principal:  
_python geometry/main.py_  
4. Sigue las instrucciones del menú en la terminal para calcular los volúmenes de las diferentes figuras geométricas o para salir del programa.

## Cómo ejecutar las pruebas
Puedes ejecutar las pruebas unitarias de manera individual con los siguientes comandos:  

_pytest tests/test_box.py_  -> Caja  
_pytest tests/test_cone.py_  -> Cono  
_pytest tests/test_cylinder.py_  -> Cilindro  
_pytest tests/test_sphere.py_  -> Esfera

## Dependencias
- Python
- Pytest
