import pytest
from calculadora import somar, subtrair, multiplicar, dividir

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, -1) == -2
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(-1, -1) == 0
    assert subtrair(0, 1) == -1

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, -1) == 1
    assert multiplicar(0, 5) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    with pytest.raises(ValueError, match="Não é possível dividir por zero"):
        dividir(10, 0)