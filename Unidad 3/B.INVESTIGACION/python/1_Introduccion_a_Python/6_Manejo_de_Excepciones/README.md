# Manejo de Excepciones

Este documento proporciona una guía sobre cómo manejar excepciones en Python.

## Introducción a las Excepciones

Las excepciones son errores que ocurren durante la ejecución de un programa. En Python, se manejan utilizando bloques `try-except`.

```python
try:
    # Código que puede causar una excepción
    x = 1 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre una excepción
    print("No se puede dividir por cero")
```

## Bloques try-except
Puedes usar múltiples cláusulas except para manejar diferentes tipos de excepciones.

```python
try:
    x = int("hola")
except ValueError:
    print("No se puede convertir una cadena a entero")
```

## Cláusula else y finally
La cláusula else se ejecuta si no ocurre ninguna excepción. La cláusula finally se ejecuta siempre, ocurra o no una excepción.

```python
try:
    x = 1 / 1
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("La división fue exitosa")
finally:
    print("Esto se ejecuta siempre")
```

## Levantando Excepciones
Puedes usar la palabra clave raise para levantar una excepción.

```python
def verificar_edad(edad):
    if edad < 18:
        raise ValueError("La edad debe ser mayor o igual a 18")
    return True

try:
    verificar_edad(17)
except ValueError as e:
    print(e)
```

## Excepciones Personalizadas
Puedes definir tus propias excepciones personalizadas heredando de la clase Exception.

```python
class EdadInvalidaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 18:
        raise EdadInvalidaError("La edad debe ser mayor o igual a 18")
    return True

try:
    verificar_edad(17)
except EdadInvalidaError as e:
    print(e)
```

## Ejercicios
1. Escribe un programa que solicite al usuario ingresar dos números y maneje la excepción de división por cero.
2. Escribe un programa que convierta una cadena a entero y maneje la excepción correspondiente si la conversión falla.
3. Crea una función que levante una excepción si un número ingresado no está en el rango de 1 a 10.
4. Define una excepción personalizada y úsala en una función para validar la entrada del usuario.  

