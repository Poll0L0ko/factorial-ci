"""
Módulo: factorial
Contiene la función factorial(numero).

Reglas:
1. Acepta solo enteros.
2. No acepta negativos.
3. factorial(0) = 1
"""

def factorial(numero: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        numero (int): Entero no negativo.

    Returns:
        int: Factorial del numero.

    Raises:
        TypeError: Si numero no es entero.
        ValueError: Si numero es negativo.
    """
    if not isinstance(numero, int):
        raise TypeError("El número debe ser un entero (int).")

    if numero < 0:
        raise ValueError("El número no puede ser negativo.")

    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado