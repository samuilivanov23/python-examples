mystring = """Hello \
World!"""
print(mystring)

print(mystring[1::2])
print(mystring[::-1]) # reverse a string

greeting = "Hello "
name = "Tom"
print(greeting + name)

for char in greeting:
  print(char)

if 'T' in name:
  print("yes")
else:
  print("no")

print(greeting.strip())
print(mystring.upper()) # .lower()
print(mystring.endswith("World!"))
print(mystring.find('o')) # first found index
print(mystring.replace("World", "Universe"))

mystring = "how,are,you,doing"
mylist = mystring.split(",")
print(mylist)
newstring = ' '.join(mylist)
print(newstring)

from timeit import default_timer as timer
mylist = ['a'] * 6
print(mylist)

#bad approach
start = timer()
mystring = ''
for i in mylist:
  mystring += i
stop = timer()
print(stop - start)
print(mystring)

#more efficient approach with join
start = timer()
mystring = ''.join(mylist)
stop = timer()
print(stop - start) # 5 times faster execution
print(mystring)

print("This is formatting strings: %.2f" % 20.15)
print("This is formatting strings: {:.2f} and {}".format(20.15, name))
print(f"This is formatting strings: {20.15} and {name}")