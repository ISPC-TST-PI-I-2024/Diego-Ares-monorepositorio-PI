# Sintaxis Básica

Este documento proporciona una guía sobre la sintaxis básica de Python, incluyendo operadores, expresiones, estructuras de control, y más.

## Contenidos

- Comentarios
- Variables y Tipos de Datos
- Operadores
- Estructuras de Control
- Funciones

### Comentarios

Los comentarios se usan para explicar el código y son ignorados por el intérprete de Python.

- Comentarios de una línea: Comienzan con `#`.
- Comentarios de múltiples líneas: Se delimitan con `"""` o `'''`.

```python
# Esto es un comentario de una sola línea

"""
Esto es un comentario
de múltiples líneas
"""
```

### Variables y Tipos de Datos  
Las variables se utilizan para almacenar información. Los tipos de datos comunes en Python incluyen enteros, flotantes, cadenas y booleanos.  

```python
entero = 10
flotante = 20.5
cadena = "Hola, mundo"
booleano = True
```

### Operadores  
Los operadores se utilizan para realizar operaciones en variables y valores.  

- Aritméticos: +, -, *, /, %, **, //
- Comparación: ==, !=, >, <, >=, <=
- Lógicos: and, or, not

```python
# Operadores aritméticos
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
modulo = 5 % 3
exponente = 5 ** 3
division_entera = 5 // 3
```
### Estructuras de Control  
Las estructuras de control se utilizan para decidir el flujo del programa.

- Condicionales: if, elif, else
- Bucles: for, while  

```python
# Condicional
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else:
    print("a es igual a b")

# Bucle for
for i in range(5):
    print("Iteración:", i)

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

### Funciones  
Las funciones se utilizan para organizar el código en bloques reutilizables.

```python  
def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("Mundo"))
```  

### Ejercicios  
1. Escribe un programa que solicite al usuario ingresar dos números y luego imprima la suma, resta, multiplicación y división de esos números.  
2. Escribe un programa que imprima los números del 1 al 10 utilizando un bucle for.
3. Escribe un programa que utilice un bucle while para imprimir los números del 10 al 1 en orden descendente.  
4. Escribe una función que reciba un número como parámetro y devuelva True si el número es par, y False si es impar.  
