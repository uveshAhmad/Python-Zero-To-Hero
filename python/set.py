#  A set is a collection which is unordered, unchangeable*, and unindexed , and do not allow duplicate values.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Note: Sets are unordered, so you cannot be sure in which order the items will appear.


thisset = {"apple", "banana", "cherry"}
print(thisset)



#Dublicate value is ignored

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# O/P:- 
# {'banana', 'cherry', 'apple'}



# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)




# Get the number of items in a set:

thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# <class 'set'>
#Set constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


# Once a set is created, you cannot change its items, but you can add new items.
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# O/P : {'apple', 'orange', 'cherry', 'banana'}




# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# O/P: {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}





# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Example
# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)



# Remove Element in Set  method-1
# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


# Remove Element in Set  method-2
# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)



# Remove Element in Set  method-3
# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# Example
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)



# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)




# Iterate the Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
# O/P : 
# apple
# cherry
# banana


# JOINS


#Union
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# O/P : {'a', 2, 'c', 3, 1, 'b'}

#Update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# O/P : {3, 'a', 'c', 1, 'b', 2}
# Note: Both union() and update() will exclude any duplicate items.

#Intersection

#1>  intersection_update()
# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#2>  intersection()
# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)



#Symmetric difference
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# Example
# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
print(z)


