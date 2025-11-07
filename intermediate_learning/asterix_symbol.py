# multiplication
result = 7 * 5
print(result)

# power operation
result = 2 ** 4
print(result)

# lists
zeros = [0] * 10
onetwos = [1, 2] * 5
print(zeros)
print(onetwos)

# tuples
zeros =(0,) * 10
onetwos = (1, 2) * 5
print(zeros)
print(onetwos)

# string
A_string = "A" * 10
AB_string = "AB" * 5
print(A_string)
print(AB_string)

# unpacking containers
numbers = (1, 2, 3, 4, 5, 6, 7)
*first, end = numbers
print(first)
print(end)

first, *end = numbers
print(first)
print(end)

first, *middle, last = numbers
print(first)
print(middle)
print(last)


# dump iterables into list and merge them
mytuple = (1, 2, 3)
myset = {4, 5, 6}
mylist = [*mytuple, *myset]
print(mylist)

# merging two dicts
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}
dict3 = {**dict1, **dict2}
print(dict3)