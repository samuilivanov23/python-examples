add10 = lambda x: x + 10
print(add10(5))

mult = lambda x,y: x*y
print(mult(2, 7))

points = [(1, 2), (15, 1), (5, -1), (10, 4)]
points_sorted = sorted(points, key=lambda x: x[1]) # sorts the list b the second elements in the tuples
print(points)
print(points_sorted)

points_sorted_based_on_sum = sorted(points, key=lambda x: x[0] + x[1])
print(points_sorted_based_on_sum)

a = [1, 2, 3, 4]
print(list(map(lambda x: x*2, a)))
print([x*2 for x in a])

print(list(filter(lambda x: x%2==0,  a)))
print([x for x in a if x%2==0])

from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a)