import pytest
import source.my_functions as my_functions

def test_add():
     result = my_functions.add(10 , 9)
     assert result == 19

def test_subtract():
    result = my_functions.subtract(10,9)
    assert result == 1

def test_multiply():
    result = my_functions.multiply(10,9)
    assert result == 90

def test_divide():
    result = my_functions.divide(10,9)
    assert round(result, 2) == 1.11
    #   NORMAL DIVISION
    #   Laging may decimal (float)
    #   Kahit whole number result, float pa rin
    #

def test_decimal():
    result = my_functions.decimal(10,9)
    assert result == 1
    #   FLOOR DIVISION
    #   Division pero i-fi-FLOOR (ibaba) ang sagot
    #   Laging whole number (integer)
    #   Kahit may decimal dapat, tinatanggal niya pababa


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(10,0)
#   HANDLING ERROR


def test_add_strings():
    result = my_functions.add("Hello ", "Kath")
    assert result == "Hello Kath"
    