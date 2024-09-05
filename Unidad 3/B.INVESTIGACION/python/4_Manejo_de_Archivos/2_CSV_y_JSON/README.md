# Manejo de Archivos CSV y JSON

Este documento proporciona una guía sobre cómo leer y escribir archivos CSV y JSON en Python.

## Introducción a los Archivos CSV y JSON

CSV (Comma-Separated Values) y JSON (JavaScript Object Notation) son formatos de archivo ampliamente utilizados para almacenar y transferir datos estructurados.

## Lectura y Escritura de Archivos CSV

Para trabajar con archivos CSV en Python, se utiliza el módulo `csv`.

### Lectura de Archivos CSV

```python
import csv

# Leer un archivo CSV
with open('datos.csv', mode='r') as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

# Leer un archivo CSV con encabezados
with open('datos.csv', mode='r') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)
```

### Escritura de Archivos CSV
```python
import csv

# Escribir en un archivo CSV
with open('datos.csv', mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Nombre', 'Edad', 'Ciudad'])
    escritor.writerow(['Alice', 30, 'Madrid'])
    escritor.writerow(['Bob', 25, 'Barcelona'])

# Escribir en un archivo CSV con encabezados
with open('datos.csv', mode='w', newline='') as archivo:
    campos = ['Nombre', 'Edad', 'Ciudad']
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerow({'Nombre': 'Alice', 'Edad': 30, 'Ciudad': 'Madrid'})
    escritor.writerow({'Nombre': 'Bob', 'Edad': 25, 'Ciudad': 'Barcelona'})
```

## Lectura y Escritura de Archivos JSON
Para trabajar con archivos JSON en Python, se utiliza el módulo json.

### Lectura de Archivos JSON
```python
import json

# Leer un archivo JSON
with open('datos.json', 'r') as archivo:
    datos = json.load(archivo)
    print(datos)
```

### Escritura de Archivos JSON
```python
import json

# Escribir en un archivo JSON
datos = {
    'Nombre': 'Alice',
    'Edad': 30,
    'Ciudad': 'Madrid'
}

with open('datos.json', 'w') as archivo:
    json.dump(datos, archivo, indent=4)
```

## Ejercicios
1. Escribe un programa que lea un archivo CSV y convierta su contenido en una lista de diccionarios.
2. Crea un archivo JSON que contenga una lista de productos, donde cada producto tiene nombre, precio y cantidad. Luego, escribe un programa que lea este archivo y calcule el valor total del inventario.
3. Escribe un programa que convierta el contenido de un archivo JSON en un archivo CSV.
4. Escribe un programa que lea un archivo CSV con datos de ventas y genere un resumen en un archivo JSON con el total de ventas por producto.
