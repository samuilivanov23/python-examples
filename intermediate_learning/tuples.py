mytuple = ("Max", 28, "Boston")
print(mytuple)

mytuple = ("Max",) # for single element tuple put comma at the end. Otherwise it is STRING
print(mytuple)

mytuple = tuple(["Max", 28, "Boston"])
item = mytuple[-1]
print(item)

for i in mytuple:
  print(i)

if "Boston" in mytuple:
  print("yes")
else:
  print("no")

print(len(mytuple))
print(mytuple.count('Max')) # Returns the index of the first found element

mylist = list(mytuple) # and vice-versa
print(mylist)

a = (1, 2, 3, 4, 5, 6, 7)
print(a[3:6])
print(a[:4:2]) # with step element... every second element from start to index 4

name, age, city = mytuple
print(name, age, city)

i1, *i2, i3 = a
print(i1)
print(i2) # list from 2 to 6
print(i3)

import sys
mylist = [0, 1, 2, "hello", True]
mytuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(mylist), "bytes") # 96 bytes
print(sys.getsizeof(mytuple), "bytes") # 80 bytes

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000)) # almost 10 times faster