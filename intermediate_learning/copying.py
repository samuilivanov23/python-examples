# This will only create a new variable with the same reference. 
# Modifying one will affect the other.
list_a = [1, 2, 3, 4, 5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)


### Shallow copy
# One level deep. Modifying on level 1 does not affect the other list. 
# Use copy.copy(), or object-specific copy functions/copy constructors.
import copy
list_a = [1, 2, 3, 4]
list_b = copy.copy(list_a)

list_b[0] = -10
print(list_a)
print(list_b)

# But with nested objects, modifying on level 2 or deeper does affect the other!
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.copy(list_a)

# affects the other!
list_a[0][0]= -10
print(list_a)
print(list_b)


### Deep copies
list_a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
list_b = copy.deepcopy(list_a)

# does not affect the other
list_a[0][0]= -10
print(list_a)
print(list_b)

### Custom objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Company:
  def __init__(self, boss, employee):
    self.boss = boss
    self.employee = employee

# Only copies the reference
p1 = Person("Paul", 37)
p2 = p1
p2.age = 42
print(p1.age)
print(p2.age)

# shallow copy
p1 = Person("Paul", 37)
p2 = copy.copy(p1)
p2.age = 42
print(p1.age)
print(p2.age)


# shallow copy will affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)

company_clone = copy.copy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)

# deep copy will NOT affect nested objects
boss = Person('Jane', 55)
employee = Person('Joe', 28)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company.boss.age)
print(company_clone.boss.age)