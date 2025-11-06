mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict2 = dict(name="Max", age=28, city="New York")
print(mydict, mydict2)

print(mydict["name"])
#print(mydict["last_name"]) KeyError:

mydict["email"] = "testemail@xyz.com"
print(mydict)
mydict["email"] = "newemail@xyz.com"
print(mydict)

for i in mydict.keys():
  print(i)
for i in mydict.values():
  print(i)
for key, value in mydict.items():
  print(key, value)

del mydict["email"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

try:
  print(mydict["lastname"])
except:
  print("Error")

mydict = {"name": "Max", "age": 28, "city": "New York"}
mydict2 = dict(name="Max", age=20, email="testmail@xyz.com")
mydict.update(mydict2)
print(mydict)