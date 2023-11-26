# Example
# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
# The youngest child is Linus

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")




# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")



# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
# Example
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()   # Noeway
my_function("Brazil")



# Passing a list through argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)



#Return Value
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))



# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example
def myfunction():
  pass



# Python program to illustrate 
# math module 
import math 
  
def Main(): 
    num = -85
  
    # fabs is used to get the absolute  
    # value of a decimal 
    num = math.fabs(num)  
    print(num) 
      
      
if __name__=="__main__": 
    Main() 



def fun():
    print("Inside Function")
 
 
fun()



# Lambda keyword
g = lambda x: x*x*x
 
print(g(7))



# Return keyword
def fun():
    S = 0
 
    for i in range(10):
        S += i
    return S
 
 
print(fun())
 

 
# Yield Keyword
 
 
def fun():
    S = 0
 
    for i in range(10):
        S += i
        yield S
 
 
for i in fun():
    print(i)



# Python program to illustrate  
# function with main 

# aise bhi chl jayega code bina main ke ok 
# def getInteger(): 
#     result = int(input("Enter integer: ")) 
#     return result 
  

# result=getInteger()
# print(result)
    
# # def Main(): 
# #     print("Started") 

def getInteger(): 
    result = int(input("Enter integer: ")) 
    return result 
  

result=getInteger()
print(result)
    
def Main(): 
    print("Started") 
  
    # calling the getInteger function and  
    # storing its returned value in the output variable 
    output = getInteger()      
    print(output) 
  
# now we are required to tell Python  
# for 'Main' function existence 
if __name__=="__main__": 
    Main() 



    import math as gfg
 
print(gfg.factorial(5))
