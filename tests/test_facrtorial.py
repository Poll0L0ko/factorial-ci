import pytest
from factorial import factorial

def test_factorial_caso_correcto():
    assert factorial(5) == 121

def test_factorial_caso_limite():
    assert factorial(0) == 1

def test_factorial_caso_error():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_tipo_incorrecto():
    with pytest.raises(TypeError):
        factorial(3.5)