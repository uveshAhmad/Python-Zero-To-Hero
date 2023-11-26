 

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:


thislist = ["apple", "banana", "cherry"]
print(thislist)

# Example
# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["abc", 34, True, 40, "male"]
print(list1)


# Example
# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))   #   output <class 'list'>


# Example
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


#------------------------------------------------------------------------------------
# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Example
# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#  O/P : cherry 


# Example
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Example
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


# check element present in list or not
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


# ExampleGet your own Python Server
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)




# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#O/P:-- ['apple', 'banana', 'watermelon', 'cherry']



# ExampleGet your own Python Server
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Example
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Example
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

 

#  Remove Specified Item
# The remove() method removes the specified item.
# ExampleGet your own Python Server
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)



# The pop() method removes the specified index.
# Example
# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# O/P :- ['apple', 'cherry']
thislist.pop()
print(thislist)
# O/P :- ['apple', 'banana']





# The del keyword also removes the specified index:
# Example
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist[0])    #banana
print(thislist)
# O/P :- ['banana', 'cherry']
thislist = ["apple", "banana", "cherry"]
del thislist
# print(thislist)   gave error because del the list completely





# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
 

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# 2nd method 
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# 3rd method 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


# 4th method
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]





fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# O/P :- 
# ['apple', 'banana', 'mango']
#Short form above example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
