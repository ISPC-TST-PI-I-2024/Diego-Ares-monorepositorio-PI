# Módulos en Python

Este documento proporciona una guía sobre cómo crear y utilizar módulos en Python.

## Introducción a los Módulos

Un módulo es un archivo que contiene definiciones y sentencias de Python. Los módulos ayudan a organizar y reutilizar el código.

## Creación de un Módulo

Para crear un módulo, simplemente guarda el código en un archivo con extensión `.py`.

```python
# archivo: mi_modulo.py

def saludar(nombre):
    return f"Hola, {nombre}"

def despedir(nombre):
    return f"Adiós, {nombre}"
```

## Importación de Módulos
Puedes importar un módulo en otro archivo utilizando la palabra clave import.

```python
# archivo: uso_modulo.py

import mi_modulo

print(mi_modulo.saludar("Alice"))
print(mi_modulo.despedir("Bob"))
```
### También puedes importar funciones o variables específicas de un módulo.

```python
# archivo: uso_modulo.py

from mi_modulo import saludar, despedir

print(saludar("Alice"))
print(despedir("Bob"))
```

## Uso de la Función dir()
La función dir() devuelve una lista de los nombres definidos en un módulo.

```python
import mi_modulo

print(dir(mi_modulo))
```

## Módulos Incorporados
Python viene con una biblioteca estándar de módulos incorporados que puedes usar.

```python
import math

print(math.sqrt(16))
```

## Módulos de Terceros
Puedes instalar módulos de terceros utilizando pip y luego importarlos en tu código.

```sh
pip install requests
```
```python
import requests

respuesta = requests.get("https://api.github.com")
print(respuesta.status_code)
```

## Ejercicios
1. Crea un módulo llamado matematica.py que contenga funciones para sumar, restar, multiplicar y dividir dos números. Luego, escribe un programa que importe este módulo y utilice sus funciones.
2. Crea un módulo llamado cadena.py que contenga funciones para convertir una cadena a mayúsculas, minúsculas y capitalizarla. Luego, escribe un programa que importe este módulo y utilice sus funciones.
3. Investiga sobre un módulo incorporado en Python (por ejemplo, datetime, random, os) y escribe un programa que utilice sus funcionalidades.
4. Instala un módulo de terceros (por ejemplo, numpy, pandas, requests) y escribe un programa que utilice sus funcionalidades.
