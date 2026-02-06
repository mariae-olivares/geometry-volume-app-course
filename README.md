# geometry-volume-app-course
Calculadora de volúmenes de figuras geométricas

## Descripción del proyecto
Este proyecto consiste en una aplicación en Python para calcular el volumen de diversas figuras geométricas. En específico, se implementa el cálculo del volumen para: cajas, conos, cilindros y esferas. Además de la documentación para los cálculos ya mencionados, el proyecto cuenta con pruebas para cada figura geométrica utilizando pytest.

## Estructura del Proyecto
A continuación se muestra, a forma de diagrama, la estructura del proyecto:

### geometry-volume-app-course/  
#### |-- geometry/
Contiene la definición de cada una de las funciones para el cálculo de los volúmenes  
| |-- init.py  
| |-- box.py # Cálculo de volumen de caja  
| |-- cone.py # Cálculo de volumen de cono  
| |-- cylinder.py # Cálculo de volumen de cilindro  
| |-- sphere.py # Cálculo de volumen de esfera 
#### |-- tests/   
Contiene los archivos de prueba de cada una de las figuras  
| |-- init.py  
| |-- test_box.py # Pruebas para box.py  
| |-- test_cone.py # Pruebas para cone.py  
| |-- test_cylinder.py # Pruebas para cylinder.py  
| |-- test_sphere.py # Pruebas para sphere.py 
#### |-- .gitignore
#### |-- README.md  
#### |-- main.py
Se debe ejecutar para poder acceder a la calculadora de volúmenes  
#### |-- requirements.txt   
i
Incluye las dependencias necesarias para poder correr el programa  

## Cómo ejecutar main.py
1. Después de realizar el fork a tu cuenta de GitHub, clona el repositorio en tu computadora:  
_git clone <link_del_repositorio>_  
  Para obtener el link, entra a tu repositorio en GitHub y cópialo desde la sección Code.    
2. Abre una terminal en el directorio.
3. Ejecuta el archivo principal:  
_python main.py_  
4. Sigue las instrucciones del menú en la terminal para calcular los volúmenes de las diferentes figuras geométricas o para salir del programa.
------------------------------------------------------------------------------------------------------------------------------------------------
Ejemplo de ejecución:

$ python main.py  

=== 3D Geometry Volume Calculator ===  
1. Volume of a Cylinder  
2. Volume of a Box  
3. Volume of a Cone  
4. Volume of a Sphere  
5. Quit  
Select an option: 3  
Enter radius (m): 2  
Enter height (m): 3  
Volume of cone: 12.566 m³  

=== 3D Geometry Volume Calculator ===  
1. Volume of a Cylinder  
2. Volume of a Box  
3. Volume of a Cone  
4. Volume of a Sphere  
5. Quit  
Select an option: 5  
Catch you later, mate!  


## Cómo ejecutar las pruebas
1. Abre una terminal en el directorio.
2. Instala las dependencias del proyecto:  
_pip install -r requirements.txt_ ó _python -m pip install -r requirements.txt_ 
3. Realiza las pruebas:
- Puedes ejecutar las pruebas de manera individual con los siguientes comandos:  

_pytest tests/test_box.py_  -> Caja  
_pytest tests/test_cone.py_  -> Cono  
_pytest tests/test_cylinder.py_  -> Cilindro  
_pytest tests/test_sphere.py_  -> Esfera

- Ó, puedes ejecutar todas las pruebas con el siguiente comando:
_pytest tests_

------------------------------------------------------------------------------------------------------------------------------------------------
Ejemplo de ejecución:

$ pytest tests   
================= test session starts =================    
platform win32 -- Python 3.11.6, pytest-9.0.2, pluggy-1.6.0  
rootdir: "tu ruta del archivo"  
collected 14 items  

tests/test_box.py ...                                                                                                                                                                                        [ 21%]  
tests/test_cone.py ....                                                                                                                                                                                      [ 50%]  
tests/test_cylinder.py ....                                                                                                                                                                                  [ 78%]  
tests/test_sphere.py ...                                                                                                                                                                                     [100%]  
================= 14 passed in 0.08s =================    

## Dependencias
- Python
- Pytest (Para la realización de las pruebas se utilizó pytest-9.0.2)
