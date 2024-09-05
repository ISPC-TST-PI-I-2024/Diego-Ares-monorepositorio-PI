# Listas, Tuplas y Conjuntos

Este documento proporciona una guía sobre cómo utilizar listas, tuplas y conjuntos en Python.

## Listas

Las listas son colecciones ordenadas de elementos que son mutables.

```python
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
```

### Operaciones con Listas
Las listas soportan varias operaciones, como agregar, eliminar y modificar elementos.

```python
mi_lista.append(6)  # Agregar
mi_lista.remove(2)  # Eliminar
mi_lista[0] = 10    # Modificar
print(mi_lista)
```

## Tuplas
Las tuplas son colecciones ordenadas de elementos que son inmutables.

```python
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
```
### Operaciones con Tuplas
Aunque las tuplas son inmutables, puedes realizar algunas operaciones como acceder a elementos y desempaquetar.

```python
print(mi_tupla[0])  # Acceder a elementos
a, b, c, d, e = mi_tupla  # Desempaquetar
print(a, b, c, d, e)
```

## Conjuntos
Los conjuntos son colecciones desordenadas de elementos únicos.

```python
mi_set = {1, 2, 3, 4, 5}
print(mi_set)
```

### Operaciones con Conjuntos
Los conjuntos soportan varias operaciones, como agregar, eliminar y realizar operaciones de conjuntos (unión, intersección, diferencia).

```python
mi_set.add(6)       # Agregar
mi_set.remove(3)    # Eliminar
otro_set = {4, 5, 6, 7}
print(mi_set | otro_set)  # Unión
print(mi_set & otro_set)  # Intersección
print(mi_set - otro_set)  # Diferencia
```

## Ejercicios
1. Crea una lista con los números del 1 al 10, luego agrega el número 11 y elimina el número 5. Imprime la lista resultante.
2. Crea una tupla con los días de la semana y desempaquétala en variables individuales. Imprime cada día por separado.
3. Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Realiza las operaciones de unión, intersección y diferencia entre ambos conjuntos. Imprime los resultados.