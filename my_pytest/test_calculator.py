import pytest
import calculator

def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2

def test_subtract():
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(2, 3) == -1

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 3) == -3

def test_divide():
    assert calculator.divide(6, 2) == 3
    assert calculator.divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(1, 0)
