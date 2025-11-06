from itertools import product, permutations, combinations, accumulate, groupby
import operator
a = [1, 2]
b = [3]
prod = product(a, b, repeat=2)
print(list(prod))

a = [1, 2, 3]
print(list(permutations(a)))

a = [1, 2, 3, 4]
print(list(combinations(a, 2)))

print(list(accumulate(a)))
print(list(accumulate(a, func=operator.mul)))

def smaller_than_3(x):
  return x < 3

groupby_obj = groupby(a, key=smaller_than_3) # or lambda x: x < 3
for key, value in groupby_obj:
  print(key, list(value))