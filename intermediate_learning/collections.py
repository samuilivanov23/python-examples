from collections import Counter, namedtuple
a = "aaabbbccccc"
counter = Counter(a)
print(counter)
print(counter.items())
print(counter.keys())
print(counter.values())
print(counter.most_common(1)[0][0])
print(list(counter.elements()))

Point = namedtuple("Point", "x,y")
pt1 = Point(4, -5)
print(pt1)