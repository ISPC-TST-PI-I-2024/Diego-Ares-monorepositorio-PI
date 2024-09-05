# Diccionarios

Este documento proporciona una guía sobre cómo utilizar diccionarios en Python.

## Diccionarios

Los diccionarios son colecciones desordenadas de pares clave-valor.

```python
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
print(mi_diccionario)
```

## Operaciones con Diccionarios
Puedes realizar varias operaciones con diccionarios, como agregar, eliminar y modificar elementos.

```python
mi_diccionario['d'] = 4  # Agregar
del mi_diccionario['b']  # Eliminar
mi_diccionario['a'] = 10  # Modificar
print(mi_diccionario)
```

## Métodos de Diccionarios
Los diccionarios tienen varios métodos útiles, como keys(), values(), items(), get(), pop(), update(), etc.

```python
llaves = mi_diccionario.keys()  # Obtener todas las claves
valores = mi_diccionario.values()  # Obtener todos los valores
items = mi_diccionario.items()  # Obtener todos los pares clave-valor
valor = mi_diccionario.get('a')  # Obtener el valor de una clave
mi_diccionario.pop('c')  # Eliminar un elemento y devolver su valor
mi_diccionario.update({'e': 5})  # Actualizar el diccionario con otro diccionario
print(llaves, valores, items, valor, mi_diccionario)
```

## Iteración sobre Diccionarios
Puedes iterar sobre las claves, valores y pares clave-valor de un diccionario.

```python
for clave in mi_diccionario:
    print(clave, mi_diccionario[clave])  # Iterar sobre claves

for valor in mi_diccionario.values():
    print(valor)  # Iterar sobre valores

for clave, valor en mi_diccionario.items():
    print(clave, valor)  # Iterar sobre pares clave-valor
```

## Ejercicios
1. Crea un diccionario con los nombres de los meses como claves y la cantidad de días como valores. Luego, agrega una clave para un mes ficticio y elimina la clave correspondiente a febrero.
2. Escribe un programa que solicite al usuario ingresar un nombre y una edad, y luego almacene esta información en un diccionario. Repite el proceso para varios usuarios y finalmente imprime el diccionario completo.
3. Crea un diccionario que contenga productos y sus precios. Luego, incrementa el precio de cada producto en un 10% y muestra el diccionario actualizado.
