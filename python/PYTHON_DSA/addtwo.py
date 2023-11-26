number1 = int(input("First number :"))
number2 = int(input("\n Second Number"))
sum = number1+number2
print(sum)



num1 = int(15)
num2 = int(12)
# Adding two nos
import operator
su = operator.add(num1,num2)
# printing values
print("Sum of {0} and {1} is {2}" .format(num1,
                                       num2, su))


def add(a,b):
  return a+b
 
#initializing the variables
num1 = 10
num2 = 5
 
#function calling and store the result into sum_of_twonumbers
sum_of_twonumbers = add(num1,num2)
 
#To print the result
print("Sum of {0} and {1} is {2};" .format(num1,
                           num2, sum_of_twonumbers))












add_numbers = lambda x, y: x + y
 
# Take input from the user
num1 = 1
num2 = 2
 
# Call the lambda function to add the two numbers
result = add_numbers(num1, num2)
 
# Print the result
print("The sum of", num1, "and", num2, "is", result)






def add_numbers_recursive(x, y):
    if y == 0:
        return x
    else:
        return add_numbers_recursive(x + 1, y - 1)
 
# Take input from the user
num1 = 1
num2 = 2
 
# Call the recursive function to add the two numbers
result = add_numbers_recursive(num1, num2)
 
# Print the result
print("The sum of", num1, "and", num2, "is", result)




