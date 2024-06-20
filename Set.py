set= {"mango","apple","banana","pear","carrot"}
print(set)
print(len(set))

for x in set:
    print(x)
b = "banana" in set
print(b)

set.add("orange")
set.clear()

print(set)
del set
print(set)
