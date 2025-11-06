x = -5

try:
  if x < 0:
    raise Exception("x should be positive")
except Exception as e:
  print(e)

try:
  assert (x >= 0), "x is not positive"
except Exception as e:
  print(e)

try:
  a = 5 / 1
  a = a + "10"
except ZeroDivisionError as e:
  print(e)
except TypeError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print("everything is OK. Runs if no exception is catched")
finally:
  print("Runs every time")

class ValueTooHighError(Exception):
  pass

class ValueTooSmallError(Exception):
  def __init__(self, message, value):
    self.message = message
    self.value = value

def test_value(x):
  if x > 100:
    raise ValueTooHighError("Value is too high!")
  
  if x < 5:
    raise ValueTooSmallError("Value too small!", x)


try:
  test_value(57)
  test_value(1)
except ValueTooHighError as e:
  print(e)
except ValueTooSmallError as e:
  print(e.message, e.value)
except Exception as e:
  print(e)