myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 2, 3])
print(myset)
print(set("Hello"))

myset.add(1)
myset.add(4)
myset.add(4)
myset.add(5)
print(myset)

myset.discard(4)
print(myset)

myset.pop()
print(myset)

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

diff = odds.difference(evens)
print(diff)

odds.update(evens)
print(odds)

odds.intersection_update(evens)
print(odds)

odds.difference_update(primes)
print(odds)

setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5}
setC = {8, 9, 10}
print(setA.issubset(setB))
print(setA.issuperset(setB))
print(setA.isdisjoint(setC))

a = frozenset([1, 2, 3, 4]) # imutable
print(a)