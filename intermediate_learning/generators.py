def countdown(num):
  print("Starting")
  while num > 0:
    yield num
    num -= 1

#This does not execute the function
cd = countdown(3)

# This will print "Starting" and the first yield value
print(next(cd))
print(next(cd))
print(next(cd))

try:
  print(next(cd))
except StopIteration as e:
  print("The generator has finished")

# Use it for functions that take iterables as input
cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)

# Big advantage: Generators save memory!
# Since the values are generated lazily, i.e. only when needed, it saves a lot of memory, 
# especially when working with large data. Furthermore, we do not need to wait until all 
# the elements have been generated before we start to use them.
import sys
from timeit import default_timer as timer

def firstn(n):
  num, nums = 0, []
  while num < n:
    nums.append(num)
    num += 1
  return nums

def firstn_gen(n):
  num = 0
  while num < n:
    yield num
    num += 1

start = timer()
sum_of_first_n = sum(firstn(1000))
stop = timer()
print(sum_of_first_n)
print(sys.getsizeof(firstn(1000)), "bytes") ### 9016 bytes
print(stop - start)

start = timer()
sum_of_first_n = sum(firstn_gen(1000))
stop = timer()
print(sum_of_first_n)
print(sys.getsizeof(firstn_gen(1000)), "bytes") ### 112 bytes
print(stop - start)

def fibonacci(limit):
  a, b = 0, 1
  while a < limit:
    yield a
    a, b = b, a + b

fib = fibonacci(10)
print(list(fib))

# generator expressions. Generally slower because of func calls overhead
start = timer()
mygenerator = (i for i in range(1000) if i % 2 == 0)
stop = timer()
print(sys.getsizeof(mygenerator))
print(stop - start)

# list expressions
start = timer()
mylist = [i for i in range(1000) if i % 2 == 0]
stop = timer()
print(sys.getsizeof(mylist))
print(stop - start)

# Example for an iterable object
class Firstn:
  def __init__(self, n):
    self.n = n
    self.num = 0
  
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.num < self.n:
      cur = self.num
      self.num += 1
      return cur
    else:
      raise StopIteration()

firstn_obj = Firstn(1000)
print(sum(firstn_obj))