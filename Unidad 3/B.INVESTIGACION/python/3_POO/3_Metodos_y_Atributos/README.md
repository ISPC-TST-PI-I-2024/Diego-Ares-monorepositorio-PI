# Métodos y Atributos

Este documento proporciona una guía sobre cómo utilizar métodos y atributos en Python.

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

## Métodos de Clase
Los métodos de clase son métodos que están vinculados a la clase en sí y no a una instancia específica. Se definen utilizando el decorador @classmethod.

```python
class Persona:
    numero_personas = 0
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Persona.numero_personas += 1
    
    @classmethod
    def contar_personas(cls):
        return f"Hay {cls.numero_personas} personas"

print(Persona.contar_personas())
persona1 = Persona("Alice", 30)
print(Persona.contar_personas())
```

## Métodos Estáticos
Los métodos estáticos son métodos que no están vinculados ni a la clase ni a las instancias. Se definen utilizando el decorador @staticmethod.

```python
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

print(Calculadora.sumar(3, 5))
```

## Atributos de Instancia
Los atributos de instancia son variables que pertenecen a una instancia específica de una clase.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Alice", 30)
print(persona1.nombre, persona1.edad)
```

## Atributos de Clase
Los atributos de clase son variables que pertenecen a la clase en sí y son compartidos por todas las instancias de la clase.

```python
class Persona:
    especie = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Alice", 30)
persona2 = Persona("Bob", 25)
print(persona1.especie, persona2.especie)
```

## Decoradores de Métodos
Los decoradores de métodos se utilizan para modificar el comportamiento de los métodos. Los decoradores comunes son @classmethod y @staticmethod.

```python
class Persona:
    @classmethod
    def metodo_de_clase(cls):
        pass
    
    @staticmethod
    def metodo_estatico():
        pass
```

## Ejercicios
1. Define una clase Coche con un atributo de clase numero_coches que cuente el número de instancias creadas. Agrega métodos de instancia para mostrar información del coche y un método de clase para mostrar el número total de coches.
2. Define una clase CuentaBancaria con métodos estáticos para validar el número de cuenta y calcular los intereses. Agrega métodos de instancia para depositar y retirar dinero.
3. Crea una clase Empleado con atributos de instancia nombre y salario, y un atributo de clase empresa. Agrega un método de instancia para mostrar la información del empleado y un método de clase para cambiar el nombre de la empresa.
4. Define una clase Matematicas con métodos estáticos para realizar operaciones matemáticas básicas como sumar, restar, multiplicar y dividir.
