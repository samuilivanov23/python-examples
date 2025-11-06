import functools

def start_end_decorator(func):
  def wrapper(*args, **kwargs):
    print("start")
    func(*args, **kwargs)
    print("end")
  return wrapper

@start_end_decorator
def print_name(name):
  print(name)

name = "Tom"
print_name(name)

def start_end_decorator2(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print("start")
    result = func(*args, **kwargs)
    print("end")
    return result
  return wrapper

@start_end_decorator2
def add_5(x):
  return x + 5

x = 10
result = add_5(x)
print(result)

print(add_5.__name__)
help(add_5)

def repeat(num_times):
  def decorator_repeat(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      for _ in range(num_times):
        result = func(*args, **kwargs)
      return result
    return wrapper
  return decorator_repeat

@repeat(num_times=3)
def greet(name):
  print(f"Hello {name}")

name = "Alex"
greet(name)


class CountCalls:
  def __init__(self, func):
    functools.update_wrapper(self, func)
    self.func = func
    self.num_calls = 0
  
  def __call__(self, *args, **kwargs):
    self.num_calls += 1
    print(f"Call {self.num_calls} of {self.func.__name__!r}")
    return self.func(*args, **kwargs)

@CountCalls
def say_hello(name):
  print(f"Hello {name}")

name = "Robert"
say_hello(name)
say_hello(name)
say_hello(name)
