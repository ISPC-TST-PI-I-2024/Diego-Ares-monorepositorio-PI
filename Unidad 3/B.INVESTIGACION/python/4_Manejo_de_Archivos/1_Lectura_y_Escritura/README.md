# Lectura y Escritura de Archivos

Este documento proporciona una guía sobre cómo leer y escribir archivos en Python.

## Introducción a la Lectura y Escritura de Archivos

Python proporciona funciones integradas para leer y escribir archivos. Trabajar con archivos es esencial para la persistencia de datos.

## Lectura de Archivos

Para leer un archivo, se utiliza la función `open()` en modo lectura (`'r'`).

```python
# Leer un archivo completo
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea
with open('archivo.txt', 'r') as archivo:
    for linea in archivo:
        print(linea.strip())
```

## Escritura de Archivos
Para escribir en un archivo, se utiliza la función open() en modo escritura ('w'). Esto sobrescribe el contenido existente.

```python
# Escribir en un archivo
with open('archivo.txt', 'w') as archivo:
    archivo.write('Hola, mundo!')
```

## Uso del Modo Append
Para agregar contenido a un archivo sin sobrescribir el existente, se utiliza el modo append ('a').

```python
# Agregar contenido a un archivo
with open('archivo.txt', 'a') as archivo:
    archivo.write('\nNueva línea agregada')
```

## Gestión de Archivos con el Bloque with
El bloque with asegura que el archivo se cierre correctamente después de que se complete el bloque de código.

```python
# Uso del bloque with para manejar archivos
with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
```

## Lectura y Escritura de Archivos Binarios
Para trabajar con archivos binarios, se utilizan los modos 'rb' para lectura y 'wb' para escritura.

```python
# Leer un archivo binario
with open('imagen.jpg', 'rb') as archivo:
    contenido = archivo.read()

# Escribir en un archivo binario
with open('imagen_copia.jpg', 'wb') as archivo:
    archivo.write(contenido)
```

## Ejercicios
1. Escribe un programa que lea un archivo de texto y cuente el número de líneas, palabras y caracteres.
2. Crea un archivo de texto y escribe las tablas de multiplicar del 1 al 10.
3. Escribe un programa que lea un archivo binario y cree una copia del mismo.
4. Modifica un archivo de texto existente para agregarle una nueva línea al final sin sobrescribir el contenido existente.
