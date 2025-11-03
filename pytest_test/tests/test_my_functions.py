import pytest
import time
import src.my_functions as my_functions

def test_add():
  result = my_functions.add(1, 4)
  assert result == 5

def test_subtract():
  result = my_functions.subtract(5, 2)
  assert result == 3

def test_abs_subtract():
  result = my_functions.abs_subtract(10, 15)
  assert result == 5

def test_add_strings():
  result = my_functions.add("I like ", "cheese burgers")
  assert result == "I like cheese burgers"

def test_divide():
  result = my_functions.divide(9, 3)
  assert result == 3

def test_divide_by_zero():
  with pytest.raises(ValueError):
    my_functions.divide(10, 0)

@pytest.mark.slow
def test_very_slow():
  time.sleep(5)
  result = my_functions.divide(9, 3)
  assert result == 3

@pytest.mark.skip(reason="This feature is currently broken!")
def test_add():
  assert my_functions.add(1, 2) == 3

@pytest.mark.xfail(reason="Division by zero is not allowed!")
def test_divide_by_zero():
  my_functions.divide(4, 0)