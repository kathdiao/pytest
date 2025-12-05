import pytest
import source.math_operations as math_operations

def test_add():
     result = math_operations.add(10 , 9)
     assert result == 19


def test_subtract():
    result = math_operations.subtract(10,9)
    assert result == 1


def test_multiply():
    result = math_operations.multiply(10,9)
    assert result == 90


def test_divide():
    result = math_operations.divide(10,9)
    assert round(result, 2) == 1.11
    #   NORMAL DIVISION


def test_decimal():
    result = math_operations.decimal(10,9)
    assert result == 1
    #   FLOOR DIVISION


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        math_operations.divide(10,0)
#   HANDLING ERROR


def test_add_strings():
    result = math_operations.add("Hello ", "Kath")
    assert result == "Hello Kath"
#   STRING