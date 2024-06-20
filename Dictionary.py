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

