thisdict = {
  "brand": "Suzuki",
  "model": "Cultus",
  "year": 2013
}
thisdict["color"] = "Mettalic Green"
#x = thisdict["model"]
thisdict["year"] = 2020
print(thisdict)
#print(thisdict["model"])
#get length of list
#print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
mydict= thisdict.copy()
print(mydict)
print(type(thisdict))
#Use dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
#Get keys
x = thisdict.keys()
print(x)
#Add new item in the dictionary

