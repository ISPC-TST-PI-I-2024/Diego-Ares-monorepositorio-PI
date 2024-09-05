
# Clases y Objetos

Este documento proporciona una guía sobre cómo utilizar clases y objetos en Python.

## Introducción a la Programación Orientada a Objetos

La programación orientada a objetos (POO) es un paradigma de programación que utiliza "objetos" y sus interacciones para diseñar aplicaciones y programas.

## Definición de Clases

Una clase es un plano para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase pueden utilizar.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

## Creación de Objetos
Un objeto es una instancia de una clase.

```python
persona1 = Persona("Alice", 30)
print(persona1.nombre, persona1.edad)
```

## Métodos de Instancia
Los métodos de instancia son funciones definidas dentro de una clase que operan sobre instancias de esa clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"
    
persona1 = Persona("Alice", 30)
print(persona1.saludar())
```

## Atributos de Clase y de Instancia
Los atributos de clase son compartidos por todas las instancias de una clase, mientras que los atributos de instancia son únicos para cada instancia.

```python
class Persona:
    especie = "Humano"  # Atributo de clase
    
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad
    
persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)
print(persona1.especie, persona1.nombre)
print(persona2.especie, persona2.nombre)
```

## Métodos Especiales
Los métodos especiales, también conocidos como métodos mágicos, son funciones especiales que se definen mediante doble guión bajo al principio y al final del nombre del método. Un ejemplo común es el método __str__.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"
    
persona1 = Persona("Alice", 30)
print(persona1)
```

## Ejercicios
1. Define una clase Coche con atributos marca, modelo y año. Crea una instancia de Coche y muestra sus atributos.
2. Agrega un método acelerar a la clase Coche que imprima un mensaje indicando que el coche está acelerando.
3. Define una clase Rectangulo con atributos largo y ancho, y un método que calcule el área del rectángulo. Crea una instancia de Rectangulo y muestra el área.
4. Crea una clase Libro con atributos de instancia para el título y el autor, y un atributo de clase para contar el número total de libros creados. Implementa un método para mostrar la información del libro.
