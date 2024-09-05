# Herencia y Polimorfismo

Este documento proporciona una guía sobre cómo utilizar la herencia y el polimorfismo en Python.


## Introducción a la Herencia

La herencia permite crear una nueva clase a partir de una clase existente. La nueva clase hereda los atributos y métodos de la clase existente.

## Definición de Clases Base y Derivadas

Una clase base es la clase de la que se hereda. Una clase derivada es la nueva clase que hereda de la clase base.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"
```

## Sobrescritura de Métodos
La sobrescritura de métodos permite que una clase derivada proporcione una implementación específica de un método que ya está definido en su clase base.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"
```

## Uso de la Función super()
La función super() se utiliza para llamar a un método de la clase base desde una clase derivada.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido de animal"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hacer_sonido(self):
        return "Guau"
```

## Polimorfismo
El polimorfismo permite utilizar una misma interfaz para diferentes tipos de objetos.

```python
animales = [Perro("Firulais", "Labrador"), Gato("Misu")]

for animal in animales:
    print(animal.nombre, animal.hacer_sonido())
```

## Ejercicios
1. Define una clase base Vehiculo con un método moverse. Luego, define dos clases derivadas Coche y Bicicleta que sobrescriban el método moverse con comportamientos específicos.
2. Define una clase base Empleado con atributos nombre y salario, y un método mostrar_info. Luego, define dos clases derivadas Gerente y Ingeniero que sobrescriban el método mostrar_info y agreguen un atributo adicional.
3. Crea una clase base Forma con un método area que devuelva 0. Luego, define dos clases derivadas Rectangulo y Circulo que sobrescriban el método area con sus respectivas fórmulas.
4. Usa polimorfismo para iterar sobre una lista de objetos Vehiculo y llama al método moverse en cada objeto.