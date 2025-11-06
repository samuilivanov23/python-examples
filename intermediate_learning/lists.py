mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist.append("watermelon")
for i in mylist:
  print(i)

if "cherry" in mylist:
  print("Cherry is in the list.")
else:
  print("Cherry is not in the list.")

mylist.pop()
print(mylist)

mylist.remove("apple")
print(mylist)

mylist.append("strawberry")
mylist.reverse()
print(mylist)

new_list = sorted(mylist)
print(new_list)

mylist = [0] * 5
mylist2 = [1, 2, 3, 4, 5]
new_list = mylist + mylist2
print(new_list)
print(new_list[2:6])

list_org = ["banana", "cherry", "apple"]
# list_copy = list_org.copy() || list_copy = list_org[:] || list_copy = list(list_org)
list_copy = list_org.copy() #if list_copy = list_org => both list will have the same value after the append
list_org.append("watermelon")
print(list_org)
print(list_copy)

mylist = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist]
print(mylist, b)