# Funciones y Módulos

Este documento proporciona una guía sobre cómo declarar y usar funciones en Python, así como sobre cómo organizar el código en módulos.

## Declaración y Uso de Funciones

Las funciones se utilizan para organizar el código en bloques reutilizables.

```python
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Mundo"))
```
## Parámetros y Argumentos
Puedes definir funciones con múltiples parámetros y llamarlas con argumentos.

```python
def sumar(a, b):
    return a + b

print(sumar(3, 5))
```

## Funciones Lambda
Las funciones lambda son funciones pequeñas y anónimas definidas con la palabra clave lambda.

```python
suma = lambda a, b: a + b
print(suma(3, 5))
```

## Módulos y Paquetes
Puedes organizar el código en módulos y paquetes para mejorar la estructura y la reutilización.

### Creación y Uso de Módulos
Un módulo es un archivo que contiene definiciones y declaraciones de Python.

```python
# archivo: mi_modulo.py

def saludar(nombre):
    return f"Hola, {nombre}"
```

Puedes importar y usar un módulo en otro archivo.

```python
# archivo: main.py

import mi_modulo

print(mi_modulo.saludar("Mundo"))
```

### Organización de Paquetes
Un paquete es una colección de módulos organizados en un directorio.

```markdown
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
```
Puedes importar y usar módulos de un paquete.

```python
# archivo: main.py

from mi_paquete import modulo1

print(modulo1.saludar("Mundo"))
```

## Ejercicios
1. Escribe una función que reciba una lista de números y devuelva la suma de todos los números.
2. Escribe una función lambda que reciba dos números y devuelva su producto.
3. Crea un módulo con una función que convierta grados Celsius a Fahrenheit y úsalo en otro archivo.
4. Organiza un paquete con dos módulos: uno que contenga funciones matemáticas y otro que contenga funciones de cadenas. Usa ambos módulos en un script principal.