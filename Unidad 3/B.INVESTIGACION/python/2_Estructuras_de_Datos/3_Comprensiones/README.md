# Comprensiones

Este documento proporciona una guía sobre cómo utilizar las comprensiones en Python.

## Comprensiones de Listas

Las comprensiones de listas proporcionan una forma concisa de crear listas.

```python
mi_lista = [x for x in range(10)]
print(mi_lista)
```

## Comprensiones de Diccionarios
Las comprensiones de diccionarios permiten crear diccionarios de manera concisa.

```python
mi_diccionario = {x: x**2 for x in range(10)}
print(mi_diccionario)
```

## Comprensiones de Conjuntos
Las comprensiones de conjuntos proporcionan una forma concisa de crear conjuntos.

```python
mi_set = {x for x in range(10)}
print(mi_set)
```

## Comprensiones Anidadas
Las comprensiones anidadas permiten crear estructuras de datos más complejas.

```python
matriz = [[x for x in range(3)] for y in range(3)]
print(matriz)
```

## Ejercicios
1. Crea una lista de los cuadrados de los números del 1 al 10 usando una comprensión de listas.
2. Crea un diccionario que contenga los números del 1 al 5 como claves y sus respectivos cubos como valores usando una comprensión de diccionarios.
3. Crea un conjunto que contenga los números pares del 1 al 20 usando una comprensión de conjuntos.
4. Crea una matriz de 3x3 que contenga el número de fila en cada posición usando una comprensión anidada.
