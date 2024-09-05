# script.py

def sumar(a, b):
    """
    Suma dos números.

    Parameters:
    a (int, float): El primer número a sumar.
    b (int, float): El segundo número a sumar.

    Returns:
    int, float: La suma de los dos números.
    """
    return a + b


def restar(a, b):
    """
    Resta el segundo número del primero.

    Parameters:
    a (int, float): El número del cual se va a restar.
    b (int, float): El número a restar.

    Returns:
    int, float: La diferencia entre los dos números.
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.

    Parameters:
    a (int, float): El primer número a multiplicar.
    b (int, float): El segundo número a multiplicar.

    Returns:
    int, float: El producto de los dos números.
    """
    return a * b


def dividir(a, b):
    """
    Divide el primer número por el segundo.

    Parameters:
    a (int, float): El número a dividir.
    b (int, float): El número divisor.

    Returns:
    int, float: El cociente de la división.

    Raises:
    ZeroDivisionError: Si `b` es 0.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b
