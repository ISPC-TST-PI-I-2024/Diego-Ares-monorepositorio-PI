# Paquetes en Python

Este documento proporciona una guía sobre cómo crear y utilizar paquetes en Python.

## Introducción a los Paquetes

Un paquete es una forma de estructurar el espacio de nombres del módulo de Python mediante el uso de "nombres de módulos con puntos". Un paquete es simplemente un directorio que contiene un archivo especial `__init__.py`.

## Creación de un Paquete

Para crear un paquete, organiza tus módulos en un directorio y agrega un archivo `__init__.py`.

```plaintext
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```

## Importación de Paquetes y Módulos
Puedes importar módulos desde un paquete utilizando la sintaxis de punto.

```python
# archivo: main.py

import mi_paquete.modulo1
import mi_paquete.modulo2

mi_paquete.modulo1.funcion1()
mi_paquete.modulo2.funcion2()
```

### También puedes importar funciones o variables específicas de un módulo dentro de un paquete.

```python
# archivo: main.py

from mi_paquete.modulo1 import funcion1
from mi_paquete.modulo2 import funcion2

funcion1()
funcion2()
```

## Organización de Paquetes
Puedes organizar tus paquetes en subpaquetes para una mejor modularización.

```plaintext
mi_paquete/
    __init__.py
    subpaquete1/
        __init__.py
        modulo1.py
    subpaquete2/
        __init__.py
        modulo2.py
```

## Uso del Archivo __init__.py
El archivo __init__.py se ejecuta cuando se importa un paquete y puede ser utilizado para inicializar el paquete.

```python
# archivo: mi_paquete/__init__.py

from .modulo1 import funcion1
from .modulo2 import funcion2
```

## Paquetes de Terceros
Puedes instalar paquetes de terceros utilizando pip y luego importarlos en tu código.

```sh
pip install numpy
```
```python
import numpy as np

array = np.array([1, 2, 3])
print(array)
```

## Ejercicios
1. Crea un paquete llamado calculadora con dos módulos: aritmetica.py (con funciones para sumar, restar, multiplicar y dividir) y trigonometria.py (con funciones para seno, coseno y tangente). Escribe un programa que utilice estos módulos.
2. Organiza un paquete llamado analisis_datos con subpaquetes estadistica (con funciones para media, mediana y moda) y visualizacion (con funciones para crear gráficos simples). Escribe un programa que utilice estos subpaquetes.
3. Investiga sobre un paquete de terceros en Python (por ejemplo, matplotlib, pandas, scikit-learn) y escribe un programa que utilice sus funcionalidades.
4. Crea un archivo __init__.py en un paquete de ejemplo y utiliza este archivo para inicializar algunas variables cuando el paquete se importe.
