# Principios SOLID

Este documento proporciona una guía sobre los principios SOLID en programación orientada a objetos.


## Introducción a los Principios SOLID

Los principios SOLID son un conjunto de cinco principios de diseño destinados a hacer que el software sea más comprensible, flexible y mantenible.

## Principio de Responsabilidad Única (SRP)

Cada clase debe tener una única responsabilidad y, por lo tanto, una única razón para cambiar.

```python
class Reporte:
    def generar_reporte(self):
        pass

class ReportePDF(Reporte):
    def exportar_pdf(self):
        pass
```

## Principio de Abierto/Cerrado (OCP)
Las entidades de software deben estar abiertas para su extensión, pero cerradas para su modificación.

```python
class Forma:
    def area(self):
        pass

class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14 * self.radio * self.radio
```

## Principio de Sustitución de Liskov (LSP)
Los objetos de una clase derivada deben ser reemplazables por objetos de la clase base sin alterar el correcto funcionamiento del programa.

```python
class Ave:
    def volar(self):
        pass

class Pato(Ave):
    def volar(self):
        return "Pato volando"

class Avestruz(Ave):
    def volar(self):
        raise Exception("Avestruz no puede volar")
```

## Principio de Segregación de Interfaces (ISP)
Una clase no debe ser forzada a implementar interfaces que no utiliza. Es mejor tener muchas interfaces específicas en lugar de una única interfaz general.

```python
class Imprimible:
    def imprimir(self):
        pass

class Escaneable:
    def escanear(self):
        pass

class Impresora(Imprimible):
    def imprimir(self):
        return "Imprimiendo..."

class Escaner(Escaneable):
    def escanear(self):
        return "Escaneando..."
```

## Principio de Inversión de Dependencias (DIP)
Los módulos de alto nivel no deben depender de los módulos de bajo nivel. Ambos deben depender de abstracciones.

```python
class Motor:
    def encender(self):
        pass

class Coche:
    def __init__(self, motor: Motor):
        self.motor = motor
    
    def encender(self):
        self.motor.encender()
```

## Ejercicios
1. Aplica el Principio de Responsabilidad Única (SRP) para refactorizar una clase Empleado que actualmente maneja tanto los detalles del empleado como la generación de su informe.
2. Aplica el Principio de Abierto/Cerrado (OCP) para agregar una nueva forma Triangulo sin modificar la clase Forma base.
3. Aplica el Principio de Sustitución de Liskov (LSP) asegurándote de que todas las subclases de Vehiculo puedan sustituir a Vehiculo sin errores.
4. Aplica el Principio de Segregación de Interfaces (ISP) para refactorizar una clase TodoEnUno que actualmente implementa tanto la impresión como el escaneo.
5. Aplica el Principio de Inversión de Dependencias (DIP) para refactorizar una clase Usuario que depende directamente de una clase ServicioEmail.
