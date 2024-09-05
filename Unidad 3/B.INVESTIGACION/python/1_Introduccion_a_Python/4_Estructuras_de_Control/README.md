# Estructuras de Control

Este documento proporciona una guía sobre cómo utilizar las estructuras de control en Python, incluyendo condicionales, bucles y control de flujo.

## Condicionales

Los condicionales se utilizan para ejecutar código basado en una condición.

```python
a = 10
b = 20

if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")
```

## Bucles
Los bucles permiten ejecutar repetidamente un bloque de código mientras se cumpla una condición.

### Bucle for
El bucle for itera sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena).

```python
for i in range(5):
    print("Iteración:", i)
```
### Bucle while
El bucle while repite un bloque de código mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

## Control de Flujo
El control de flujo altera la ejecución normal de un bucle.

### Break
La declaración break termina el bucle actual.

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Continue
La declaración continue omite la iteración actual y continúa con la siguiente iteración del bucle.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

### Pass
La declaración pass no hace nada. Se utiliza como un marcador de posición.

```python
for i in range(5):
    if i == 3:
        pass  # El pass no hace nada
    print(i)
```

## Ejercicios
1. Escribe un programa que solicite al usuario ingresar dos números y luego imprima cuál de los dos números es mayor.
2. Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
3. Escribe un programa que utilice un bucle while para imprimir los números del 10 al 1 en orden descendente.
4. Escribe un programa que utilice un bucle for para imprimir los números del 1 al 10, pero se detenga si encuentra el número 7.
5. Escribe un programa que utilice un bucle for para imprimir todos los números del 1 al 10, excepto los múltiplos de 3.
6. Escribe un programa que utilice un bucle for para iterar sobre los números del 1 al 5 y use pass para el número 3.
