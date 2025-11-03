def add(number_one, number_two):
  return number_one + number_two

def divide(number_one, number_two):
  if number_two == 0:
    raise ValueError
  return number_one / number_two

def subtract(number_one, number_two):
  return number_one - number_two

def abs_subtract(number_one, number_two):
  return abs(number_one - number_two)