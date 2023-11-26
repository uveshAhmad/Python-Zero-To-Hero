# Python program to illustrate a tuple 
# creates a tuple which is immutable 
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
#When we say that tuples are ordered, it means that the items have a defined order, and 
#that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or
# remove items after the tuple has been created.
# Allow Duplicates
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


# Example
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# type print <class 'tuple'>

#constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



# Tupple ko   changable ya mutable bnane ke liye pehle tupple ko list me bna do fir list ko do
# dobara tupple me change kr do 
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#2nd method to add tuples
# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
 
# remove from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

print(thistuple)



# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists




# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
# O/P: -- 
# apple
# banana
# ['cherry', 'strawberry', 'raspberry']


# Join two tuples:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply of  tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
# print(mytuple)
# O/P:-- 
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')




# count()---> 	Returns the number of times a specified value occurs in a tuple
# index()--> 	Searches the tuple for a specified value and returns the position of where it was found

 
uvesh = ("u" , "v" , "e" , "s" ,"h" , "u" , "v" , "h")
result = uvesh.count("u")  # 2
print(result)
result = uvesh.index("h")  #4
print(result)


