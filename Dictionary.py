#dictionary in python
""" stores data in key value format.

"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
x=thisdict.get("model")
print(x)
print(thisdict["model"])

a=thisdict.keys()
b=thisdict.values()
print(a,b)

thisdict.update({"year": 2020})
print(thisdict)

mydict = {
    "name": "suren",
    "age": 20,
    "height": 6
    }
print(mydict)

dict2 = mydict.copy()
dict3 = dict(mydict)
print(dict3)
print(dict2)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
