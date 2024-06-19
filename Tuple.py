a = ("elephant","deer","tiger","bear","lion")
#prints whole tuple
print(a)
#we can access to any element of the tuple through its index.
print(a[3])
#if we want to reate a tuple with only one item in it then we should put a comma after the item.
b=("man",)
print(b)
#range in tuple
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
#prints the element from index 2 to index 4 but 4th index element is not included
#if we use -1 then the last element will be accessed
print(thistuple[2:4])
#reverses the tuple
print(thistuple[::-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
