# Variables y Tipos de Datos

Este documento proporciona una guía sobre cómo declarar y usar variables en Python, así como sobre los diferentes tipos de datos disponibles.

## Declaración de Variables

En Python, no es necesario declarar explícitamente el tipo de una variable. El tipo se determina automáticamente cuando se le asigna un valor.

```python
mi_variable = 10  # Entero
mi_variable = "Hola"  # Cadena
mi_variable = 3.14  # Flotante
mi_variable = True  # Booleano
```

## Tipos de Datos  
Los tipos de datos básicos en Python incluyen:

- Enteros (int): Números enteros.
- Flotantes (float): Números con punto decimal.
- Cadenas (str): Texto.
- Booleanos (bool): Valores de verdad (True o False).  

```python
entero = 10
flotante = 20.5
cadena = "Hola, mundo"
booleano = True
```

## Conversión de Tipos  
Puedes convertir entre tipos de datos utilizando las funciones int(), float(), str(), etc.

```python
entero = int(20.5)  # Convertir flotante a entero
flotante = float(10)  # Convertir entero a flotante
cadena = str(10)  # Convertir entero a cadena
booleano = bool(1)  # Convertir entero a booleano  
```

## Operaciones con Variables
Puedes realizar operaciones con variables utilizando operadores aritméticos, de comparación, lógicos, etc.

```python
a = 10
b = 5

# Operaciones aritméticas
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b  

# Operaciones de comparación
igual = (a == b)
diferente = (a != b)
mayor_que = (a > b)
menor_que = (a < b)

# Operaciones lógicas
y = (a > 5 and b < 10)
o = (a > 5 or b > 10)
no = not (a > 5)
```

## Ejercicios  

1. Declara una variable de cada tipo de dato (entero, flotante, cadena y booleano) y muestra sus valores.
2. Convierte un número flotante a entero y muestra el resultado.
3. Escribe un programa que solicite al usuario ingresar su nombre y edad, y luego imprima un mensaje que incluya ambos datos.
4. Escribe un programa que evalúe si un número ingresado por el usuario es mayor que 10 y menor que 20.  

# Tipos de Datos Avanzados: Secuencias, Conjuntos y Mapas

Las secuencias son tipos de datos que consisten en elementos ordenados. Los tipos más comunes de secuencias en Python son listas, tuplas y rangos.

## Listas

Las listas son colecciones ordenadas de elementos que son mutables.

```python
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
```

## Tuplas
Las tuplas son colecciones ordenadas de elementos que son inmutables.

```python
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
```

## Rangos
Los rangos son secuencias inmutables de números enteros.

```python
mi_rango = range(1, 6)
print(list(mi_rango))
```

## Selección de Subsecuencias (Slices)
Puedes seleccionar subsecuencias de listas, tuplas y cadenas usando slices.

```python
mi_lista = [1, 2, 3, 4, 5]
print(mi_lista[1:4])
```

## Operaciones Predefinidas para Secuencias
Puedes realizar varias operaciones predefinidas en secuencias, como encontrar la longitud, el máximo, el mínimo, etc.

```python
mi_lista = [1, 2, 3, 4, 5]
print(len(mi_lista))  # Longitud
print(max(mi_lista))  # Máximo
print(min(mi_lista))  # Mínimo
```

## Conjuntos
Los conjuntos son colecciones desordenadas de elementos únicos.

### set y frozenset
Los conjuntos (set) son mutables, mientras que los conjuntos congelados (frozenset) son inmutables.

```python
mi_set = {1, 2, 3, 4, 5}
mi_frozenset = frozenset(mi_set)
print(mi_set)
print(mi_frozenset)
```

## Funciones de Actualización
Puedes actualizar conjuntos utilizando varias funciones como add(), remove(), update(), etc.

```python
mi_set = {1, 2, 3}
mi_set.add(4)
mi_set.update([5, 6])
mi_set.remove(2)
print(mi_set)
```

## Operaciones
Puedes realizar varias operaciones en conjuntos, como unión, intersección, diferencia, etc.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Unión
print(set1 & set2)  # Intersección
print(set1 - set2)  # Diferencia
```

## Condicionales
Puedes usar condicionales para verificar la pertenencia, subconjuntos, superconjuntos, etc.

```python
set1 = {1, 2, 3}
set2 = {1, 2}
print(1 in set1)  # Pertenencia
print(set2.issubset(set1))  # Subconjunto
print(set1.issuperset(set2))  # Superconjunto
```

## Mapas (Diccionarios)
Los diccionarios son colecciones desordenadas de pares clave-valor.

### Explorar Valores
Puedes explorar los valores en un diccionario usando varias técnicas.

```python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
print(mi_dict.keys())  # Llaves
print(mi_dict.values())  # Valores
print(mi_dict.items())  # Pares llave-valor
```

## Actualizar Valores
Puedes actualizar los valores en un diccionario usando varias técnicas.

```python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
mi_dict['a'] = 10
mi_dict.update({'b': 20, 'd': 4})
print(mi_dict)
```

## Objetos de Tipo Vista
Los diccionarios proporcionan vistas de objetos para llaves, valores y elementos.

```python
mi_dict = {'a': 1, 'b': 2, 'c': 3}
llaves = mi_dict.keys()
valores = mi_dict.values()
items = mi_dict.items()
print(llaves)
print(valores)
print(items)
```

## Ejercicios
### Secuencias:
1. Crea una lista de números del 1 al 10 y selecciona una subsecuencia del tercer al sexto elemento.
2. Convierte la lista anterior en una tupla y crea un rango que abarque los mismos números.
3. Encuentra el número máximo, mínimo y la longitud de la lista.

### Conjuntos:
1. Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 3 al 7. Encuentra la unión, intersección y diferencia de ambos conjuntos.
2. Añade el número 6 al primer conjunto y elimina el número 2 del mismo conjunto.
3. Verifica si el segundo conjunto es un subconjunto del primer conjunto.

### Mapas (Diccionarios):
1. Crea un diccionario con los días de la semana como claves y los nombres de los días como valores.
2. Actualiza el diccionario cambiando el valor del lunes a "Lunes".
3. Imprime todas las llaves, valores y elementos del diccionario.