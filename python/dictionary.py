#  Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# <class 'dict'>

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# another way to get value of key
x = thisdict.get("model")


#  to find all keys of dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()
print(x)
# dict_keys(['brand', 'model', 'year'])
# dict_values(['Ford', 'Mustang', 1964])
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])




car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change




# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example
# Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")




#update_value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
#another way to upadte the value 
thisdict.update({"year": 2020})
#Example
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict.update({"color": "red"})
print(thisdict)


#removing elements
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
thisdict.popitem() # remove last iteam 
print(thisdict)


# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
del thisdict #delete complete dictionary
thisdict.clear() # clear all the elements of dictionary
print(thisdict)









# Print all key names in the dictionary, one by one:
#Method-1
for x in thisdict:
 print(x)
 print(thisdict[x])
#Method-2
for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x)



# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)




#Nested Dictionary 
# Create a dictionary that contain three dictionaries:
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
print(myfamily["child2"]["name"])












