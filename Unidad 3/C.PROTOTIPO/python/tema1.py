## PARTE 1 ##

# 3. Hola, Mundo
print("Hola, Mundo")

# 4. Comentarios
# Esto es un comentario de una línea

"""
Esto es un comentario
de múltiples líneas
"""

# 5. Entrada de Usuario
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}")

# 6. Cálculo Simple
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es {suma}")

# 7. Condicionales
num = float(input("Introduce un número: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# 8. Declaración de Variables
entero = 5
flotante = 5.5
cadena = "Hola"
booleano = True

print(f"Entero: {entero}, Flotante: {flotante}, Cadena: {cadena}, Booleano: {booleano}")

# 9. Conversión de Tipos
flotante = 10.7
entero = int(flotante)
flotante_convertido = float(entero)
print(f"Flotante convertido a entero: {entero}")
print(f"Entero convertido a flotante: {flotante_convertido}")

# 10. Operaciones Matemáticas
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}")

# 11. Formateo de Cadenas
nombre = "Juan"
edad = 25
print(f"Hola, mi nombre es {nombre} y tengo {edad} años")

# 12. Longitud de Cadena
cadena = input("Introduce una cadena: ")
longitud = len(cadena)
print(f"La longitud de la cadena es {longitud}")

# 13. Condicional Simple
num = int(input("Introduce un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# 14. Condicional Anidado
num = int(input("Introduce un número: "))
if 1 <= num <= 100:
    print("El número está en el rango de 1 a 100")
else:
    print("El número no está en el rango de 1 a 100")

# 15. Bucle for
for i in range(1, 11):
    print(i)

# 16. Bucle while
i = 10
while i > 0:
    print(i)
    i -= 1

# 17. Bucle con break
for i in range(1, 11):
    if i % 4 == 0:
        break
    print(i)

# 18. Bucle con continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 19. Bucle Anidado
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")

# 20. List Comprehensions
cuadrados = [i**2 for i in range(1, 11)]
print(cuadrados)

# 21. Función Simple
def cuadrado(num):
    return num ** 2

print(cuadrado(5))

# 22. Función con Múltiples Parámetros
def suma(a, b):
    return a + b

print(suma(3, 4))

# 23. Función con Valor por Defecto
def suma(a, b=5):
    return a + b

print(suma(3))
print(suma(3, 7))

# 24. Función Recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 25. Importación de Módulos
import math
print(math.sqrt(16))

# 26. Módulo Propio (Guarda esto en un archivo llamado mi_modulo.py)
def saludar(nombre):
    return f"Hola, {nombre}"

# 27. Manejo Básico de Excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# 28. Excepción Específica
try:
    num = int(input("Introduce un número: "))
except ValueError:
    print("Eso no es un número válido")

# 29. Bloques try y finally
try:
    num = int(input("Introduce un número: "))
finally:
    print("Bloque finally ejecutado")

# 30. Multiples Except
try:
    num = int(input("Introduce un número: "))
    resultado = 10 / num
except ValueError:
    print("Eso no es un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
    
    # 31. Sumar Dígitos
num = input("Introduce un número: ")
suma = sum(int(digito) for digito in num)
print(f"La suma de los dígitos es {suma}")

# 32. Número Primo
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("Introduce un número: "))
if es_primo(num):
    print(f"{num} es un número primo")
else:
    print(f"{num} no es un número primo")

# 33. Invertir Cadena
cadena = input("Introduce una cadena: ")
cadena_invertida = cadena[::-1]
print(f"La cadena invertida es: {cadena_invertida}")

# 34. Contar Vocales
cadena = input("Introduce una cadena: ").lower()
vocales = "aeiou"
contador = sum(1 for letra in cadena if letra in vocales)
print(f"La cadena tiene {contador} vocales")

# 35. Palíndromo
cadena = input("Introduce una cadena: ").lower()
cadena_sin_espacios = cadena.replace(" ", "")
if cadena_sin_espacios == cadena_sin_espacios[::-1]:
    print("La cadena es un palíndromo")
else:
    print("La cadena no es un palíndromo")

# 36. Máximo de Tres
def maximo_de_tres(a, b, c):
    return max(a, b, c)

print(maximo_de_tres(5, 10, 7))

# 37. Tabla de Multiplicar
num = int(input("Introduce un número: "))
for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")

# 38. Sumar Lista
def sumar_lista(lista):
    return sum(lista)

print(sumar_lista([1, 2, 3, 4, 5]))

# 39. Producto de Lista
def producto_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

print(producto_lista([1, 2, 3, 4, 5]))

# 40. Encontrar el Mínimo
def encontrar_minimo(lista):
    return min(lista)

print(encontrar_minimo([4, 2, 8, 1, 9]))

# 41. Contar Elementos
lista = [1, 2, 3, 4, 5]
print(f"La lista tiene {len(lista)} elementos")

# 42. Remover Duplicados
def remover_duplicados(lista):
    return list(set(lista))

print(remover_duplicados([1, 2, 2, 3, 4, 4, 5]))

# 43. Ordenar Lista
lista = [4, 2, 8, 1, 9]
lista_ordenada = sorted(lista)
print(f"La lista ordenada es: {lista_ordenada}")

# 44. Merge Sorted Lists
def merge_sorted_lists(lista1, lista2):
    return sorted(lista1 + lista2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

# 45. Anagramas
def son_anagramas(cadena1, cadena2):
    return sorted(cadena1.replace(" ", "").lower()) == sorted(cadena2.replace(" ", "").lower())

cadena1 = input("Introduce la primera cadena: ")
cadena2 = input("Introduce la segunda cadena: ")

if son_anagramas(cadena1, cadena2):
    print("Las cadenas son anagramas")
else:
    print("Las cadenas no son anagramas")

# 46. Generador de Contraseñas
import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for i in range(longitud))

longitud = int(input("Introduce la longitud de la contraseña: "))
print(f"Contraseña generada: {generar_contraseña(longitud)}")

# 47. Calculadora Simple
def calculadora(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        return "Operación no válida"

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")
print(f"Resultado: {calculadora(num1, num2, operacion)}")

# 48. Conversión de Temperatura
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcion = input("Elige la conversión: (1) Celsius a Fahrenheit, (2) Fahrenheit a Celsius: ")

if opcion == "1":
    celsius = float(input("Introduce la temperatura en Celsius: "))
    print(f"{celsius} °C es {celsius_a_fahrenheit(celsius)} °F")
elif opcion == "2":
    fahrenheit = float(input("Introduce la temperatura en Fahrenheit: "))
    print(f"{fahrenheit} °F es {fahrenheit_a_celsius(fahrenheit)} °C")
else:
    print("Opción no válida")

# 49. Contador de Palabras
cadena = input("Introduce una cadena: ")
palabras = cadena.split()
print(f"La cadena tiene {len(palabras)} palabras")

# 50. Suma de Pares e Impares
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_pares = sum(num for num in lista if num % 2 == 0)
suma_impares = sum(num for num in lista if num % 2 != 0)
print(f"Suma de pares: {suma_pares}, Suma de impares: {suma_impares}")

## PARTE 2 ##

# 7. Variables de Entorno
import os

def leer_variables_entorno():
    """
    Lee variables de entorno y las utiliza para la configuración del programa.
    
    Returns:
    dict: Un diccionario con las variables de entorno relevantes.
    """
    config = {
        "DB_HOST": os.getenv("DB_HOST", "localhost"),
        "DB_PORT": os.getenv("DB_PORT", "5432"),
        "DEBUG_MODE": os.getenv("DEBUG_MODE", "False")
    }
    return config

# Ejemplo de uso
configuracion = leer_variables_entorno()
print(configuracion)

# 8. Serialización JSON
import json

def serializar_datos(datos):
    """
    Serializa datos en formato JSON.
    
    Parameters:
    datos (dict): Datos a serializar.
    
    Returns:
    str: Cadena JSON resultante.
    """
    return json.dumps(datos, indent=4)

def deserializar_datos(json_str):
    """
    Deserializa una cadena JSON a un diccionario.
    
    Parameters:
    json_str (str): Cadena JSON a deserializar.
    
    Returns:
    dict: Diccionario resultante.
    """
    return json.loads(json_str)

# Ejemplo de uso
datos = {"nombre": "Alice", "edad": 30, "ciudad": "Madrid"}
json_str = serializar_datos(datos)
print(json_str)

datos_recuperados = deserializar_datos(json_str)
print(datos_recuperados)

# 9. Expresiones Regulares
import re

def validar_correo(correo: str) -> bool:
    """
    Valida una dirección de correo electrónico utilizando expresiones regulares.
    
    Parameters:
    correo (str): Dirección de correo electrónico a validar.
    
    Returns:
    bool: True si la dirección es válida, False en caso contrario.
    """
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, correo) is not None

# Ejemplo de uso
correo = "ejemplo@correo.com"
print(validar_correo(correo))

# 10. Conversiones Avanzadas
import json

def convertir_json_a_diccionario(json_str: str):
    """
    Convierte una cadena JSON a un diccionario.
    
    Parameters:
    json_str (str): Cadena JSON a convertir.
    
    Returns:
    dict: Diccionario resultante.
    """
    return json.loads(json_str)

def convertir_diccionario_a_json(diccionario: dict) -> str:
    """
    Convierte un diccionario a una cadena JSON.
    
    Parameters:
    diccionario (dict): Diccionario a convertir.
    
    Returns:
    str: Cadena JSON resultante.
    """
    return json.dumps(diccionario, indent=4)

# Ejemplo de uso
json_str = '{"nombre": "Bob", "edad": 25, "habilidades": ["Python", "Django"]}'
diccionario = convertir_json_a_diccionario(json_str)
print(diccionario)

json_resultante = convertir_diccionario_a_json(diccionario)
print(json_resultante)

# 11. Manejo de Fechas
from datetime import datetime

def calcular_diferencia_dias(fecha1: str, fecha2: str) -> int:
    """
    Calcula la diferencia en días entre dos fechas.
    
    Parameters:
    fecha1 (str): La primera fecha en formato 'YYYY-MM-DD'.
    fecha2 (str): La segunda fecha en formato 'YYYY-MM-DD'.
    
    Returns:
    int: La diferencia en días entre las dos fechas.
    """
    formato = "%Y-%m-%d"
    f1 = datetime.strptime(fecha1, formato)
    f2 = datetime.strptime(fecha2, formato)
    return (f2 - f1).days

# Ejemplo de uso
fecha1 = "2023-01-01"
fecha2 = "2024-01-01"
print(calcular_diferencia_dias(fecha1, fecha2))
Estructuras de Control

# 12. Compresión de Lista Avanzada
def es_primo(numero):
    """
    Verifica si un número es primo.
    
    Parameters:
    numero (int): Número a verificar.
    
    Returns:
    bool: True si el número es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Generar lista de números primos del 1 al 100
primos = [x for x in range(1, 101) if es_primo(x)]
print(primos)

# 13. Condicionales en Comprehensions
# Crear un diccionario de cuadrados de números del 1 al 10, pero solo incluir números pares
cuadrados_pares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(cuadrados_pares)

# 14. Iteradores Personalizados
class Cuadrados:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            resultado = self.i ** 2
            self.i += 1
            return resultado
        else:
            raise StopIteration

# Ejemplo de uso
iterador = Cuadrados(5)
for numero in iterador:
    print(numero)

# 15. Recursión: Torre de Hanoi
def torre_hanoi(n, origen, destino, auxiliar):
    """
    Resuelve el problema de la Torre de Hanoi.

    Parameters:
    n (int): Número de discos.
    origen (str): El nombre de la torre origen.
    destino (str): El nombre de la torre destino.
    auxiliar (str): El nombre de la torre auxiliar.
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    torre_hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    torre_hanoi(n-1, auxiliar, destino, origen)

# Ejemplo de uso
torre_hanoi(3, 'A', 'C', 'B')

# 16. Uso de itertools para generar todas las permutaciones de una lista
import itertools

def generar_permutaciones(lista):
    """
    Genera todas las permutaciones de una lista de elementos.
    
    Parameters:
    lista (list): Lista de elementos.
    
    Returns:
    list: Lista de tuplas, cada una representando una permutación.
    """
    return list(itertools.permutations(lista))

# Ejemplo de uso
elementos = [1, 2, 3]
permutaciones = generar_permutaciones(elementos)
print(permutaciones)

 # 17. Generador de números de Fibonacci   
def generador_fibonacci():
    """
    Generador que produce una secuencia infinita de números de Fibonacci.
    
    Yields:
    int: El siguiente número en la secuencia de Fibonacci.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Ejemplo de uso
fibonacci = generador_fibonacci()
for _ in range(10):
    print(next(fibonacci))

#18. Bucles Eficientes con Generadores para Procesar un Archivo Grande
def procesar_archivo_linea_por_linea(ruta_archivo):
    """
    Procesa un archivo de texto grande línea por línea utilizando generadores.
    
    Parameters:
    ruta_archivo (str): Ruta del archivo a procesar.
    
    Yields:
    str: Cada línea del archivo.
    """
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            yield linea.strip()

# Ejemplo de uso
ruta = "archivo_grande.txt"
for linea in procesar_archivo_linea_por_linea(ruta):
    print(linea)
Funciones y Módulos

#19. Decorador para Registrar la Entrada y Salida de una Función
import functools
import datetime

def registrar_entrada_salida(func):
    """
    Decorador que registra la entrada y salida de una función en un archivo de log.
    
    Parameters:
    func (function): Función a decorar.
    
    Returns:
    function: Función decorada.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        entrada = f"Entrada: {datetime.datetime.now()} - args: {args}, kwargs: {kwargs}\n"
        resultado = func(*args, **kwargs)
        salida = f"Salida: {datetime.datetime.now()} - resultado: {resultado}\n"
        with open("log.txt", "a") as archivo_log:
            archivo_log.write(entrada)
            archivo_log.write(salida)
        return resultado
    return wrapper

# Ejemplo de uso
@registrar_entrada_salida
def suma(a, b):
    return a + b

resultado = suma(10, 20)
print(resultado)

# 20. Función de Orden Superior
def aplicar_funcion_a_lista(funcion, lista):
    """
    Aplica una función a cada elemento de una lista.
    
    Parameters:
    funcion (function): Función a aplicar.
    lista (list): Lista de elementos.
    
    Returns:
    list: Lista de resultados.
    """
    return [funcion(x) for x in lista]

# Ejemplo de uso
def cuadrado(x):
    return x ** 2

lista = [1, 2, 3, 4]
resultado = aplicar_funcion_a_lista(cuadrado, lista)
print(resultado)

# 21. Función Parcial con functools.partial
from functools import partial

def multiplicar(a, b):
    return a * b

# Crear una función parcial que siempre multiplique por 2
multiplicar_por_2 = partial(multiplicar, 2)

# Ejemplo de uso
print(multiplicar_por_2(5))  # Output: 10

# 22. Módulos Personalizados con Funciones Matemáticas Avanzadas

# matematicas.py

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número.

    Parameters:
    n (int): Número del que se quiere calcular el factorial.

    Returns:
    int: Factorial del número.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def combinaciones(n: int, k: int) -> int:
    """
    Calcula el número de combinaciones posibles (n choose k).
    
    Parameters:
    n (int): Total de elementos.
    k (int): Número de elementos seleccionados.
    
    Returns:
    int: Número de combinaciones.
    """
    return factorial(n) // (factorial(k) * factorial(n - k))

# archivo_principal.py
from matematicas import factorial, combinaciones

print(factorial(5))  # Output: 120
print(combinaciones(5, 2))  # Output: 10

# 23. Importación Dinámica de Módulo
def importar_modulo(nombre_modulo):
    """
    Importa dinámicamente un módulo en tiempo de ejecución basado en la entrada del usuario.
    
    Parameters:
    nombre_modulo (str): Nombre del módulo a importar.
    
    Returns:
    module: El módulo importado.
    """
    modulo = __import__(nombre_modulo)
    return modulo

# Ejemplo de uso
nombre_modulo = input("Ingresa el nombre del módulo que deseas importar: ")
modulo = importar_modulo(nombre_modulo)
print(f"El módulo {nombre_modulo} ha sido importado.")

# 24. Context Managers con contextlib.contextmanager
from contextlib import contextmanager

@contextmanager
def manejar_archivo_seguro(ruta_archivo, modo):
    """
    Context manager personalizado para manejar archivos de manera segura.
    
    Parameters:
    ruta_archivo (str): Ruta del archivo.
    modo (str): Modo en que se abrirá el archivo.
    
    Yields:
    file: Archivo abierto.
    """
    archivo = open(ruta_archivo, modo)
    try:
        yield archivo
    finally:
        archivo.close()

# Ejemplo de uso
with manejar_archivo_seguro("archivo.txt", "w") as archivo:
    archivo.write("Hola, Mundo!")
Manejo de Excepciones

# 25. Excepciones Personalizadas
class ValorInvalidoError(Exception):
    """Excepción personalizada para valores inválidos."""
    pass

def validar_entrada(valor):
    """
    Valida la entrada del usuario y lanza una excepción personalizada si el valor es inválido.
    
    Parameters:
    valor (int): Valor a validar.
    
    Raises:
    ValorInvalidoError: Si el valor no está en el rango permitido.
    """
    if not (0 <= valor <= 100):
        raise ValorInvalidoError(f"El valor {valor} no es válido. Debe estar entre 0 y 100.")

# Ejemplo de uso
try:
    validar_entrada(150)
except ValorInvalidoError as e:
    print(e)

# 26. Propagación de Excepciones
def funcion_interna():
    """
    Función que lanza una excepción.
    
    Raises:
    ValueError: Excepción que se lanza para propagar.
    """
    raise ValueError("Algo salió mal en la función interna.")

def funcion_externa():
    """
    Función que llama a otra y propaga la excepción.
    """
    try:
        funcion_interna()
    except ValueError as e:
        print(f"Error capturado en funcion_externa: {e}")
        raise

# Ejemplo de uso
try:
    funcion_externa()
except ValueError as e:
    print(f"Excepción propagada hasta el nivel superior: {e}")

# 27. Reintento Automático con Decorador
import functools
import time

def reintentar(excepciones, intentos=3, retraso=2):
    """
    Decorador que intenta ejecutar una función varias veces en caso de una excepción específica.
    
    Parameters:
    excepciones (tuple): Excepciones a capturar para reintentar.
    intentos (int): Número de intentos.
    retraso (int): Tiempo de espera entre intentos.
    
    Returns:
    function: Función decorada.
    """
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(intentos):
                try:
                    return func(*args, **kwargs)
                except excepciones as e:
                    print(f"Error: {e}. Intentando de nuevo ({i+1}/{intentos})...")
                    time.sleep(retraso)
            raise RuntimeError("Se agotaron todos los intentos.")
        return wrapper
    return decorador

# Ejemplo de uso
@reintentar((ValueError,))
def division(a, b):
    if b == 0:
        raise ValueError("División por cero!")
    return a / b

try:
    print(division(10, 0))
except RuntimeError as e:
    print(e)