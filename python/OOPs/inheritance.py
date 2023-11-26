# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname )
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
class Student(Person):
  def __init__(self, fname, lname , year):
    #yeh jo upar fun bnaya h ye inherit nhi krega or override kr dega parent class ke __init__ ko 
    #isse bachne ke liye hame parent class ke __init__ ko call lagana hoga 
 #Vimp.
 # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
 # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
 #To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
     Person.__init__(self, fname, lname ) # ye child class ke __init__ ke andar hi rhega OK
     super().__init__(fname , lname) # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
 #By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
     self.graduationyear = year  # adding some more properties in child class

     #add some methods in child class 
  def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  # crete object
x = Student("Mike", "Olsen" , 2019)
x.welcome()
 
