import random

# random float in [0,1]
a = random.random()
print(a)

# random integer in range [a,b]. b is included
a = random.randint(1,10)
print(a)

# random integer in range [a,b]. b is excluded
a = random.randrange(1,10)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose k unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"), k=3)
print(a)

a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

random.seed(1)
print('Seeding with 1...')
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(1)
print('Seeding with 1...')
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(10)
print('Seeding with 1...\n')
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

random.seed(10)
print('Seeding with 1...\n')
print(random.random())
print(random.uniform(1,10))
print(random.choice(list("ABCDEFGHI")))

import secrets

# random integer in range [0, n].
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(5)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)

import numpy as np

# array with 3 real numbers
a = np.random.rand(3)
print(a)

# array with values from [0, 10] with size 3
a = np.random.rand(0, 10, 3)
print(a)

# array with values from [0, 10] with dimensions 3, 4
a = np.random.randint(0, 10, (3, 4))
print(a)

# randomly shuffle an array !!!only on the first axis of the multi-dimensional array
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)