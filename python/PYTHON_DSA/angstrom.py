n = 153  # or n=int(input()) -> taking input from user
s = n  # assigning input value to the s variable
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")
    
    
    
    
    
    
def is_armstrong(num):
    num_str = str(num)
    n = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**n
    if sum == num:
        return True
    else:
        return False
num=153
print(is_armstrong(num))







import math
 
def isArmstrong(num):
    n = num
    numDigits = 0
    sum = 0
     
    # Find number of digits in num
    while n > 0:
        n //= 10
        numDigits += 1
     
    n = num
     
    # Calculate sum of digits raised to the power of numDigits
    while n > 0:
        digit = n % 10
        sum += math.pow(digit, numDigits)
        n //= 10
     
    # Check if num is Armstrong number or not
    if sum == num:
        return True
    return False
 
 
 
 
 
def is_armstrong_number(number):
    return sum(int(digit)**len(str(number)) for digit in str(number)) == number
# Example usage:
num = 153
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
    
    
    
    