##########################################################
### Parameters vs Arguments
##########################################################
def print_name(name): # name is the parameter
  print(name)

print_name('Alex') # 'Alex' is the argument



##########################################################
### Positional vs Keyword args
##########################################################
def foo(a, b, c):
  print(a, b, c)

# positional arguments
foo(1, 2, 3)

# keyword arguments
foo(a=1, b=2, c=3)
foo(b=2, c=5, a=3) # The order is not important here

# mix of both
foo(1, b=7, c=10)

# This is not allowed:
# foo(1, b=2, 3) # positional argument after keyword argument
# foo(1, b=2, a=3) # multiple values for argument 'a'



##########################################################
### Default arguments
##########################################################
def bar(a, b, c, d=17):
  print(a, b, c, d)

bar(1, 2, 3, 4)
bar(1, b=2, c=3, d=150)
bar(1, 2, 3)

# not allowed: default arguments must be at the end
# def bar(a, b=2, c, d=4):
#     print(a, b, c, d)



############################################################################
### Variable-length arguments (*args, **kwargs)
############################################################################
def zoo(a, b, *args, **kwargs):
  print(a, b)
  for arg in args:
    print(arg)
  for kwarg in kwargs:
    print(kwarg, kwargs[kwarg])

# 3, 4, 5 are combined into args
# six and seven are combined in kwargs
zoo(1, 2, 3, 4, 5, six=6, seven=7)

# omitting of args or kwargs is possible
zoo(1, 2, three=3)

# If you write '*,' in your function parameter list, all parameters after that must be passed as keyword arguments.
def goo(a, b, *, c, d):
  print(a, b, c, d)

goo(1, 2, c=12, d=20)
# not allowed:
# foo(1, 2, 3, 4)

# arguments after variable-length arguments must be keyword arguments
def moo(*args, last):
  for arg in args:
    print(arg)
  print(last)

moo(8, 9, 10, last=50)




########################################################
### Unpacking into arguments
########################################################
def test_unpacking(a, b, c):
  print(a, b, c)

mylist = [1, 2, 3] # or tuple
test_unpacking(*mylist)

mydict = {'a': 1, 'b': 2, 'c': 3}
# my_dict = {'a': 1, 'b': 2, 'd': 3} # not possible since wrong keyword
test_unpacking(**mydict)




########################################################
### Local vs Global vars
########################################################
def foo1():
  x = number
  print(f"number in function {x}")

def foo2():
  global number
  number = 3
  x = number
  print(f"number in function {x}")

number = 0
print('number before foo1(): ', number)
foo1()
print('number after foo1(): ', number)

print('number before foo2(): ', number)
foo2()
print('number after foo2(): ', number)


number = 0

def foo3():
  number = 3

print('number before foo3(): ', number)
foo3() # does not modify the global variable
print('number after foo3(): ', number)




########################################################
### Passing parameters
########################################################

# immutable objects -> no change
def test_func1(x):
  x = 5 # x += 5 also no effect since x is immutable and a new variable must be created

var = 10
print('var before test_func1():', var)
test_func1(var)
print('var after test_func1()', var)

# mutable objects -> change
def test_func2(a_list):
  a_list.append(18)

mylist = [1, 2, 3]
print('var before test_func2():', mylist)
test_func2(mylist)
print('var after test_func2()', mylist)

# immutable objects within a mutable object -> change
def test_func3(a_list):
  a_list[0] = 25
  a_list[2] = "Andrew"

mylist = [1, 2, "James"]
print("mylist before test_func3(): ", mylist)
test_func3(mylist)
print("mylist after test_func3(): ", mylist)

# Rebind a mutable reference -> no change
def test_func4(a_list):
  a_list = [100, 200, 300]
  a_list.append(400)

mylist = [10, 20, 30]
print("mylist before test_func4(): ", mylist)
test_func4(mylist)
print("mylist after test_func4(): ", mylist)


# another example with rebinding references:
def roo(a_list):
    a_list += [4, 5] # this chanches the outer variable
    
def hoo(a_list):
    a_list = a_list + [4, 5] # this rebinds the reference to a new local variable

my_list = [1, 2, 3]
print('my_list before roo():', my_list)
roo(my_list)
print('my_list after roo():', my_list)

my_list = [1, 2, 3]
print('my_list before hoo():', my_list)
hoo(my_list)
print('my_list after hoo():', my_list)